from flask import Flask, request, render_template
from make_prediction import user_or_not
import numpy as np

# create a flask object
app = Flask(__name__)

# creates an association between the / page and the entry_page function (defaults to GET)
@app.route('/')
def entry_page():
    return render_template('index.html')

# creates an association between the /predict_user_or_not page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/predict_user_or_not/', methods=['GET', 'POST'])
def render_message():

    # user-entered behavioral scores
    scores = ['n_score', 'e_score', 'o_score', 'a_score', 'c_score', 's_score', \
                'alcohol', 'amphet', 'amyl', 'benzos', 'cannabis', 'coke', 'ecstacy', \
                'ketamine', 'inhalants', 'acid', 'mushrooms', 'nicotine', 'age_18-24', \
                'age_25-34', 'age_35+', 'sex_M', 'some_college', 'country_UK', \
                'country_USA', 'no_college', 'finished_college', 'higher_ed']

    # error messages to ensure correct units of measure
    messages = ["Neuroticism score must be between 10 and 90, double check your results.",
                "Extraversion score must be between 10 and 90, double check your results.",
                "Openness to Experience score must be between 10 and 90, double check your results.",
                "Agreeableness score must be between 10 and 90, double check your results.",
                "Conscientiousness score must be between 10 and 90, double check your results.",
                "Sensation Seeking score must be between 0 and 40, double check your results.",
                "Please respond with yes or no only based on your use in the last month.",
                "Please respond with yes or no only based on your use in the last month.",
                "Please respond with yes or no only based on your use in the last month.",
                "Please respond with yes or no only based on your use in the last month.",
                "Please respond with yes or no only based on your use in the last month.",
                "Please respond with yes or no only based on your use in the last month.",
                "Please respond with yes or no only based on your use in the last month.",
                "Please respond with yes or no only based on your use in the last month.",
                "Please respond with yes or no only based on your use in the last month.",
                "Please respond with yes or no only based on your use in the last month.",
                "Please respond with yes or no only based on your use in the last month.",
                "Please respond with yes or no only based on your use in the last month.",
                "Please respond with yes or no only based on your age.",
                "Please respond with yes or no only based on your age.",
                "Please respond with yes or no only based on your age.",
                "Please respond with yes or no only based on your education experience.",
                "Please respond with yes or no only based on your country of residence.",
                "Please respond with yes or no only based on your country of residence.",
                "Please respond with yes or no only based on your education experience.",
                "Please respond with yes or no only based on your education experience.",
                "Please respond with yes or no only based on your education experience."]


    # hold all amounts as floats
    amounts = []

    # takes user input and ensures it can be turned into a floats
    for i, score in enumerate(scores):
        user_input = request.form[score]
        if user_input == "Yes" or user_input ==  "yes":
            user_input = 1
        if user_input == "No" or user_input == "no":
            user_input = 0
        try:
            float_score = float(user_input)
        except:
            return render_template('index.html', message=messages[i])
        amounts.append(float_score)

    # show user final message
    final_message = user_or_not(np.array(amounts).reshape(1, -1))
    return render_template('index.html', message=final_message)

if __name__ == '__main__':
    app.run(debug=True)
