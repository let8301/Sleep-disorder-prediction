import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_pie_chart(ds):
    st.write("#### Pie Chart of Gender")
    data_counts = ds['Gender'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(data_counts, labels=data_counts.index, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.
    st.pyplot(fig)

def plot_countplot(ds):
    st.write("#### Countplot of Occupation")
    fig, ax = plt.subplots(figsize=(15,6))
    sns.countplot(x='Occupation', data=ds, ax=ax)
    ax.set_title('Count of Occupation')
    ax.set_xlabel('Occupation')
    ax.set_ylabel('Count')
    st.pyplot(fig)
    st.write("The countplot provides an overview of the distribution of various occupations within the dataset. Software Engineers have the highest count, indicating a significant number of individuals in this profession. Doctors follow closely, having the second-highest count, while Sales Representatives also show a notable presence. Other occupations such as nurses, engineers, accountants, scientists, lawyers, salespeople, and managers have varying counts, with scientists, lawyers, and managers being less common as shown by the shorter bars. Overall, the countplot highlights the occupational diversity in the dataset, showing which professions are well-represented and which are less frequent.")

def hist_plot(ds):
    st.write("#### Histogram of Age Distribution")
    fig, ax = plt.subplots()
    ax.hist(ds["Age"], bins=10)
    ax.set_title('Age Distribution')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
    st.write("The histogram illustrates the age distribution within the dataset, with age intervals ranging from 25 to 60 years, each spanning 5 years. The highest frequency is observed in the 40-45 age group, with over 70 individuals, making it the most common age range. Other notable peaks are in the 30-35 and 50-55 age groups. Conversely, the 25-30 and 55-60 age ranges have very low frequencies, nearly zero, indicating these ages are less common in the dataset.")

def histogram(ds):
    st.write("#### Histogram of Daily Steps Distribution")
    fig, ax = plt.subplots()
    sns.histplot(ds["Daily Steps"], color="green", kde=True, ax=ax)
    ax.set_title('Distribution of Daily Steps')
    ax.set_xlabel('Daily Steps')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
    st.write("The histogram displays the distribution of daily steps, with each bar representing specific step count ranges. The most common step count is around 8000 steps.")

def scatter_plot(ds):
    st.write("#### Scatterplot")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Age', y='Sleep Duration', hue='BMI Category', data=ds)
    plt.title('Sleep Duration vs. Age')
    plt.xlabel('Age')
    plt.ylabel('Hours of Sleep')
    plt.show()
    st.pyplot()
    st.write("The scatterplot displays individual data points, with the x-axis representing age and the y-axis showing hours of sleep. Points are color-coded by BMI category. There is no clear linear relationship between age and sleep duration, with data points scattered across the plot. This indicates that sleep duration does not follow a straightforward trend related to age or BMI alone. ")

def barplot(ds):
    st.write("#### Sleep Disorders by Occupation")
    occupation_counts = ds['Occupation'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=occupation_counts.index, y=occupation_counts.values)
    plt.xticks(rotation=45)
    plt.xlabel('Occupation')
    plt.ylabel('Frequency of Sleep Disorders')
    plt.title('Sleep Disorders by Occupation')
    st.pyplot()
    st.write("The bar plot shows the frequency of sleep disorders across various professions. Nurses have the highest frequency of sleep disorders, followed closely by doctors. Engineers, lawyers, teacher, accountants and salesperson experience moderate levels of sleep disorders, while software engineers, scientists and sales representatives have lower frequencies. Managers have the lowest frequency of sleep disorders among the listed occupations.")

def countplot_bmi(ds):
    st.write("#### Distribution of Sleep Disorders by BMI Category")
    plt.figure(figsize=(10, 6))
    sns.countplot(x='BMI Category', hue='Sleep Disorder', data=ds)
    plt.xlabel('BMI Category')
    plt.ylabel('Count of Sleep Disorders')
    plt.title('Distribution of Sleep Disorders by BMI Category')
    plt.xticks(rotation=45)
    st.pyplot()

def boxplot(ds):
    st.write("#### Sleep Duration by Gender")
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Gender', y='Sleep Duration', palette='mako', data=ds)
    plt.title('Sleep Duration by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Sleep Duration')
    st.pyplot()

def sleep_pie_chart(ds):
    st.write("#### Pie Chart of Sleep Disorder")
    data_counts = ds['Sleep Disorder'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(data_counts, labels=data_counts.index, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.
    st.pyplot(fig)