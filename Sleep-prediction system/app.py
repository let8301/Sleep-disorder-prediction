import streamlit as st
import pickle 
import numpy as np
import pandas as pd
import os
import seaborn as sns
from plots import plot_pie_chart, plot_countplot, hist_plot, histogram, scatter_plot,barplot, countplot_bmi,boxplot,sleep_pie_chart

st.set_option('deprecation.showPyplotGlobalUse', False)

current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, "../assets/sleep_disorder.csv")


with open('../assets/sleep_prediction_dt.pkl', 'rb') as file:
    model = pickle.load(file)
ds = pd.read_csv(csv_path)
disorder_mapping = {
    0: {
        "name": "No Disorder",
        "description": "You do not have any sleep disorder.",
        "causes": "N/A",
        "tips": "Maintain a healthy lifestyle to continue having good sleep."
    },
    1: {
        "name": "Sleep Apnea",
        "description": "Sleep apnea is a serious sleep disorder where breathing repeatedly stops and starts during sleep. This interruption in breathing can lead to poor sleep quality and excessive daytime sleepiness, affecting overall health and daily functioning.",
        "causes": "Sleep apnea can be caused by factors such as obesity, large neck circumference, a narrowed airway, older age, family history, alcohol or sedative use, smoking, and nasal congestion. Also men are statistically more likely to develop sleep apnea compared to women.",
        "tips": "To overcome sleep apnea, it's important to maintain a healthy weight, exercise regularly, and avoid alcohol and smoking. Sleeping on your side, using a CPAP machine or an oral appliance, and treating nasal congestion can also help. In severe cases, surgery might be necessary. Consulting a sleep specialist is recommended for proper diagnosis and management."
    },
    2: {
        "name": "Insomnia",
        "description": "Insomnia is a common sleep disorder characterized by difficulty falling asleep, staying asleep, or both, despite having the opportunity to sleep. This condition can lead to daytime fatigue, low energy, mood disturbances, and a decreased performance in work or school.",
        "causes": "Insomnia can stem from various sources such as stress, anxiety, depression, poor sleep habits, medical conditions, medications, and lifestyle choices including the consumption of caffeine, nicotine, and alcohol. Major life changes or events can also disrupt sleep patterns.",
        "tips": "To combat insomnia, maintain a regular sleep schedule and create a restful environment. Limit screen time before bed and avoid large meals, caffeine, and alcohol in the evening. Engage in regular physical activity and practice relaxation techniques such as yoga or meditation. Establish a calming bedtime routine, limit naps, and manage stress through mindfulness or therapy. If insomnia continues, consult a healthcare provider or sleep specialist."
    }
}


def prediction(datavalues):
    result = model.predict(datavalues)
    return result

def app_info():
    image_path = "sleep.jpg"
    st.image(image_path, use_column_width=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("The Sleep Disorder Prediction App is a comprehensive tool designed to help individuals and healthcare professionals assess and predict the likelihood of sleep disorders based on various health and lifestyle factors. This interactive and user-friendly application leverages data visualization and machine learning to provide insights and predictions related to sleep health.")
    st.write("The Sleep Disorder Prediction app evaluates the likelihood of a sleep disorder by analyzing a range of essential health and lifestyle attributes. These attributes include:")
    st.markdown("""
    - Person ID
    - Gender
    - Age
    - Occupation
    - Sleep Duration (hours)
    - Quality of Sleep (scale: 1-10)
    - Physical Activity Level (minutes/day)
    - Stress Level (scale: 1-10)
    - BMI Category
    - Blood Pressure (systolic/diastolic)
    - Heart Rate (bpm)
    - Daily Steps
    """)
   

def info_graphics():
    st.write("### About Dataset")
    st.write("The Sleep Health and Lifestyle Dataset comprises 400 rows and 13 columns, covering a wide range of variables related to sleep and daily habits. It includes details such as gender, age, occupation, sleep duration, quality of sleep, physical activity level, stress levels, BMI category, blood pressure, heart rate, daily steps, and the presence or absence of sleep disorders.")
    st.write("#### Attributes")
    st.write("Person ID: An identifier for each individual.")
    st.write("Gender: The gender of the person (Male/Female).")
    st.write("Age: The age of the person in years.")
    st.write("Occupation: The occupation or profession of the person.")
    st.write("Sleep Duration (hours): The number of hours the person sleeps per day.")
    st.write("Quality of Sleep (scale: 1-10): A subjective rating of the quality of sleep, ranging from 1 to 10.")
    st.write("Physical Activity Level (minutes/day): The number of minutes the person engages in physical activity daily.")
    st.write("Stress Level (scale: 1-10): A subjective rating of the stress level experienced by the person, ranging from 1 to 10.")
    st.write("BMI Category: The BMI category of the person (e.g., Underweight, Normal, Overweight).")
    st.write("Blood Pressure (systolic/diastolic): The blood pressure measurement of the person, indicated as systolic pressure over diastolic pressure.")
    st.write("Heart Rate (bpm): The resting heart rate of the person in beats per minute.")
    st.write("Daily Steps: The number of steps the person takes per day.")
    st.write("Sleep Disorder: The presence or absence of a sleep disorder in the person (None, Insomnia, Sleep Apnea).")

    plot_pie_chart(ds)
    plot_countplot(ds)
    hist_plot(ds)
    histogram(ds)
    scatter_plot(ds)
    barplot(ds)
    countplot_bmi(ds)
    boxplot(ds)
    sleep_pie_chart(ds)
    
def input_tab():
    options = {"Male":0,"Female":1}
    gender = st.radio("Gender",list(options.keys()), horizontal=True)
    bmi_options={'Overweight':0,'Normal':1,'Obese':2,'Underweight':3}
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
        disorder_info = disorder_mapping.get(result[0], {
            "name": "Unknown Disorder",
            "description": "The model predicted an unknown disorder.",
            "causes": "N/A",
            "tips": "N/A"
        })
        st.markdown(f"""
        <style>
        .result {{
            font-size: 50px;  /* Increase font size */
            text-align: center;  /* Center align text */
        }}
        </style>
        <div class="result">
            Sleep Disorder: {disorder_info['name']}
        </div>
        """, unsafe_allow_html=True)
        st.write(f"**Description:** {disorder_info['description']}")
        st.write(f"**Causes:** {disorder_info['causes']}")
        st.write(f"**Tips:** {disorder_info['tips']}")
    
        
def main():
    st.title("Sleep Disorder Prediction App")
    tabs = ["App Description","Info Graphics", "Prediction"]
    selected_tab = st.sidebar.radio("Choose a tab", tabs)
    if selected_tab == "App Description":
        app_info()
    elif selected_tab == "Info Graphics":
        info_graphics()
    elif selected_tab == "Prediction":
        input_tab()
if __name__ == "__main__":
    main()