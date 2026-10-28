
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

model = joblib.load("model.joblib")
app = FastAPI(title="Penguin species")


class Penguin(BaseModel):
    bill_length_mm: float
    bill_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(penguin: Penguin):
    X = pd.DataFrame([penguin.model_dump()])
    return {"species": model.predict(X)[0]}


from fastapi.responses import FileResponse

@app.get("/")
def home():
    return FileResponse("index.html")
