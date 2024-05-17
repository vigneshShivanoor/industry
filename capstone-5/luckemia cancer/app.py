from flask import Flask, render_template, request
import numpy as np
from PIL import Image
from load import init

app = Flask(__name__)
cnn_model, g = init()

# Preprocessing function
def preprocess_input_image(image):
    img = Image.open(image)
    img = img.resize((256, 196))  # Resize image to match expected input shape
    img_array = np.array(img)
    img_array = img_array / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Output function
def get_predicted_label(prob):
    label_mapping = {
        1: "benign",
        2: "Malignant-Early",
        3: "Malignant-Pre",
        4: "Malignant-Pro"
    }
    predicted_label_value = np.argmax(prob, axis=1)[0]  # Get the predicted label value (0-indexed)
    return label_mapping.get(predicted_label_value, "None")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predicting', methods=['POST'])
def predicting():
    try:
        file = request.files['file']
        input_image = preprocess_input_image(file)
        prob = cnn_model.predict(input_image)
        predicted_label = get_predicted_label(prob)
        return render_template('results.html', predicted_label=predicted_label, error=None)
    except Exception as e:
        return render_template('results.html', predicted_label=None, error=str(e))

if __name__ == '__main__':
    app.run(debug=True, port=8000)
