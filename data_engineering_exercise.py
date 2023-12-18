# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:04:30 2023

@author: AIoanni1
"""

import pandas as pd

# =============================================================================
# QUESTION 1
# =============================================================================
print("Question 1")
# Sample data as stated in the question
data = {'name': ['Andy', 'Jose', 'Dieu', 'Chloe', 'Jose'],
        'continent': ['America', 'Europe', 'Asia', 'America', 'Europe'],
        'college': ['Lib Arts', 'Business', 'Engineering', 'Engineering', 'Business']}

# Create a DataFrame from sample data
STUDENTS = pd.DataFrame(data)

# Count the number of unique student names for each continent, college pair
counts = STUDENTS.groupby(['college', 'continent']).name.nunique().unstack(fill_value=0)

# Sort colleges in reverse alphabetical order
counts = counts.sort_index(ascending=False)

# # Display the result
print(counts)

for _ in range(2):
    print("")
    
# =============================================================================
# QUESTION 2
# =============================================================================
print("Question 2")
print("Part A")

# part A
# Create the DataFrame as stated in the question
data = {'month': ['jan', 'feb', 'mar', 'apr', 'may', 'jun'],
        'eggs': [47, 110, 221, 77, 132, 205],
        'salt': [12.0, 50.0, 89.0, 87.0, 0.0, 60.0],
        'spam': [17, 31, 72, 20, 52, 55]}

df = pd.DataFrame(data)

# Set 'month' column as the index
df.set_index('month', inplace=True)

# Count the number of months where 'eggs' > 100
num_months = (df.loc[['apr', 'may', 'jun'], 'eggs'] > 100).sum()

# Display the result
print("Number of months with eggs > 100:", num_months)
print("Correct Answer: A")

# part B
print("")
print("Part B")
# A) strptime, .date()
# B) strptime, .as.date()
# C) to_date, [Nothing]
# D) to_datetime, [Nothing]

import datetime

date1 = datetime.datetime.strptime('01012018', '%d%m%Y').date()

print(date1)
print(type(date1))
print("Correct Answer for Question 2 part B: Answer A")

# part C
print("")
print("Part C")
# A) iris[(iris['Species'] == 'setosa') && (iris['Petal.Width'] > 2)].sort_values('Sepal.Length', ascending = False) 
# B) iris.loc[(iris['Species'] == 'setosa') & (iris['Petal.Width'] > 2)].sort_values('Sepal.Length', ascending = False) 
# C) iris.loc[(iris['Species'] == 'setosa') & (iris['Petal.Width'] > 2)].sort_values('Sepal.Length', desc) 
# D) iris[(iris['Species'] == 'setosa') & (iris['Petal.Width'] > 2)].sort_descending('Sepal.Length') 

print("Correct Answer for Question 2 part C: Answer B")

