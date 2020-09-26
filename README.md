# Metis Project 3: Classifying Likelihood of Heroin Use

#### Amidst the Covid Pandemic, the Opioid Epidemic is still rampaging but is no longer in the eyes of the media.
#### I want to be able to provide concerned users and parents of users with an easy to use web app that will provide them expert analysis and a specific recommendation for risk of heroin use now or in the future.
#### In my analysis, I downloaded data from the UCI repo that had demographic information, behavioral scores, and a drug survey.

## 1. Identifying Key Factors

#### For every respondent: 

I regrouped some of their demographic data for simplicity in the web app as well as effectiveness in the model. I prioritized effectiveness in the model over simplicity in the app.
I considered them a “drug user” if they have used the substance in the last month. As specificity was my goal, I did not want to consider those that had used the drug well into the past as it would not be relevant for providing assistance to those who need it today.



## 2. Packages Used

pandas: Python package for data manipulation and analysis
numpy: fundamental package for scientific computing in Python
matplotlib: plotting and visualization package for Python
seaborn: Python visualization package based on matplotlib
pickle: Python module serializing and deserializing Python objects for faster object loading
requests: Python HTTP library that provides a simple API to abstract the complexities of making HTTP requests
sklearn: Python library built for machine learning; contains classification, regression, and clustering algorithms
Flask: Web app configuration tool for creating the visual online
HTML: Coding language used to create the webpage for the Flask app
CSS: Styling for HTML webpage
Javascript: Coding language, used to create an interaction in Flask app
PostgreSQL: Open Source relational database management system
SQLAlchemy: Python package for interacting with an SQL system

## 3. Credit for Data:
[UCI Data Repository] (https://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29#)


## 4. EDA and Modeling

### 4a. Putting data into AWS using postgres
Used AWS system and postgres to download data directly from the UCI website. Arranged data into a table by constructing column headers with the specific data-types of each column in mind. Used SQLAlchemy in a Jupyter Notebook to bring the data in for cleaning and modeling

### 4b. Decoding Functions
The data was encoded in 6-digit float codes and 3-digit strings for memory reasons. I wrote functions in a .py file that decoded the data according the the schema provided by the UCI repository.

### 4c. Building a base model
Once the data was decoded and dummified, I had to build a target column. I did so by combining the heroin and methadone user columns and considered no occurrence of either to be the negative case and any occurrence to be the positive case. I looked at the relationships of the behavioral scores to the target column with pair plots as they are continuous variables, and used a groupby aggregating on the mean for all the categorical variables. As the target column had a 90/10 split in neg/pos case, I went looking for relationships that strayed from this imbalance when considering which variables might make good candidates for feature selection.

Using a dummy classifier, my model scored a .05 on fbeta with beta = 3 (I determined I cared 3 times as much about false negatives as false positives) and had a ROC-AUC score of .47 Putting the data into a cross validation loop with 5 models- LogReg, KNN, Dec Tree, Ran Forest, and SVC- improved the scores but did not address the original class imbalance issue so I did not determine which model I would use at this step.

### 4d.Determining the model
In order to determine which model to use, I put both random and smote oversampling to the test inside of a cross validation loop on all 5 of my models, scoring the same fbeta and roc auc for each. This is where random oversampling LogReg separated itself with noticeably higher scores as compared to other models and I determined it to be the model I would use.

### 4e: Feature selection and model tuning
I used the insights I had gathered earlier, as well as testing out various combinations of dropping columns and regrouping them in order to increase the interpretability of the prediction as well as the score of the model. I ended up increasing my fbeta score by about 8.3% with this tuning. I also determined the optimal ratio to use as well as the best threshold for the predict proba split during this step.

### 4f: Scoring on final model
The final model scored noticeably better than the training data. I determined this to be simple luck. I pickled this model, its scaler, and its prime threshold and used them in the Flask app. I also descaled its coefficients and exponentiated them in order to determine the variables impact on the odds of Heroin Use.

## 5. Creating Visualizations

Variable Impact Percentages:
I sorted the variables by magnitude of impact- positive, negative, by category (demographic, behavioral score, drug history)- and produced plots that showed the results. Included were the 5 most negatively impacting variables, 5 most positively impacting, and the full groups of each variable category sorted by magnitude.

## 6. Flask App

The flask app was a simple, structured resource. It carried 2 links, one for each drug survey that the respondent will need to fill out in order to get their behavioral scores, and a series of yes or no questions along with boxes to input the scores of their behavioral tests. Behind the scenes, the model will take in their response as a new row of data and use the pickled fit, scaler, and threshold to make a prediction on if the respondent is at risk of heroin use.

## 7. Analysis and Future Model Plans
This model does not do that bad of a job determining the risk of heroin use. That is rather surprising because the data it is based on is not optimal. One of the first things I would do is improve the dataset. Obtaining more respondents from different countries, as well as more ethnicities, will go a long way to improving the predictive power of the model. Perfect deployment of this would have thousands of responses from multiple countries, ethnicities, ages, etc where there are both behavioral scores and drug survey responses. Being able to isolate drug use to more specific time-frames would also be beneficial.

## 6. Authors

Louis Sagan
