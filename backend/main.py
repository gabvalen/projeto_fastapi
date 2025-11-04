from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# ✅ Novo modelo da entrada de dados
class Aluno(BaseModel):
    Age: int
    Gender: str
    Address: str
    Mother_Education: int
    Father_Education: int
    Mother_Job: str
    Travel_Time: int
    Study_Time: int
    Free_Time: int
    Going_Out: int
    Weekend_Alcohol_Consumption: int
    Weekday_Alcohol_Consumption: int
    Number_of_Absences: int
    Grade_1: int
    Grade_2: int
    Final_Grade: int
    Wants_Higher_Education: str
    Internet_Access: str
    In_Relationship: str

    class Config:
        schema_extra = {
            "example": {
                "Age": 17,
                "Gender": "F",
                "Address": "U",
                "Mother_Education": 2,
                "Father_Education": 3,
                "Mother_Job": "health",
                "Travel_Time": 2,
                "Study_Time": 3,
                "Free_Time": 4,
                "Going_Out": 3,
                "Weekend_Alcohol_Consumption": 2,
                "Weekday_Alcohol_Consumption": 1,
                "Number_of_Absences": 5,
                "Grade_1": 14,
                "Grade_2": 15,
                "Final_Grade": 16,
                "Wants_Higher_Education": "yes",
                "Internet_Access": "yes",
                "In_Relationship": "no"
            }
        }

# Inicializar o app
app = FastAPI(title="API Previsão de Evasão")

# Carregar o modelo treinado
with open("modelo_completo.pkl", "rb") as f:
    modelo_info = pickle.load(f)

modelo = modelo_info["model"]
colunas_encoded_final = modelo_info["colunas_encoded_final"]

@app.get("/")
def home():
    return {"mensagem": "API de previsão de evasão rodando com sucesso!"}

@app.post("/predict")
def prever(aluno: Aluno):
    dados = [aluno.dict()]
    import pandas as pd
    df = pd.DataFrame(dados)
    df_encoded = pd.get_dummies(df, dtype=int)
    df_alinhado = df_encoded.reindex(columns=colunas_encoded_final, fill_value=0)

    previsao = modelo.predict(df_alinhado)[0]
    return {
        "previsao": bool(previsao),
        "mensagem": "PROVÁVEL EVASÃO" if previsao else "NÃO DEVE EVADIR"
    }