import streamlit as st
import pickle 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, "../assets/Sleep_health_and_lifestyle_dataset.csv")


with open('../assets/sleep_prediction_dt.pkl', 'rb') as file:
    model = pickle.load(file)
ds = pd.read_csv(csv_path)


def prediction(datavalues):
    result = model.predict(datavalues)
    return result

def info_graphics():
    st.write("### About Dataset")
    st.write("## Pie Chart")
# Aggregate the data
    data_counts = ds['Gender'].value_counts()

# Create the pie chart
    fig, ax = plt.subplots()
    ax.pie(data_counts, labels=data_counts.index, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.
    st.pyplot(fig)

    st.write("## Countplot of Occupation")
    fig, ax = plt.subplots(figsize=(15,6))
    sns.countplot(x='Occupation', data=ds, ax=ax)
    ax.set_title('Count of Occupation')
    ax.set_xlabel('Occupation')
    ax.set_ylabel('Count')
    st.pyplot(fig)

    st.write("## Scatter Plot")
#hist plot
    fig, ax = plt.subplots()
    ax.hist(ds["Age"], bins=10)
    ax.set_title('Age Distribution')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.histplot(ds["Daily Steps"], color="green", kde=True, ax=ax)
    ax.set_title('Distribution of Daily Steps')
    ax.set_xlabel('Daily Steps')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

def input_tab():
    options = {"Male":0,"Female":1}
    gender = st.radio("Gender",list(options.keys()), horizontal=True)
    bmi_options={'Overweight':0,'Normal':1,'Obese':2,'Normal Weight':3}
    bmi = st.radio("Body Mass Index(BMI)",list(bmi_options.keys()),horizontal=True)
    job =['Software Engineer', 'Doctor', 'Sales Representative', 'Teacher','Nurse', 'Engineer', 'Accountant', 'Scientist', 'Lawyer',
       'Salesperson', 'Manager']
    select_job = st.selectbox("Profession",job)
    age = st.slider("Age", 25, 60, 50)
    qos = st.slider("Quality of Sleep", 0, 10, 5)
    sl = st.slider("Stress Level", 0, 10, 5)
    sd = st.number_input("Sleep Duration:",min_value=5.0, max_value=9.0, format="%.2f")
    phy_act_level = st.number_input("Physical Activity Level:",min_value=25.0, max_value=100.0, format="%.2f")
    heart_rate = st.number_input("Heart Rate:",min_value=60.0, max_value=90.0, format="%.2f")
    steps = st.number_input("Daily Steps:",min_value=2500.0, max_value=10050.0, format="%.2f")
    high_bp = st.number_input("Systolic BP (High BP):",min_value=110.0, max_value=150.0, format="%.2f")
    low_bp = st.number_input("Diastolic BP (Low BP):",min_value=70.0, max_value=100.0, format="%.2f")
    predict=st.button('Predict')
    datavalues = [[options[gender], bmi_options[bmi],job.index(select_job), age, qos, 
        sl, sd, phy_act_level, heart_rate, steps, high_bp, low_bp]]
    if predict and datavalues:
        result = prediction(datavalues)
        st.markdown(f"""
    <style>
    .result {{
        font-size: 50px;  /* Increase font size */
        text-align: center;  /* Center align text */
    }}
    </style>
    <div class="result">
        Sleep Disorder: {result[0]}
    </div>
""", unsafe_allow_html=True)
def main():
    st.title("Sleep Prediction")
    tabs = ["Info Graphics", "Input"]
    selected_tab = st.sidebar.radio("Choose a tab", tabs)
    if selected_tab == "Info Graphics":
        info_graphics()
    elif selected_tab == "Input":
        input_tab()
if __name__ == "__main__":
    main()