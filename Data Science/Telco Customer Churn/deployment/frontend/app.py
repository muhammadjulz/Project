import streamlit as st
import pandas as pd
import requests



def run():
    # Membuat Title
    st.title('Telco Customer Churn')
    # Membuat subheader
    st.subheader('Berikut Adalah Web-Applikasi untuk memprediksi bahwa customer tidak akan berlangganan kembali')
    # Membuat deskripsi
    st.write('page ini dibuat oleh Muhammad Julizar')

    with st.form(key='form_parameters'):
        gender = st.radio('gender', ('Male', 'Female'))
        SeniorCitizen = st.radio('SeniorCitizen', (0,1))
        Partner = st.radio('Partner',('Yes', 'No'))
        Dependents = st.radio('Dependents', ('Yes', 'No'))
        MultipleLines = st.radio('MultipleLines', ('Yes','No','No phone service'))
        InternetService = st.radio('InternetService', ('DSL', 'Fiber optic', 'No'))
        OnlineSecurity = st.radio('OnlineSecurity', ('Yes', 'No'))
        OnlineBackup = st.radio('OnlineBackup', ('Yes', 'No'))
        DeviceProtection = st.radio('DeviceProtection', ('Yes', 'No')) 
        TechSupport = st.radio('TechSupport', ('Yes', 'No')) 
        Contract = st.radio('Contract', ('Month-to-month', 'Two year', 'One year'))
        PaperlessBilling = st.radio('PaperlessBilling', ('Yes', 'No'))
        PaymentMethod = st.radio('PaymentMethod', ('Electronic check', 'Mailed check', 'Bank transfer (automatic)','Credit card (automatic)'))
        tenure = st.number_input('tenure', min_value=0, value=0, step=1)
        MonthlyCharges = st.number_input('MonthlyCharges', min_value=0, value=0)
        TotalCharges = st.number_input('TotalCharges', min_value=0, value=0)

        submitted = st.form_submit_button('Predict')
    
    # Create A New data
    data_inf = {
        'gender': gender,
        'SeniorCitizen': SeniorCitizen,
        'Partner': Partner,
        'Dependents': Dependents,
        'MultipleLines': MultipleLines,
        'InternetService': InternetService,
        'OnlineSecurity': OnlineSecurity,
        'OnlineBackup': OnlineBackup,
        'DeviceProtection': DeviceProtection,
        'TechSupport': TechSupport,
        'Contract': Contract,
        'PaperlessBilling': PaperlessBilling,
        'PaymentMethod': PaymentMethod,
        'tenure' : tenure,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges' : TotalCharges
    }

    if submitted:
        # Show Inference DataFrame
        st.dataframe(pd.DataFrame([data_inf]))
        print('[DEBUG] Data Inference : \n', data_inf)
        
        # Predict
        URL = "https://backend-telco-churn-muhammadjulizar1.koyeb.app/predict"
        r = requests.post(URL, json=data_inf)

        if r.status_code == 200:
            res = r.json()
            st.write('## Prediction : ', res['label_names'])
            print('[DEBUG] Result : ', res)
            print('')
        else:
            st.write('Error with status code ', str(r.status_code))
        

if __name__ == '__main__':
    run()