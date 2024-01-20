from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle


class HouseFeatures(BaseModel):
    area: float
    bedrooms: float
    bathrooms: float
    stories: float
    mainroad: float
    guestroom: float
    basement: float
    hotwaterheating: float
    airconditioning: float
    parking: float
    prefarea: float
    furnished: float
    semi_furnished: float
    unfurnished: float


app = FastAPI()


@app.post("/predict")
def read_root(item: HouseFeatures):
    data = [{'area': item.area,
             'bedrooms':  item.bedrooms,
             'bathrooms':  item.bathrooms,
             'stories':  item.stories,
             'mainroad':  item.mainroad,
             'guestroom':  item.guestroom,
             'basement':  item.basement,
             'hotwaterheating':  item.hotwaterheating,
             'airconditioning':  item.airconditioning,
             'parking':  item.parking,
             'prefarea':  item.prefarea,
             'furnished':  item.furnished,
             'semi-furnished':  item.semi_furnished,
             'unfurnished': item.unfurnished
             }]
    df = pd.DataFrame(data)
    with open('./model/model.pkl', 'rb') as f:
        clf2 = pickle.load(f)
    
    return {"Predict": str(clf2.predict(df))}
