import pandas as pd
import pickle

def prever_evasao(novos_alunos):
    """
    Carrega o modelo treinado e faz previsões para uma lista de novos alunos.

    Args:
        novos_alunos (list of dict): Uma lista onde cada dicionário representa
                                     um aluno com seus dados.

    Returns:
        list: Uma lista de strings com os resultados das previsões.
    """
    try:
        # 1. Carregar o modelo e os metadados salvos
        with open('modelo_completo.pkl', 'rb') as f:
            modelo_info = pickle.load(f)

        model = modelo_info['model']
        # Pega a lista de colunas que o modelo espera APÓS o encoding
        colunas_encoded_final = modelo_info['colunas_encoded_final']

        print("✅ Modelo 'modelo_completo.pkl' carregado com sucesso.")

        # 2. Converter os novos dados para um DataFrame do pandas
        novos_dados_df = pd.DataFrame(novos_alunos)

        # 3. Aplicar o One-Hot Encoding nos novos dados
        novos_dados_encoded = pd.get_dummies(novos_dados_df, dtype=int)

        # 4. Alinhar as colunas do novo DataFrame com as colunas do modelo
        # Esta é a etapa CRÍTICA. O .reindex garante que o novo dataframe tenha
        # exatamente as mesmas colunas (na mesma ordem) que o modelo foi treinado.
        # As colunas que não existirem nos novos dados (ex: Mother_Job_health)
        # serão criadas e preenchidas com 0.
        novos_dados_alinhado = novos_dados_encoded.reindex(
            columns=colunas_encoded_final, fill_value=0
        )

        # 5. Fazer as previsões
        predicoes = model.predict(novos_dados_alinhado)

        # 6. Formatar os resultados para exibição
        resultados = []
        for i, predicao in enumerate(predicoes):
            nome_aluno = f"Aluno {i+1}"
            resultado = "PROVÁVEL EVASÃO (True)" if predicao else "NÃO DEVE EVADIR (False)"
            resultados.append(f"Previsão para {nome_aluno}: {resultado}")
            
        return resultados

    except FileNotFoundError:
        return ["❌ ERRO: Arquivo 'modelo_completo.pkl' não encontrado. Execute o script de treinamento primeiro."]
    except Exception as e:
        return [f"❌ ERRO inesperado durante a previsão: {e}"]

# --- Início da Execução ---
if __name__ == "__main__":
    # Criando 3 perfis de alunos para testar a previsão.
    # Os valores são baseados no arquivo de análise.
    
    # Aluno 1: Perfil de alto risco
    aluno_risco_alto = {
        'Age': 19, 'Gender': 'M', 'Address': 'R',
        'Mother_Education': 1, 'Father_Education': 1, 'Mother_Job': 'other',
        'Travel_Time': 4, 'Study_Time': 1, 'Wants_Higher_Education': 'no',
        'Internet_Access': 'no', 'In_Relationship': 'yes',
        'Free_Time': 5, 'Going_Out': 5,
        'Weekend_Alcohol_Consumption': 5, 'Weekday_Alcohol_Consumption': 5,
        'Number_of_Absences': 20, 'Grade_1': 8, 'Grade_2': 7, 'Final_Grade': 6
    }

    # Aluno 2: Perfil de baixo risco
    aluno_risco_baixo = {
        'Age': 16, 'Gender': 'F', 'Address': 'U',
        'Mother_Education': 4, 'Father_Education': 4, 'Mother_Job': 'health',
        'Travel_Time': 1, 'Study_Time': 4, 'Wants_Higher_Education': 'yes',
        'Internet_Access': 'yes', 'In_Relationship': 'no',
        'Free_Time': 3, 'Going_Out': 2,
        'Weekend_Alcohol_Consumption': 1, 'Weekday_Alcohol_Consumption': 1,
        'Number_of_Absences': 0, 'Grade_1': 18, 'Grade_2': 19, 'Final_Grade': 19
    }

    # Aluno 3: Perfil intermediário/mediano
    aluno_intermediario = {
        'Age': 17, 'Gender': 'M', 'Address': 'U',
        'Mother_Education': 2, 'Father_Education': 2, 'Mother_Job': 'services',
        'Travel_Time': 2, 'Study_Time': 2, 'Wants_Higher_Education': 'yes',
        'Internet_Access': 'yes', 'In_Relationship': 'no',
        'Free_Time': 3, 'Going_Out': 3,
        'Weekend_Alcohol_Consumption': 3, 'Weekday_Alcohol_Consumption': 2,
        'Number_of_Absences': 4, 'Grade_1': 12, 'Grade_2': 11, 'Final_Grade': 11
    }
    
    # Lista com todos os alunos para fazer a previsão de uma vez
    lista_de_alunos = [aluno_risco_alto, aluno_risco_baixo, aluno_intermediario]
    
    # Chama a função e imprime os resultados
    resultados_finais = prever_evasao(lista_de_alunos)
    
    print("\n--- Resultados da Previsão ---")
    for res in resultados_finais:
        print(res)