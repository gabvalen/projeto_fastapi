Como executar o projeto localmente:

Abre dois terminais na raiz do projeto e nos dois terminais execute o ambiente virtual: 
python -m venv .venv

Nos dois terminais ative o ambiente virtual com o comando: 
.venv\Scripts\activate

E em seguida instale as dependencias com o comando: pip install -r requirements.txt

***Rodar o backend***
cd backend
python -m uvicorn main:app --reload

***Rodar o frontend***
cd frontend
python -m streamlit run app.py