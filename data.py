#TASK 1: Loading And Exploring The Dataset.
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')#reading the data set.
print(data.head())#returning the first 5 rows of the dataset using the .head() function.

#exploring structure of dataset by checking data types
data = pd.read_csv('data.csv')

print(data.dtypes) #this checks and prints the data types of each column.
print(data.isna())#checks for any missing values.
print(data.fillna(0))#fills any missing values with zero.
print(data.dropna())#drops any missing values.

#TASK 2: Basic Data Analysis
data = pd.read_csv('data.csv')
describe = data.describe()#output statistics like count, mean,standard deviation, min, 25% (first quartile), 50% (median), 75% (third quartile), and max.
print(describe)

data = pd.read_csv('data.csv')
grouped_data = data.groupby('Duration')[['Pulse','Maxpulse','Calories']].mean()#calculating groupings on categorical data and the mean of each numerical column
print(grouped_data)

#TASK 3: DATA VISUALIZATION
#Line chart showing duration vs pulse
plt.plot(data['Duration'],data['Pulse'])
plt.xlabel('Duaration')
plt.ylabel('Pulse')
plt.title(' Duration vs Pulse')
plt.show()

#Bar chart showing comparison of a numerical value(Duration) against Pulse, Maxpulse and Calories
data.groupby('Duration')['Pulse'].mean().plot(kind = 'bar')
plt.xlabel('Pulse')
plt.ylabel('Duration(s)')
plt.title('Pulse against Duration')
plt.show()

#Histogram of a numerical column to understand its distribution
#Distribution for Pulse
data['Pulse'].plot(kind = 'hist',bins = 10)
plt.xlabel('Pulse')
plt.ylabel('Duration')
plt.title('Pulse distribution')
plt.show()

#Scatter plot to visualize the relationship between two numerical columns
#Relationship between duration and Pulse
data.plot(kind = 'scatter', x = 'Duration', y = 'Pulse')
plt.title('Pusle vs Duration')
plt.show()