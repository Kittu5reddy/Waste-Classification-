import torch
from torchvision import models, transforms
from PIL import Image

# Load model function
def load_model():
    model = models.vgg16(pretrained=False)
    model.classifier[6] = torch.nn.Linear(4096, 4)  # 4 output classes
    try:
        model.load_state_dict(torch.load('./model/40.pth', map_location=torch.device('cpu')))
        model.eval()  # Set model to evaluation mode
        return model
    except FileNotFoundError:
        print("Error: Model file 'Modek' not found.")
        return None

# Image preprocessing function
def preprocess_image(image):
    transform_test = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    image = transform_test(image).unsqueeze(0)  # Add batch dimension
    return image

# Function to predict the class
def predict_image_class(image, model):
    image_tensor = preprocess_image(image)
    with torch.no_grad():
        outputs = model(image_tensor)
        _, preds = torch.max(outputs, 1)

    # Map index to class name
    idx_to_class = {0: 'Biodegradable', 1: 'Non-Biodegradable', 2: 'Trash', 3: 'Hazardous'}
    return idx_to_class.get(preds.item(), "Unknown")