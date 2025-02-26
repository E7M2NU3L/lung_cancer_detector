import torch
from torchvision import transforms
from PIL import Image
import io
import requests
import os 
from lung_classifier.singletons.lung_models import Covid_CNN

class CovidPredictor:
    def __init__(self, image : str, path : str) -> None:
        self.image = image
        self.path = os.path.join(path, "models", "covid_detector.pth")
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        self.model = Covid_CNN(num_classes=10).to(device)
        print("Pretrained model is loaded")

        self.output_dir = "D:/mission_2025/python_learning/django_services/lung_cancer_detector/models/covid_detector.pth"
        self.model.load_state_dict(torch.load(self.path))
        print("Model is loaded with weights")

        self.transform = transforms.Compose([
                transforms.Resize((180, 180)),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                    std=[0.229, 0.224, 0.225])
            ])
        print("Transforms are set")

         # Define class labels
        self.class_labels = ["Covid", "Normal"]
        

    # Load and transform the image
    def preprocess_image(self):
        response = requests.get(self.image)
        byteInfo = io.BytesIO(response.content)
        image = Image.open(byteInfo).convert("RGB")  # Ensure RGB format
        image = image.resize((180,180))
        image = self.transform(image)  # Apply transformations
        image = image.unsqueeze(0)  # Add batch dimension
        print("image is processed")
        return image

    def predict_image(self):
        image = self.preprocess_image()

        # Forward pass through the model
        with torch.no_grad():
            output = self.model(image)
            predicted_class = torch.argmax(output, dim=1).item()

        return self.class_labels[predicted_class]