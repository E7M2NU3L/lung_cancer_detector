import torch
from torchvision import transforms
from PIL import Image

class CovidPredictor:
    def __init__(self, image : str) -> None:
        self.image = image

        self.transform = transforms.Compose([
            transforms.Resize((64, 64)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                std=[0.229, 0.224, 0.225])
        ])

         # Define class labels
        self.class_labels = ["Covid", "Normal"]
        self.output_dir = ""
        self.model = torch.load(self.output_dir)

    # Load and transform the image
    def preprocess_image(self):
        image = Image.open(self.image).convert("RGB")  # Ensure RGB format
        image = self.transform(self.image)  # Apply transformations
        image = image.unsqueeze(0)  # Add batch dimension
        return image

    def predict_image(self):
        image = self.preprocess_image(self.image)

        # Forward pass through the model
        with torch.no_grad():
            output = self.model(image)
            predicted_class = torch.argmax(output, dim=1).item()

        return self.class_labels[predicted_class]