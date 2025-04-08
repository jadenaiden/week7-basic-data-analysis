#TASK 1: Loading And Exploring The Dataset.
import pandas as pd

data = pd.read_csv('data.csv')#reading the data set.
print(data.head())#returning the first 5 rows of the dataset using the .head() function.

#exploring structure of dataset by checking data types
data = pd.read_csv('data.csv')

print(data.dtypes) #this checks and prints the data types of each column.
print(data.isna())#checks for any missing values.
print(data.fillna(0))#fills any missing values.
print(data.dropna())#drops any missing values

#TASK 2: Basic Data Analysis
