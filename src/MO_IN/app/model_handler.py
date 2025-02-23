import pickle
import pandas as pd

# Carregar os dois modelos treinados
with open('model/modelo_gradient_boosting_interno.pkl', 'rb') as file:
    model_interno = pickle.load(file)

with open('model/modelo_gradient_boosting_externo.pkl', 'rb') as file:
    model_externo = pickle.load(file)

def predict_outcomes(data):
    """
    Função para fazer previsões com os dois modelos carregados.
    """
    # Realizar o One-Hot Encoding de acordo com o que foi feito no treinamento
    df_encoded = pd.get_dummies(data)

    # Garantir que as colunas de features de treinamento sejam as mesmas
    # Pegue as colunas do modelo (as colunas usadas no treinamento)
    model_columns_interno = model_interno.feature_names_in_  # Captura as colunas usadas no treinamento
    model_columns_externo = model_externo.feature_names_in_  # Captura as colunas usadas no treinamento

    # Garantir que as colunas de entrada estejam presentes
    missing_cols_interno = set(model_columns_interno).difference(df_encoded.columns)
    missing_cols_externo = set(model_columns_externo).difference(df_encoded.columns)

    # Adicionar as colunas faltantes com valor 0 (zero)
    for c in missing_cols_interno:
        df_encoded[c] = 0  # Adiciona as colunas faltantes para o modelo de Laborterapia Interna

    for c in missing_cols_externo:
        df_encoded[c] = 0  # Adiciona as colunas faltantes para o modelo de Laborterapia Externa

    # Reorganiza as colunas para garantir a ordem correta
    df_encoded_interno = df_encoded[model_columns_interno]
    df_encoded_externo = df_encoded[model_columns_externo]

    # Fazer previsões para ambos os modelos
    predictions_interno = model_interno.predict(df_encoded_interno)
    predictions_externo = model_externo.predict(df_encoded_externo)
    
    # Adicionar previsões aos dados originais
    data['Previsões Interno'] = predictions_interno
    data['Previsões Externo'] = predictions_externo
    
    # Retornar os dados com as previsões
    return data.to_dict(orient='records')
