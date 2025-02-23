from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd
import os

# Carregar a planilha de dados
file_path_updated = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Tabela SISDEPEN e IBGE.xlsx')
df_updated = pd.read_excel(file_path_updated, sheet_name='Sheet1')

# One-Hot Encoding para transformar variáveis categóricas em numéricas
df_encoded = pd.get_dummies(df_updated)

# Selecionar as variáveis explicativas (excluindo os targets)
features = df_encoded.drop(columns=['6.1 Laborterapia | Trabalho Interno | Total', 
                                    '6.1 Laborterapia | Trabalho Externo | Total'])

# Selecionar as variáveis-alvo (targets) separadamente
target_interno = df_encoded['6.1 Laborterapia | Trabalho Interno | Total']
target_externo = df_encoded['6.1 Laborterapia | Trabalho Externo | Total']

# Dividir os dados em treino e teste para cada target
from sklearn.model_selection import train_test_split
X_train, X_test, y_train_interno, y_test_interno = train_test_split(features, target_interno, test_size=0.2, random_state=42)
_, _, y_train_externo, y_test_externo = train_test_split(features, target_externo, test_size=0.2, random_state=42)

# Definir o modelo de Gradient Boosting
modelo_gb_interno = GradientBoostingRegressor(random_state=42)

# Definir os parâmetros a serem testados no GridSearchCV
param_grid = {
    'n_estimators': [100, 150, 200, 250, 300],       
    'max_depth': [2, 3, 4, 5],                    
    'learning_rate': [0.01, 0.02, 0.03, 0.04, 0.05, 0.06], 
    'min_samples_split': [5, 10, 15, 20],                
    'min_samples_leaf': [2, 3, 4, 5],                   
    'subsample': [0.7, 0.8, 0.9, 1.0]                 
}

param_grid = {
    'n_estimators': [100, 150, 200, 250, 300],      
    'max_depth': [2, 3, 4, 5],                     
    'learning_rate': [0.01, 0.05, 0.06, 0.1],         
    'min_samples_split': [10, 15, 20],                
    'min_samples_leaf': [3, 4, 5],              
    'subsample': [0.8, 0.9, 1.0]                     
}

# Aplicar GridSearchCV
grid_search = GridSearchCV(estimator=modelo_gb_interno, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)

# Treinar o modelo com o GridSearchCV
grid_search.fit(X_train, y_train_interno)

# Melhor conjunto de parâmetros encontrados
print(f'Melhor conjunto de parâmetros: {grid_search.best_params_}')

# Usar o melhor modelo encontrado
melhor_modelo_interno = grid_search.best_estimator_

# Fazer previsões
y_pred_gb_interno = melhor_modelo_interno.predict(X_test)

# Avaliar o desempenho
mse_gb_interno = mean_squared_error(y_test_interno, y_pred_gb_interno)
mae_gb_interno = mean_absolute_error(y_test_interno, y_pred_gb_interno)
r2_gb_interno = r2_score(y_test_interno, y_pred_gb_interno)

# Exibir os resultados
print(f'Resultados ajustados para Laborterapia Interna com Gradient Boosting (GridSearchCV):')
print(f'MSE: {mse_gb_interno}')
print(f'MAE: {mae_gb_interno}')
print(f'R²: {r2_gb_interno}')
