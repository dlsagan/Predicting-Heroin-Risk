import pickle
import pandas as pd
import numpy as np
from predict_helper import predict_thresh_prime

# read in the model
my_model = pickle.load(open("model_for_flask.pickle","rb"))
my_scaler = pickle.load(open("scaler_for_flask_model.pkl", "rb"))
thresh_prime = pickle.load(open("thresh_prime_for_flask_model.pkl", "rb"))

# create a function to take in user-entered amounts and apply the model
def user_or_not(amounts_float, model=my_model):

    # scale new data
    my_scaler.transform(amounts_float)

    # inputs into the model
    input_df = amounts_float
    
    # make a prediction
    prediction = predict_thresh_prime(my_model.predict_proba(input_df)[:, 1], thresh_prime)

    # return a message
    message_array = ["You are not likely at risk, but best to still be careful with drugs.",
                     "You are likely at risk for heroin addiction, please seek out addiction specialists."]

    return message_array[prediction]
