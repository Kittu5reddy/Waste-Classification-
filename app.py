import streamlit as st
from PIL import Image
from main import load_model, predict_image_class  # Import from model.py

st.set_page_config(page_title="Waste Classification CNN Convolutional Neural Network", page_icon="♻️")

# Cache the model loading function
@st.cache_resource
def get_model():
    return load_model()

# Streamlit App
st.title("♻️ Waste Classification CNN Convolutional Neural Network")

# Introduction
st.header("Introduction")
st.write("""
This project utilizes a Convolutional Neural Network (CNN) to classify waste into four categories: **Biodegradable, Non-Biodegradable, Trash, or Hazardous**. The model is designed to assist in waste management by automating the classification process, making it easier to sort and recycle waste effectively.


### Resource:
- **Data-Set**:"kaggle datasets download -d alistairking/recyclable-and-household-waste-classification".

### Key Features:
- **Model Loading**: The model is loaded using a cached function to improve performance.
- **Image Upload**: Users can upload images of waste through the Streamlit interface.
- **Prediction**: The uploaded image is processed and classified into one of the four categories using the trained CNN model.
- **User Feedback**: The app provides visual feedback by displaying the uploaded image and the predicted class.

""")

st.write("Upload an image of waste, and the model will classify it into one of four categories: **Biodegradable, Non-Biodegradable, Trash, or Hazardous.**")

uploaded_image = st.file_uploader("📤 Upload an image", type=['jpg', 'jpeg', 'png'])

if uploaded_image:
    try:
        # Display the uploaded image
        image = Image.open(uploaded_image).convert('RGB')
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Load model
        model = get_model()
        if model is not None:
            # Predict the class
            predicted_class = predict_image_class(image, model)
            st.balloons()
            st.success(f"✅ **Predicted Class:** *{predicted_class}*")
        else:
            st.warning("⚠️ Model not loaded. Please check the file path.")

    except Exception as e:
        st.error(f"❌ Error processing the file: {e}")
