import streamlit as st
import pandas as pd

from data_preprocessing import data_preprocessing
from prediction import prediction

st.header('Jaya Jaya Institute Students Perfomance Prediction')

data = {}
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    opt = ['Female', 'Male']
    Gender = st.selectbox(
        label ='Gender',
        options = range(len(opt)),
        format_func = lambda x: opt[x]
    )
    data['Gender'] = Gender

with col2:
    opt = ['No', 'Yes']
    Scholarship_holder = st.selectbox(
        label = 'Scolarship Holder',
        options = range(len(opt)),
        format_func = lambda x: opt[x]
    )
    data['Scholarship_holder'] = Scholarship_holder

with col3:
    opt = ['No', 'Yes']
    Debtor = st.selectbox(
        label = 'Debtor',
        options = range(len(opt)),
        format_func = (lambda x: opt[x])
    )
    data['Debtor'] = Debtor

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    opt = ['No', 'Yes']
    Displaced = st.selectbox(
        label = 'Displaced',
        options = range(len(opt)),
        format_func = (lambda x: opt[x])
    )
    data['Displaced'] = Displaced

with col2:
    Age_at_enrollment = st.number_input(
        label = 'Age at Enrollment',
        min_value = 0,
        max_value = 80,
        value = 19
    )
    data['Age_at_enrollment'] = Age_at_enrollment


with col3:
    Admission_grade = st.number_input(
        label = 'Admission Grade',
        min_value = 0,
        max_value = 200,
        value = 120
    )
    data['Admission_grade'] = Admission_grade

col1, col2 = st.columns([2, 1])
with col1:
    opt = {
        1: '1st Phase - General Contingent',
        2: 'Ordinance No. 612/93',
        5: '1st Phase - Special Contingent (Azores Island)',
        7: 'Holders of Other Higher Courses',
        10: 'Ordinance No. 854-B/99',
        15: 'International Student (Bachelor)',
        16: '1st Phase - Special Contingent (Madeira Island)',
        17: '2nd Phase - General Contingent',
        18: '3rd Phase - General Contingent',
        26: 'Ordinance No. 533-A/99 (Different Plan)',
        27: 'Ordinance No. 533-A/99 (Other Institution)',
        39: 'Over 23 Years old',
        42: 'Transfer', 
        43: 'Change of Course',
        44: 'Technological Specialization Diploma Holders',
        51: 'Change of Institution/Course',
        53: 'Short Cycle Diploma Holder',
        57: 'Change of Institution/Course (International)'
    }
    Application_mode = st.selectbox(
        label = 'Application Mode',
        options = list(opt.keys()),
        format_func = lambda x: opt[x]
    )
    data['Application_mode'] = Application_mode

with col2:
    opt = ['No', 'Yes']
    Tuition_fees_up_to_date = st.selectbox(
        label = 'Tuition Fees Up to Date',
        options = range(len(opt)),
        format_func = (lambda x: opt[x])
    )
    data['Tuition_fees_up_to_date'] = Tuition_fees_up_to_date

col1, col2, col3 = st.columns(3)
with col1:
    Curricular_units_1st_approved = st.number_input(
        label = 'Curricular Units 1st Sem Approved',
        min_value = 0,
        value = 8
    )
    data['Curricular_units_1st_sem_approved'] = Curricular_units_1st_approved

with col2:
    Curricular_units_1st_enrolled = st.number_input(
        label = 'Curricular Units 1st Sem Enrolled',
        min_value = 0,
        value = 10
    )
    data['Curricular_units_1st_sem_enrolled'] = Curricular_units_1st_enrolled

with col3:
    Curricular_units_1st_grade = st.number_input(
        label = 'Curricular Units 1st Sem Grade',
        min_value = 0,
        value = 8
    )
    data['Curricular_units_1st_sem_grade'] = Curricular_units_1st_grade

col1, col2, col3 = st.columns(3)
with col1:
    Curricular_units_2nd_approved = st.number_input(
        label = 'Curricular Units 2nd Sem Approved',
        min_value = 0,
        value = 8
    )
    data['Curricular_units_2nd_sem_approved'] = Curricular_units_2nd_approved

with col2:
    Curricular_units_2nd_enrolled = st.number_input(
        label = 'Curricular Units 2nd Sem Enrolled',
        min_value = 0,
        value = 10
    )
    data['Curricular_units_2nd_sem_enrolled'] = Curricular_units_2nd_enrolled

with col3:
    Curricular_units_2nd_grade = st.number_input(
        label = 'Curricular Units 2nd Sem Grade',
        min_value = 0,
        value = 8
    )
    data['Curricular_units_2nd_sem_grade'] = Curricular_units_2nd_grade

input_df = pd.DataFrame([data])

with st.expander('View the Raw Data'):
    st.dataframe(data=input_df, width=800, height=18)

if st.button('Predict'):
    new_data = data_preprocessing(data=input_df)

    with st.expander('View the Preprocessed Data'):
        st.dataframe(data=new_data, width=800, height=18)
    
    st.write('Prediction Result: {}'.format(prediction(new_data)))