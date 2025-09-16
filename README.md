**🎨 API de Previsão de Risco de Evasão Escolar**
Esta é a API de backend para o nosso projeto, construída para prever o risco de evasão escolar. Ela é a ponte entre o frontend e o modelo de Machine Learning.

**⚙️ Tecnologias Utilizadas**
FastAPI: O framework super-rápido para construir a API.

Pydantic: Para garantir que os dados de entrada sejam sempre perfeitos.

scikit-learn & pickle: Para carregar e usar o nosso modelo de IA.

**🚀 Como Rodar a API Localmente**
Para que tudo funcione, siga estes passos simples:

**Pré-requisitos:** Tenha certeza de que o **Python** está instalado.

**Instalação:** Abra o terminal na pasta do projeto e instale as bibliotecas.

pip install fastapi uvicorn scikit-learn
**Arquivo do Modelo:** A API depende de um arquivo crucial, o modelo.pkl.

⚠️  **ATENÇÃO: Este projeto só funcionará após a equipe de Ciência de Dados fornecer este arquivo.** Ele deve ser colocado na mesma pasta que o main.py.

**Executar:** Inicie o servidor Uvicorn com este comando.

uvicorn main:app --reload
Sua API estará online e pronta para ser usada em http://127.0.0.1:8000.

🛣️**Endpoints da API**
A documentação interativa completa (Swagger UI) está disponível em http://127.0.0.1:8000/docs para você testar e explorar!

**GET /
Descrição:** Uma rota de boas-vindas para confirmar que a API está no ar.

**POST /predict
Descrição:** Recebe os dados de um aluno e retorna a previsão de risco de evasão.

**Corpo da Requisição (JSON de Entrada):**

{
  "idade": 15,
  "serie": 9,
  "mudou_escola": 1,
  "distorcao_idade_serie": 1
}
**Resposta (JSON de Saída):**

JSON

{
  "previsao": 1,
  "probabilidade": [0.25, 0.75]
}
previsao: 1 = alto risco de evasão; 0 = baixo risco.

probabilidade: A chance de ser da classe 0 (baixo risco) e da classe 1 (alto risco), respectivamente.

🤝 **Suporte e Contato**
Qualquer dúvida sobre a API ou a integração, podem me procurar! Estou à disposição para ajudar a equipe de Frontend e DevOps a colocar o projeto em produção.


