from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Modelo da entrada de dados
class Aluno(BaseModel):
    idade: int
    serie: int
    mudou_escola: int
    distorcao_idade_serie: int

# Inicializar o app
app = FastAPI(title="API Previsão de Evasão")

# Carregar o modelo treinado (o Isaque vai te passar o modelo.pkl)
with open("modelo.pkl", "rb") as f:
    modelo = pickle.load(f)

@app.get("/")
def home():
    return {"mensagem": "API de previsão de evasão rodando com sucesso!"}

@app.post("/predict")
def prever(aluno: Aluno):
    dados = [[
        aluno.idade,
        aluno.serie,
        aluno.mudou_escola,
        aluno.distorcao_idade_serie
    ]]
    previsao = modelo.predict(dados)[0]
    probabilidade = modelo.predict_proba(dados)[0].tolist()

    return {
        "previsao": int(previsao),
        "probabilidade": probabilidade
    }
