from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle

# load model
model=pickle.load(open("model\car_price_predictor_model.pkl",'rb'))

app=FastAPI()

class Input(BaseModel):
    Year:int
    Kms_Driven:int
    Present_Price:float
    Fuel_Type:int
    Transmission:int
    Owner:int

@app.get("/")
def read_root():
    return {"msg":"Car Price Predictor"}

@app.post("/predict")
def predict_price(input:Input):
    data = input.dict()
    data_in = [[data['Year'], data['Kms_Driven'], data['Present_Price'], data['Fuel_Type'],
                    data['Transmission'], data['Owner']]]

    prediction = model.predict(data_in)
    return {
        'prediction': prediction[0]
        }

if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)