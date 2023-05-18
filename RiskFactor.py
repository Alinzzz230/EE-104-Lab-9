# -*- coding: utf-8 -*-
"""
Created on Wed May 17 13:28:06 2023

@author: Andrew
"""


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Read the data into a pandas DataFrame
data = pd.read_csv('hmeq.csv')

# One-hot encode the categorical columns
data = pd.get_dummies(data)

# Fill missing values with the mean of the respective column
data = data.fillna(data.mean())

# Define the feature matrix X and target y
# We assume that 'BAD' is your target column and the rest are feature columns.
# If your data is different, you should adjust this part.
X = data.drop(columns=['BAD'])
y = data['BAD']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Predict the risk groups on the test set
predictions = clf.predict_proba(X_test)

# Define thresholds for the risk groups
low_risk_threshold = 0.33
medium_risk_threshold = 0.66

# Add a new column with the risk group to the test set
X_test['risk_group'] = ['low risk' if pred[1] <= low_risk_threshold else 'medium risk' if pred[1] <= medium_risk_threshold else 'high risk' for pred in predictions]

# Save the DataFrame to a new csv file
X_test.to_csv('risk_assessment.csv', index=False)
