import streamlit as st

# Configuração da página principal
st.set_page_config(
    page_title="Sistema de Evasão Escolar",
    layout="wide",
    page_icon="🎓"
)

# Esconde o item 'app' do menu lateral
st.markdown("""
    <style>
        /* Esconde o item 'app' da barra lateral */
        [data-testid="stSidebarNav"] ul li:first-child {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# 🔹 Conteúdo da página inicial
st.title("🎓 Sistema de Análise e Predição de Evasão Escolar")
st.markdown("""
### Bem-vindo!
Use o menu lateral à esquerda para navegar entre as seções:
- 📘 **Sobre**
- 🔍 **Predição**
- 📊 **Gráficos**
""")





















