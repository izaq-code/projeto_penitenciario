# Importar bibliotecas necessárias
from sklearn.ensemble import GradientBoostingRegressor
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

# Dividir os dados em treino e teste para cada target
X_train, X_test, y_train_interno, y_test_interno = train_test_split(features, target_interno, test_size=0.2, random_state=42)
_, _, y_train_externo, y_test_externo = train_test_split(features, target_externo, test_size=0.2, random_state=42)

# Configurar modelos de Gradient Boosting para cada target
modelo_gb_interno = GradientBoostingRegressor(
    n_estimators=150,          
    max_depth=2,              
    min_samples_split=20,      
    min_samples_leaf=5,       
    learning_rate=0.06,      
    random_state=42
)

# Configurar o modelo de Gradient Boosting para Laborterapia Externa
modelo_gb_externo = GradientBoostingRegressor(
    n_estimators=100, 
    max_depth=5, 
    min_samples_split=5, 
    min_samples_leaf=2, 
    random_state=42
)

# Treinar os modelos Gradient Boosting com os dados de treino
modelo_gb_interno.fit(X_train, y_train_interno)
modelo_gb_externo.fit(X_train, y_train_externo)

# Fazer previsões no conjunto de teste para cada target com Gradient Boosting
y_pred_gb_interno = modelo_gb_interno.predict(X_test)
y_pred_gb_externo = modelo_gb_externo.predict(X_test)

# Avaliar o desempenho dos modelos Gradient Boosting
mse_gb_interno = mean_squared_error(y_test_interno, y_pred_gb_interno)
mae_gb_interno = mean_absolute_error(y_test_interno, y_pred_gb_interno)
r2_gb_interno = r2_score(y_test_interno, y_pred_gb_interno)

mse_gb_externo = mean_squared_error(y_test_externo, y_pred_gb_externo)
mae_gb_externo = mean_absolute_error(y_test_externo, y_pred_gb_externo)
r2_gb_externo = r2_score(y_test_externo, y_pred_gb_externo)

# Exibir os resultados
print(f'Resultados para Laborterapia Interna com Gradient Boosting:')
print(f'MSE: {mse_gb_interno}')
print(f'MAE: {mae_gb_interno}')
print(f'R²: {r2_gb_interno}\n')

print(f'Resultados para Laborterapia Externa com Gradient Boosting:')
print(f'MSE: {mse_gb_externo}')
print(f'MAE: {mae_gb_externo}')
print(f'R²: {r2_gb_externo}')

import matplotlib.pyplot as plt

# Configurar o layout do gráfico
plt.figure(figsize=(14, 6))

# Gráfico para Laborterapia Interna com Gradient Boosting
plt.subplot(1, 2, 1)
plt.scatter(y_test_interno, y_pred_gb_interno, alpha=0.7, color='cornflowerblue', edgecolor='k')
plt.plot([y_test_interno.min(), y_test_interno.max()], [y_test_interno.min(), y_test_interno.max()], 'r--')
plt.title('Previsão vs Real (Interno - Gradient Boosting)')
plt.xlabel('Valores Reais')
plt.ylabel('Valores Previstos')
plt.grid(True)

# Gráfico para Laborterapia Externa com Gradient Boosting
plt.subplot(1, 2, 2)
plt.scatter(y_test_externo, y_pred_gb_externo, alpha=0.7, color='mediumseagreen', edgecolor='k')
plt.plot([y_test_externo.min(), y_test_externo.max()], [y_test_externo.min(), y_test_externo.max()], 'r--')
plt.title('Previsão vs Real (Externo - Gradient Boosting)')
plt.xlabel('Valores Reais')
plt.ylabel('Valores Previstos')
plt.grid(True)

plt.tight_layout()
plt.show()
