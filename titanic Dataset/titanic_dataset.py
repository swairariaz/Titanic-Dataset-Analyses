# first we have to import all the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#load the dataset file
df = pd.read_csv("train.csv")

#Ensure we are working with the actual dataframe
df = df.copy()

#Disply the first 5 rows of the dataset
print("\nDisplay first 5 rows of the dataset: ")
print(df.head())

#Display the last five rows of the Dataset
print("\nDisplay last 5 rows of Dataset: ")
print(df.tail())

#Disply missing values of the Dataset
print("\nMissing values of Dataset: ")
print(df.isnull().sum())

#first fill the 'Age' missing values with the median age
df['Age'] = df['Age'].fillna(df['Age'].median())

#Second fill the 'Embarked' missing values with the most common values
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

#Drop 'Cabin' column because of too many missing values
df.drop(columns = ['Cabin'], inplace = True)

#Now check, if any missing value still exist
print("\nShow, if any missing vallue exist: ")
print(df.isnull().sum())
print("There are no more missing values exist")

#Display basic statistics of the Dataset
print("\nDisplay basic statistics of Dataset: ")
print(df.describe())

#Survival Count
#plt.style.use("dark_background")
#plt.figure(figsize = (8, 6))
#custom_colors = ["#FF4C4C", "#5CD85C"]    #i choose Red for No, and Green for Yes
#sns.countplot(x = 'Survived', data = df, hue = 'Survived', palette = custom_colors, legend = False)
#plt.grid(axis = 'y', linestyle = '--', alpha = 0.5, color = 'gray')  #optional (grid for better readability
#plt.title("Survival plot (0 = NO & 1 = YES)", fontsize = 14, fontweight = 'bold', color = "white")
#plt.xlabel("Survival status", fontsize = 12, fontweight = 'bold')
#plt.ylabel("Number of Passengers", fontsize = 12, fontweight = 'bold')
#plt.show()


#Survival rate by gender
#plt.figure(figsize = (8, 6))
#plt.gcf().set_facecolor("yellow")
#plt.gca().set_facecolor("yellow")
#custom_colors = ["#87CEEB", "#FF69B4"]
#sns.countplot(x = 'Survived', data = df, hue = 'Sex', palette = custom_colors)
#plt.grid(axis='y', linestyle = '--', alpha = 0.5, color = 'gray')
#plt.title("Survival rate by Gender (0 = NO, 1 = YES) ", fontsize = 14, fontweight = 'bold', color = "black")
#plt.xlabel("Survival count", fontsize =12, fontweight = 'bold')
#plt.ylabel("Number of passenger", fontsize =12, fontweight = 'bold')
#plt.show()

#Age distribution of Passengers
#plt.style.use("dark_background")
#plt.figure(figsize = (8, 6))
#sns.histplot(df['Age'], bins = 20, kde = True, color = "red")
#plt.title("Age distribution of Passengers", fontsize=14, fontweight='bold')
#plt.xlabel("Age", fontsize=12, fontweight='bold')
#plt.xlabel("Age", fontsize=12, fontweight='bold')
#plt.ylabel("Number of Passengers", fontsize=12, fontweight='bold')
#plt.show()

#Passenger Class vs. Survival
#plt.style.use("dark_background")
#plt.figure(figsize = (8, 6))
#custom_colors = ["#C0392B", "#2E8B57"]
#sns.countplot(x = 'Pclass', hue = 'Survived', data = df, palette = custom_colors)
#plt.title("Survival rate by Passenger Class", fontsize = 14, fontweight = 'bold')
#plt.xlabel("Pclass", fontsize = 12, fontweight = 'bold')
#plt.xlabel("Survival Count", fontsize = 12, fontweight = 'bold')
#plt.show()

#Fare vs. Survival
#plt.style.use("dark_background")
#plt.figure(figsize = (8, 6))
#sns.boxplot(x = 'Survived', y = 'Fare', data = df, hue = 'Survived', palette = 'coolwarm')
#plt.title("Fared Paid vs Survival", fontsize = 14, fontweight ='bold')
#plt.show()

#Age vs Fare Scatter plot
#plt.style.use("dark_background")
#plt.figure(figsize = (8, 6))
#sns.scatterplot(x = 'Age', y = 'Fare', hue = 'Survived', data = df,  palette = 'coolwarm')
#plt.title("Age vs Fare (Survival highlighted", fontsize = 14, fontweight = 'bold')
#plt.xlabel("Age", fontsize = 14, fontweight = 'bold')
#plt.ylabel("Fare", fontsize = 14, fontweight = 'bold')
#plt.show()









