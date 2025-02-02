# Cleaner_Unkle: Waste Classification System

## Overview
**Cleaner_Unkle** is a deep learning-based image classification system designed to categorize waste into 8 different types. The goal of this project is to facilitate waste management and recycling by automating the classification of waste using computer vision techniques.

## Waste Categories
The system classifies waste into the following categories:
- **0**: E-waste
- **1**: Food waste
- **2**: Leaf waste
- **3**: Metal cans
- **4**: Paper waste
- **5**: Plastic bags
- **6**: Plastic bottles
- **7**: Wood waste

## Features
- Image preprocessing for improved classification accuracy.
- Deep learning model for waste classification.
- Flask web application for user-friendly interaction.
- Training and testing scripts for model development and evaluation.

## Folder Structure
```
Cleaner_Unkle/
│-- app.py                # Flask web application for predictions
│-- waste.ipynb           # Jupyter Notebook for model training
│-- templates/            # HTML templates for Flask web interface
│-- requirements.txt      # Dependencies for the project
│-- Model_1.h5            # Model in H5 format
│-- Model_2.keras         # Model in Keras format
│-- README.md             # Project documentation
```

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Flask
- TensorFlow/Keras
- NumPy, Pandas, Matplotlib

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/Cleaner_Unkle.git
   cd Cleaner_Unkle
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Model Training
A pre-trained model is provided in the repository. However, if you wish to train it yourself:
1. Open `train.ipynb` in Jupyter Notebook.
2. Follow the steps to preprocess data and train the model.
3. Save the trained model in the `model/` directory for testing and Flask integration.


## Running the Application
1. Start the Flask web application:
   ```sh
   python app.py
   ```
2. Open a browser and navigate to `http://127.0.0.1:5000/`.
3. Upload an image to get predictions.


## License
This project is licensed under the MIT License.

