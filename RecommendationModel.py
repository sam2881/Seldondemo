from flask import jsonify, Flask
import numpy as np
import pickle



class RecommendationModel(object):
    """
    Model template. You can load your model parameters in __init__ from a location accessible at runtime
    """

    def __init__(self):
        # Add any initialization parameters and model data that are loaded.
        print("Initializing")

        self.trainedModel = pickle.load(open('Model/' + "model_gb_ver0.pickle", 'rb'))

        # self.model_trained = joblib.load('Model/' + 'SVM_Gov_Measures_model.sav')


    def predict_raw(self,X): 
        X = np.array(X, dtype=object)
        y = X['data']['ndarray'][0]
        prediction = self.trainedModel.predict(y)
        return prediction
