import streamlit as st
import pickle
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array\

# Load your trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define class names (ensure these match the order used during training)
class_names = ['burger', 'butter_naan', 'chai', 'chapati', 'chole_bhature', 'dal_makhani',
               'dhokla', 'fried_rice', 'idli', 'jalebi', 'kaathi_rolls', 'kadai_paneer', 
               'kulfi', 'masala_dosa', 'momos', 'paani_puri', 'pakode', 'pav_bhaji', 
               'pizza', 'samosa']  # replace with actual class names

def classify_image(image, model):
    image = image.resize((224, 224))  # resize to match model input size
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)  # add batch dimension
    image = image / 256.0  # normalize

    # Debugging: Print shape and first few values of the preprocessed image
    # st.write(f"Processed Image Shape: {image.shape}")
    # st.write(f"Processed Image Sample (first 5 values): {image.flatten()[:5]}")

    # Get predictions and print them for debugging
    predictions = model.predict(image)
    st.write(f"Prediction Probabilities: {predictions}")

    predicted_class = np.argmax(predictions)
    return class_names[predicted_class]

# Streamlit UI
st.title("Indian Food Classification")
st.write("Upload an image of Indian food, and the model will classify it!")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button("Classify"):
        with st.spinner('Classifying...'):
            label = classify_image(image, model)
            st.success(f'This looks like: {label}')
