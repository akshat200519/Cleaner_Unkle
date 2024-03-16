from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Initialize Flask application
app = Flask(__name__)

# Load the saved model
model = load_model('model_2.keras')

# Define route for serving index.html
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for image uploads and predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the uploaded image file from the request
    file = request.files['image']
    
    # Load the image
    img = Image.open(file.stream)
    
    # Preprocess the image (resize, normalize, etc.)
    img = img.resize((235, 200))  # Resize the image to match the model input shape
    
    # Convert image to numpy array
    img_array = np.array(img) / 255.0  # Normalize the pixel values
    
    # Reshape the image array to match model input shape
    img_array = np.expand_dims(img_array, axis=0)
    
    # Make prediction
    prediction = model.predict(img_array)
    
    # Decode prediction (if necessary)
    predicted_class = int(np.argmax(prediction))  # Convert numpy.int64 to Python int

    # Reset the file pointer to read the uploaded image from the beginning
    file.seek(0)
    
    # Return the predicted class as JSON response
    return jsonify({'predicted_class': predicted_class})



# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
