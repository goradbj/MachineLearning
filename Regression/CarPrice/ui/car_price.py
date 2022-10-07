import streamlit as st
import requests
import json

def main():
    st.title("CAR PRICE PREDICTOR")
    
    Year = st.number_input("Year")
    
    Kms_Driven = st.number_input("Kms_Driven")
    
    Present_Price = st.number_input("Present_Price(in lacs)")
    
    Fuel_Type = st.selectbox("Fuel_Type",("CNG","Diesel","Petrol"))
    if Fuel_Type=="CNG":
        Fuel_Type=0
    elif Fuel_Type=="Diesel":
        Fuel_Type=1
    else:
        Fuel_Type=2
    
    Transmission = st.selectbox("Transmission",("Automatic","Manual"))
    if Transmission=="Automatic":
        Transmission=0
    else:
        Transmission=1
    
    Owner = st.selectbox("Owner",("First","Second","Third","Fourth"))
    if Owner=="First":
        Owner=0
    elif Owner=="Second":
        Owner=1
    elif Owner=="Third":
        Owner=2
    else:
        Owner=3

    input_data={
        "Year":Year,
        "Kms_Driven":Kms_Driven,
        "Present_Price":Present_Price,
        "Fuel_Type":Fuel_Type,
        "Transmission":Transmission,
        "Owner":Owner
    }

    price=0
    if st.button("Predict"):
        price=requests.post(url="http://127.0.0.1:8000/predict",data=json.dumps(input_data))
        price=price.json()
        p=price['prediction']
        st.success(f'The Price of the Car is {p} lacks')
    

if __name__=='__main__':
    main()