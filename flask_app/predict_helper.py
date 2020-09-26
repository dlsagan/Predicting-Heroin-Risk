import pandas as pd
from sklearn.linear_model import LogisticRegression

def predict_thresh_prime(predict_proba_value, p_value):
    if predict_proba_value > p_value:
        return 1
    else:
        return 0
