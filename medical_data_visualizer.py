Author- Shafin Khan
Student@UBC

Q-
In this project, you will visualize and make calculations from medical examination data using matplotlib, seaborn, and pandas. The dataset values were collected during medical examinations.

Data description
The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. You will use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

File name: medical_examination.csv

Feature	Variable Type	Variable	Value Type
Age	Objective Feature	age	int (days)
Height	Objective Feature	height	int (cm)
Weight	Objective Feature	weight	float (kg)
Gender	Objective Feature	gender	categorical code
Systolic blood pressure	Examination Feature	ap_hi	int
Diastolic blood pressure	Examination Feature	ap_lo	int
Cholesterol	Examination Feature	cholesterol	1: normal, 2: above normal, 3: well above normal
Glucose	Examination Feature	gluc	1: normal, 2: above normal, 3: well above normal
Smoking	Subjective Feature	smoke	binary
Alcohol intake	Subjective Feature	alco	binary
Physical activity	Subjective Feature	active	binary
Presence or absence of cardiovascular disease	Target Variable	cardio	binary
Tasks
Create a chart similar to examples/Figure_1.png, where we show the counts of good and bad outcomes for the cholesterol, gluc, alco, active, and smoke variables for patients with cardio=1 and cardio=0 in different panels.

Use the data to complete the following tasks in medical_data_visualizer.py:

Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
Normalize the data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, make the value 0. If the value is more than 1, make the value 1.
Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot(). The dataset should be split by 'Cardio' so there is one chart for each cardio value. The chart should look like examples/Figure_1.png.
Clean the data. Filter out the following patient segments that represent incorrect data:
diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
height is more than the 97.5th percentile
weight is less than the 2.5th percentile
weight is more than the 97.5th percentile
Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's heatmap(). Mask the upper triangle. The chart should look like examples/Figure_2.png.

Ans-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('https://raw.githubusercontent.com/freeCodeCamp/boilerplate-medical-data-visualizer/main/medical_examination.csv')
df.head()

overweight = (df['weight']/((df['height']/100)**2)>25).astype(int) # if you do not use astype than they will shpw true and false
df['overweight'] = overweight

df['gluc'] = (df['gluc'] > 1).astype(int) 
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df

df_cat= df.melt(id_vars=['cardio'],value_vars=sorted(['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']))

df_cat # the function melt is used to convert data from wide to long. wide data is the one where data in the first column does not repeat itself. id_vars is used used to locate the column which you want to consider as the reference column. value_vars is used to consider other columns.

 g = sns.catplot(data=df_cat, kind='count', hue='value',x='variable',col="cardio") # sns.catplot() is used to plot graph 'data' parameter shows from where to take data. kind='count' shows what should be on the y variable and is the total number of each set. x shows the sorted valuse that we have worked on previously.'col'function different
 
 df.drop(df.index[(df['ap_lo'] >= df['ap_hi']) & (df['height'] <= df['height'].quantile(0.025)) & (df['height'] >= df['height'].quantile(0.975)) & (df['weight'] <= df['weight'].quantile(0.025)) & (df['weight'] >= df['weight'].quantile(0.975))],inplace=True)
 
corr_matrix=df.corr()
corr_matrix

mask=np.triu(corr_matrix) # the job of a correlation matrix is just the one we did if we had two roll 2 dice at a time

ax = sns.heatmap(
        corr_matrix, annot=True, fmt='.1f', linewidths=1, mask=mask, 
        vmax=.8, center=0.09, square=True, cbar_kws={'shrink':0.5}) 
