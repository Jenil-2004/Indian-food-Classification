# Indian Food Classification App

This repository contains an Indian Food Classification app developed using Streamlit for the frontend and a Keras-based machine learning model utilizing transfer learning. The model is trained to classify 20 different Indian food items.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Class Labels](#class-labels)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This app classifies images of Indian food into one of 20 categories using a deep learning model built with Keras and transfer learning. The app's user interface is built with Streamlit, providing an easy-to-use platform for uploading images and viewing classification results.

## Features

- **Image Upload**: Upload an image of Indian food, and the app will predict the food category.
- **Real-time Predictions**: The app displays the predicted food category along with the corresponding confidence score.
- **Streamlit Interface**: A user-friendly interface for interacting with the model.

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Steps

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/indian-food-classification.git
    cd indian-food-classification
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Usage

- After starting the app, you'll be directed to the Streamlit interface.
- Upload an image of Indian food.
- The app will display the predicted food category and the confidence score.

## Model Details

The model is built using transfer learning with a pre-trained MobileNetV2 architecture. A custom dense layer is added to adapt the model for classifying 20 different types of Indian food.

- **Model Architecture**: MobileNetV2 + Custom Dense Layer
- **Input Size**: 224x224 pixels
- **Number of Classes**: 20

## Class Labels

The model can classify the following 20 types of Indian food:

- burger
- butter_naan
- chai
- chapati
- chole_bhature
- dal_makhani
- dhokla
- fried_rice
- idli
- jalebi
- kaathi_rolls
- kadai_paneer
- kulfi
- masala_dosa
- momos
- paani_puri
- pakode
- pav_bhaji
- pizza
- samosa

## Contributing

Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or submit a pull request.
