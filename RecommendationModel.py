import pickle
from flask import jsonify
import numpy as np



class RecommendationModel(object):
    """
    Model template. You can load your model parameters in __init__ from a location accessible at runtime
    """

def __init__(self):
    # Add any initialization parameters and model data that are loaded.
    print("Initializing")

    self.trainedModel = pickle.load(open('Model/' + "model_gb_ver0.pickle", 'rb'))

    # self.model_trained = joblib.load('Model/' + 'SVM_Gov_Measures_model.sav')


def predict(self, request):    
   
    y = request['data']['ndarray'][0]
    prediction = self.trainedModel.predict(y)
    return prediction


