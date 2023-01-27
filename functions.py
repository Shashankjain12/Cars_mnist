import keras
import numpy as np
from keras.datasets import mnist
from PIL import Image
import numpy as np


class MNIST:
    def __init__(self):
        '''
        This is the constructor method of the class which gets called when an object of the class is created.
        It loads a pre-trained model from the file ./model/mnist_model.h5 using the 
        keras.models.load_model() function and assigns it to the object variable self.model
        '''
        self.model = keras.models.load_model("./model/mnist_model.h5")

    def transform_image(self, image_path:str):
        '''
        This method takes a single argument image_path, which is a string representing the path of an image. 
        It opens the image using the Image.open() function from the Python Imaging Library (PIL) and 
        converts it to an array using np.asarray().
        It then normalizes the array by dividing each element by 255 and reshapes the array to have dimensions 
        (-1, 28, 28, 1) using the reshape() method from numpy.
        
        Args:
            image_path :- Image path where the MNIST model is used to predict the image
        Returns:
            Transformed image according to the trained dataset
        '''
        img = Image.open(image_path)
        img_arr = np.asarray(img).astype("float32") / 255
        img_mod = img_arr.reshape(-1, 28, 28, 1)
        return img_mod

    def predict_image(self, image_path:str):
        '''
        This method takes a single argument image_path, which is a string representing the path of an image.
        It calls the transform_image() method to get the processed image array, 
        then uses the predict() method of the self.model object to predict the number 
        in the image and assigns the result to a variable preds. 
        Finally, it returns the index of the highest probability class using np.argmax(preds, axis=1)
        Args:-
            Image Path - Image to be tranformed and predicted
        Returns:
            Pred_class - predicted class as per the model
        '''
        img_mod = self.transform_image(image_path=image_path)
        preds = self.model.predict(img_mod)
        pred_classes = np.argmax(preds, axis=1)
        return pred_classes
    