from PIL import Image
import torch
from torchvision import transforms
import joblib
import pandas as pd
import joblib

class LungCancerPredictor:
    def __init__(self, data : dict) -> None:
        self.data = data

        self.rf = joblib.load("../models/random_forest.pkl")
        self.gb = joblib.load("../models/gradient_boosting.pkl")
        self.ada = joblib.load("../models/adaboost.pkl")

        self.sample_data = pd.DataFrame(self.data)

        # Normalize input using the saved scaler
        self.scaler = joblib.load("../models/scaler.pkl")
        self.sample_scaled = self.scaler.transform(self.sample_data)

        self.model = torch.load("../models/lung_cancer_detector.pth")

        # Convert to PyTorch tensor
        self.sample_tensor = torch.tensor(self.sample_scaled, dtype=torch.float32)

    def predict(self) -> str:
        # Predict using Neural Network
        with torch.no_grad():
            nn_prediction = self.model(self.sample_tensor).item()
            nn_prediction = 1 if nn_prediction > 0.5 else 0  # Convert probability to class

        # Predict using ML Models
        rf_pred = self.rf.predict(self.sample_scaled)[0]
        gb_pred = self.gb.predict(self.sample_scaled)[0]
        ada_pred = self.ada.predict(self.sample_scaled)[0]

        # Ensemble (average voting)
        ensemble_pred = round((rf_pred + gb_pred + ada_pred + nn_prediction) / 4)
        return ensemble_pred

class LungCancerCTPredictor:
    def __init__(self, image : str) -> None:
        self.image = image

        self.transform = transforms.Compose([
            transforms.Resize((64, 64)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                std=[0.229, 0.224, 0.225])
        ])

         # Define class labels
        self.class_labels = ["Benign", "Malignant", "Normal"]
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