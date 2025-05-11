import joblib
import pandas as pd
import numpy as np

scaler_Admission_grade = joblib.load('model/scaler_Admission_grade.joblib')
scaler_Age_at_enrollment = joblib.load('model/scaler_Age_at_enrollment.joblib')
scaler_Application_mode = joblib.load('model/scaler_Application_mode.joblib')
scaler_Curricular_units_1st_sem_approved = joblib.load('model/scaler_Curricular_units_1st_sem_approved.joblib')
scaler_Curricular_units_1st_sem_enrolled = joblib.load('model/scaler_Curricular_units_1st_sem_enrolled.joblib')
scaler_Curricular_units_1st_sem_grade = joblib.load('model/scaler_CUrricular_units_1st_sem_grade.joblib')
scaler_Curricular_units_2nd_sem_approved = joblib.load('model/scaler_Curricular_units_2nd_sem_approved.joblib')
scaler_Curricular_units_2nd_sem_enrolled = joblib.load('model/scaler_Curricular_units_2nd_sem_enrolled.joblib')
scaler_Curricular_units_2nd_sem_grade = joblib.load('model/scaler_CUrricular_units_2nd_sem_grade.joblib')
scaler_Debtor = joblib.load('model/scaler_Debtor.joblib')
scaler_Displaced = joblib.load('model/scaler_Displaced.joblib')
scaler_Gender = joblib.load('model/scaler_Gender.joblib')
scaler_Scholarship_holder = joblib.load('model/scaler_Scholarship_holder.joblib')
scaler_Tuition_fees_up_to_date = joblib.load('model/scaler_Tuition_fees_up_to_date.joblib')

def data_preprocessing(data):
    """
    Preprocessing data    

    Args:
        data (Pandas DataFrame): Dataframe that contain all the data to make prediction             
    return:
        Pandas DataFrame: Dataframe that contain all the preprocessed data
    """

    data = data.copy()
    df = pd.DataFrame()

    df['Admission_grade'] = scaler_Admission_grade.transform(np.asarray(data['Admission_grade']).reshape(-1, 1))[0]
    df['Age_at_enrollment'] = scaler_Age_at_enrollment.transform(np.asarray(data['Age_at_enrollment']).reshape(-1, 1))[0]
    df['Application_mode'] = scaler_Application_mode.transform(np.asarray(data['Application_mode']).reshape(-1, 1))[0]
    df['Curricular_units_1st_sem_approved'] = scaler_Curricular_units_1st_sem_approved.transform(np.asarray(data['Curricular_units_1st_sem_approved']).reshape(-1, 1))[0]
    df['Curricular_units_1st_sem_enrolled'] = scaler_Curricular_units_1st_sem_enrolled.transform(np.asarray(data['Curricular_units_1st_sem_enrolled']).reshape(-1, 1))[0]
    df['Curricular_units_1st_sem_grade'] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(data['Curricular_units_1st_sem_grade']).reshape(-1, 1))[0]
    df['Curricular_units_2nd_sem_approved'] = scaler_Curricular_units_2nd_sem_approved.transform(np.asarray(data['Curricular_units_2nd_sem_approved']).reshape(-1, 1))[0]
    df['Curricular_units_2nd_sem_enrolled'] = scaler_Curricular_units_2nd_sem_enrolled.transform(np.asarray(data['Curricular_units_2nd_sem_enrolled']).reshape(-1, 1))[0]
    df['Curricular_units_2nd_sem_grade'] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(data['Curricular_units_2nd_sem_grade']).reshape(-1, 1))[0]
    df['Debtor'] = scaler_Debtor.transform(np.asarray(data['Debtor']).reshape(-1, 1))[0]
    df['Displaced'] = scaler_Displaced.transform(np.asarray(data['Displaced']).reshape(-1, 1))[0]
    df['Gender'] = scaler_Gender.transform(np.asarray(data['Gender']).reshape(-1, 1))[0]
    df['Scholarship_holder'] = scaler_Scholarship_holder.transform(np.asarray(data['Scholarship_holder']).reshape(-1, 1))[0]
    df['Tuition_fees_up_to_date'] = scaler_Tuition_fees_up_to_date.transform(np.asarray(data['Tuition_fees_up_to_date']).reshape(-1, 1))[0]

    selected_cols = ['Application_mode', 'Admission_grade', 'Displaced', 'Debtor',
       'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder',
       'Age_at_enrollment', 'Curricular_units_1st_sem_enrolled',
       'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
       'Curricular_units_2nd_sem_enrolled',
       'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade']
    df = df[selected_cols]
    
    return df
