# -*- coding: utf-8 -*-
"""
Created on Tue May 16 14:11:46 2023

@author: Andrew
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the data into a pandas DataFrame
data = pd.read_csv('risk_assessment.csv')

# Count the number of instances in each risk group
risk_counts = data['risk_group'].value_counts()

# Plot a bar chart
plt.figure(figsize=(10, 6))
plt.bar(risk_counts.index, risk_counts.values, color=['green', 'orange', 'red'])
plt.xlabel('Risk Group')
plt.ylabel('Count')
plt.title('Risk Group Distribution')
plt.show()
