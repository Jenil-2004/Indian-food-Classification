Indian Food Classification App
This repository contains an Indian Food Classification app developed using Streamlit for the frontend and a Keras-based machine learning model utilizing transfer learning. The model is trained to classify 20 different Indian food items.

Table of Contents
Introduction
Features
Installation
Usage
Model Details
Class Labels
Contributing
License
Introduction
This app classifies images of Indian food into one of 20 categories using a deep learning model built with Keras and transfer learning. The app's user interface is built with Streamlit, providing an easy-to-use platform for uploading images and viewing classification results.

Features
Image Upload: Upload an image of Indian food, and the app will predict the food category.
Real-time Predictions: The app displays the predicted food category along with the corresponding confidence score.
Streamlit Interface: A user-friendly interface for interacting with the model.
Installation
Prerequisites
Python 3.7+
pip (Python package installer)
Steps
Clone this repository:

bash
Copy code
git clone https://github.com/yourusername/indian-food-classification.git
cd indian-food-classification
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Usage
After starting the app, you'll be directed to the Streamlit interface.
Upload an image of Indian food.
The app will display the predicted food category and the confidence score.
Model Details
The model is built using transfer learning with a pre-trained MobileNetV2 architecture. A custom dense layer is added to adapt the model for classifying 20 different types of Indian food.

Model Architecture: MobileNetV2 + Custom Dense Layer
Input Size: 180x180 pixels
Number of Classes: 20
Class Labels
The model can classify the following 20 types of Indian food:

burger
butter_naan
chai
chapati
chole_bhature
dal_makhani
dhokla
fried_rice
idli
jalebi
kaathi_rolls
kadai_paneer
kulfi
masala_dosa
momos
paani_puri
pakode
pav_bhaji
pizza
samosa
Contributing
Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to customize this README to better suit your project!
