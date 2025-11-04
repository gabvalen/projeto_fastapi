# Projeto FastAPI - Previsão de Evasão Escolar

Este projeto tem como objetivo construir uma API em Python utilizando FastAPI para prever o risco de evasão escolar de alunos com base em dados educacionais. A aplicação integra um modelo de Machine Learning treinado com microdados  e fornece previsões via endpoint `/predict`.

## 🎯 Objetivo

Ajudar gestores escolares a identificar alunos com maior risco de evasão, permitindo ações preventivas baseadas em dados.

## 🧠 Estrutura dos Squads

### Squad 1: Dados & Inteligência Artificial
- **Izabelle** – Líder de Dados / Engenheira de Dados Principal
  - Lidera a coleta e processamento dos dados.
  - Baixa microdados do INEP (Censo Escolar, SAEB).
  - Cruza as bases via ID_ALUNO.
  - Cria a variável-alvo EVADIU.
  - Entrega dataset limpo e consistente.

- **Sutani** – Analista de Dados / Engenharia de Features
  - Faz análise exploratória (EDA).
  - Cria visualizações para entender padrões.
  - Desenvolve features (ex.: Distorção Idade-Série, Mudança de Escola).
  - Documenta o dicionário de dados.

- **Isaque** – Cientista de Dados / Modelagem de Machine Learning
  - Pesquisa e seleciona algoritmos (Logística, Random Forest, XGBoost).
  - Treina, testa e otimiza modelos.
  - Avalia métricas (AUC-ROC, Precisão, Recall, etc.).
  - Salva modelo final em .pkl ou .joblib.

- **Anderson** – Validação & Qualidade de Dados
  - Valida a qualidade dos dados processados.
  - Testa a lógica da variável EVADIU.
  - Analisa possíveis vieses (gênero, raça).
  - Apoia a documentação técnica.

### Squad 2: Desenvolvimento Web & Visualização
- **Gabriela** – Líder de Projeto & Desenvolvedora Backend
  - Coordena geral e garante comunicação entre squads.
  - Desenvolve o backend (API com Flask/FastAPI).
  - Integra o modelo .pkl do Isaque.
  - Entrega previsões de risco via API.

- **Kevin** – Desenvolvedor Frontend / Dashboard Principal
  - Constrói a interface (Streamlit/Dash).
  - Cria tabelas, filtros, gráficos.
  - Faz chamadas para API e exibe previsões.

- **Caio** – UI/UX Designer & Frontend Auxiliar
  - Desenha layout e experiência do usuário.
  - Prototipa no Figma/Canva.
  - Implementa design (CSS, visuais).
  - Garante interface clara e intuitiva.

- **Vicente** – Infraestrutura (DevOps) & Documentação Técnica
  - Pesquisa e implementa deploy (Streamlit Cloud, Heroku, etc.).
  - Garante site online e funcional.
  - Escreve documentação técnica (instalação, execução, API).

## Tecnologias Utilizadas

### Linguagens e Frameworks
- **Python**: Linguagem principal utilizada no projeto.
- **FastAPI**: Framework para construção da API REST.
- **Pandas**: Manipulação e análise de dados.
- **Scikit-learn**: Treinamento e avaliação de modelos de Machine Learning.
- **XGBoost**: Algoritmo de aprendizado de máquina utilizado na modelagem.
- **Streamlit / Dash**: Frameworks para construção do dashboard interativo.
- **HTML / CSS / JavaScript**: Tecnologias utilizadas no frontend.

### Ferramentas e Ambiente
- **VS Code**: Ambiente de desenvolvimento.
- **Jupyter Notebook**: Análise exploratória e desenvolvimento de modelos.
- **Git & GitHub**: Controle de versão e hospedagem do código.
- **Render / Railway / Heroku**: Alternativas para deploy da aplicação.
- **Figma / Canva**: Prototipagem e design da interface.
