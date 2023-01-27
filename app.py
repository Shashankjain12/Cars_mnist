from flask import Flask, jsonify, make_response
from flask import request
import json

from functions import MNIST
app = Flask(__name__)
mnist_model = None

@app.route("/ping")
def ping():
    return "Pinged the server", 200


@app.route('/predict_number', methods=['POST'])
def predict_mnist():
    """
    This function first retrieves the image_path from the JSON object
    in the request body using request.json.get("image_path").
    Then, it checks if the global variable mnist_model is defined or not, 
    if not, it instantiates a new MNIST class object.
    The function then uses the predict_image() method of the mnist_model object 
    to predict the number in the image, passing in the image_path as an argument.
    Then, it creates a dictionary data with two key-value pairs, 
    one is "predictions" which is the predicted number and the other one is "data_str" 
    which is a string that describes the prediction.
    
    """
    image_path = request.json.get("image_path")
    global mnist_model
    if not mnist_model:
        mnist_model = MNIST()
    image_preds = mnist_model.predict_image(image_path)
    data = {
        "predictions": str(image_preds[0]),
        "data_str": f"MNIST Model Predicts --> {image_preds[0]} <-- for the image."
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")