# Importar bibliotecas necessárias
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd
import os

# Carregar a planilha de dados
file_path_updated = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'final_processed_SISDEPEN_IBGE.xlsx')
df_updated = pd.read_excel(file_path_updated, sheet_name='Sheet1')

# One-Hot Encoding para transformar variáveis categóricas em numéricas
df_encoded = pd.get_dummies(df_updated)

# Selecionar as variáveis explicativas (excluindo os targets)
features = df_encoded.drop(columns=['6.1 Laborterapia | Trabalho Interno | Total', 
                                    '6.1 Laborterapia | Trabalho Externo | Total'])

# Selecionar as variáveis-alvo (targets) separadamente
target_interno = df_encoded['6.1 Laborterapia | Trabalho Interno | Total']
target_externo = df_encoded['6.1 Laborterapia | Trabalho Externo | Total']

# Dividir os dados em treino e teste para as features e ambos os targets
X_train, X_test, y_train_interno, y_test_interno, y_train_externo, y_test_externo = train_test_split(
    features, target_interno, target_externo, test_size=0.2, random_state=42
)

# Configurar um modelo de Random Forest para cada target
modelo_rf_interno = RandomForestRegressor(n_estimators=100, max_depth=5, min_samples_split=5, min_samples_leaf=2, random_state=42)
modelo_rf_externo = RandomForestRegressor(n_estimators=100, max_depth=5, min_samples_split=5, min_samples_leaf=2, random_state=42)

# Treinar os modelos com os dados de treino
modelo_rf_interno.fit(X_train, y_train_interno)
modelo_rf_externo.fit(X_train, y_train_externo)

# Fazer previsões no conjunto de teste para cada target
y_pred_interno = modelo_rf_interno.predict(X_test)
y_pred_externo = modelo_rf_externo.predict(X_test)

# Avaliar o desempenho dos modelos com MSE, MAE e R²
mse_rf_interno = mean_squared_error(y_test_interno, y_pred_interno)
mae_rf_interno = mean_absolute_error(y_test_interno, y_pred_interno)
r2_rf_interno = r2_score(y_test_interno, y_pred_interno)

mse_rf_externo = mean_squared_error(y_test_externo, y_pred_externo)
mae_rf_externo = mean_absolute_error(y_test_externo, y_pred_externo)
r2_rf_externo = r2_score(y_test_externo, y_pred_externo)

# Apresentar os resultados para Laborterapia Interna e Externa
print(f'Resultados para Laborterapia Interna:')
print(f'MSE: {mse_rf_interno}')
print(f'MAE: {mae_rf_interno}')
print(f'R²: {r2_rf_interno}')

print(f'\nResultados para Laborterapia Externa:')
print(f'MSE: {mse_rf_externo}')
print(f'MAE: {mae_rf_externo}')
print(f'R²: {r2_rf_externo}')