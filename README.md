Esta API fornece um endpoint para a previsão de risco de evasão escolar com base em dados de um aluno.
Tecnologias:  bibliotecas usadas: FastAPI, Pydantic, pickle e scikit-learn. 
Como Usar a API 

Endpoint de Previsão: 

Método: POST 

URL: http://127.0.0.1:8000/predict 

Corpo da Requisição (Request Body) é o formato JSON esperado. Segue código da  classe Aluno como exemplo. 

JSON 

{ 
  "idade": 15, 
  "serie": 9, 
  "mudou_escola": 1, 
  "distorcao_idade_serie": 1 
} 
 

Resposta da API (Response):  resposta JSON. 
JSON 

{ 
  "previsao": 1, 
  "probabilidade": [0.25, 0.75] 
} 
 Oque significa cada campo: previsao (0 para "sem evasão", 1 para "com evasão") e probabilidade (probabilidade de ser classe 0 e 1, respectivamente). 
 
