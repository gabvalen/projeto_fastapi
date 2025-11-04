import pickle

try:
    with open('modelo_completo.pkl', 'rb') as f:
        modelo = pickle.load(f)
    print("✅ Modelo carregado com sucesso!")
except Exception as e:
    print("❌ Erro ao carregar o modelo:")
    print(e)