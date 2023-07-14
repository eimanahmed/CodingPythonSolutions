#Importing modules and packages for problem
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import numpy as np

#Reading data from Data.world 
nba_data = pd.read_csv('nba_logreg.csv')

#Data cleaning and pre-processing
nba_data = nba_data.dropna()
target = nba_data["TARGET_5Yrs"].copy()
data = nba_data.drop('TARGET_5Yrs', axis=1)
data = nba_data.drop('Name', axis=1)

#Splitting the dataset into 80% and 20% split (80% for training)
X_train, X_test, y_train, y_test = train_test_split(data, target , test_size=0.20, random_state=0)

#Selecting a model and seeing how our data fits the model (80%)
model = LogisticRegression(solver='sag')
model.fit(X_train, y_train)

#Using the model to continue predicting future values on test set (20%)
y_pred = model.predict(X_test)

#Checking the accuracy of our model (very good - fake dataset)
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)

#How do different factors influence the information we are predicting
coefficients = pd.DataFrame({"Feature":X_train.columns,"Coefficients":np.transpose(model.coef_[0])})
print(coefficients)



