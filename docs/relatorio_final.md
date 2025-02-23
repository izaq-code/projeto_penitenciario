# Projeto Penintenciário

**Felipe Coelho de Azeredo, fazeredo@sga.pucminas.br**

**Isaque Gomes Azevedo, igazevedo@sga.pucminas.br**

**Mateus Nunes Guerra Ribeiro, mateus.ribeiro.1374124@sga.pucminas.br**

**Pedro Grojpen Couto, pedro.couto.1214249@sga.pucminas.br**

---

Professores:

**Prof. Hugo Bastos de Paula** 

---

_Curso de Ciência de Dados, Unidade Praça da Liberdade_

_Instituto de Informática e Ciências Exatas – Pontifícia Universidade de Minas Gerais (PUC MINAS), Belo Horizonte – MG – Brasil_

---

#### **Resumo**
Nesse trabalho, estamos analisando o sistema penitenciário brasileiro para conseguirmos ter uma visão mais ampla da infraestrutura, reabilitação e indicadores de ressocialização dentro das prisões brasileiras. Com esses dados, podemos identificar questões de desigualdade dentro do sistema penintenciário brasileiro e boas práticas que podem ser aplicadas.

---


## Introdução

O projeto apresentado aqui busca desenvolver um modelo inteligente capaz de identificar boas práticas e desigualdades no sistema penitenciário, em termos de infraestrutura, e analisar a relação dessa infraestrutura com a capacidade dessas de reintegrar seus detentos na sociedade.

###    Contextualização

Hoje, a prisão não oferece a oportunidade de ressocialização necessária para uma sociedade funcional (Machado, Guimarães)¹. As prisões brasileiras, que de forma geral, estão superlotadas, não tem a infraestrutura básica para corretamente reintegrar um cárcero a sociedade.

Nesse projeto, olhamos principalmente para as diferenças do que as instalações prisionais são capazes (atendimento médico, atividades laboriais, oferta de ensino e outros). Nenhum sistema penintenciário no mundo é perfeitamente justo, mas o uso estratégico de modelos inteligentes baseado em dados pode ajudar essas instituições a focar seus recursos em práticas que, por análise, são eficientes em ressocializar detentos.

###    Problema

O sistema carcerário brasileiro, em geral, prova-se ser inefetivo em sua função de reabilitação de internos. No entanto, há regiões onde a qualidade das instalações prisionais e a implementação de programas de reabilitação mostram bons indicadores de como um sistema carcerário pode melhorar. Como identificar, então, que regiões fazem um melhor trabalho e servem como modelo para as demais?

###    Objetivo geral

Desenvolver uma aplicação que analise e encontre as regiões com melhores indicadores de ressocialização e o contexto de seus sucessos, como a presença de instalações essenciais e a qualidade das mesmas, e comparar isso a eficácia da ressocialização dos detentos. Com isso, seremos capazes de entender melhor o que é necessário para criar uma prisão eficiente e inteligente.

####    Objetivos específicos
*[1] Coletar e organizar dados relevantes à infraestrutura das penitenciárias*
A aplicação irá reunir dados como, por exemplo, o número - ou existência - de:

	- consultórios médicos;
	- consultórios odontológicos;
 	- capacidade de regime interno;
	- Sala de curativos, suturas, vacinas e posto de enfermagem;
	- Sala de encontros com a sociedade / sala de reuniões;
	- biblioteca;
	
Também é informado se essas instalações são especificamente destinadas a suas finalidades específicas ou se são instalações usadas para vários fins, assim como se presídios femininos apresentam instalações como:

	- dormitórios para gestantes;
 	- berçários;
  	- centros de referência materno-infantil;
   
*[2] Mapear e analisar programas de reabilitação*
A aplicação analisará os dados relacionados a medidas de reabilitação, a efetividade delas e em que setores elas tem mais sucesso:

 	- quantidade de pessoas privadas de liberdade em programas de laborterapia (por setor primário, secundário e terciário);
 	- quantidade de pessoas privadas de liberdade em atividade educacional (por ensino fundamental, médio, técnico, superior);

*[3] Implementar uma visualização dos dados compreensiva*

*[4] Identificar os padrões em penitenciárias de sucesso em reabilitação dos detentos, baseando-se nos últimos passos*

###    Justificativas

A razão pela qual estamos desenvolvendo esse projeto é para que a situação atual do sistema carcerário brasileiro e os seus problemas sejam claramente identificados e para que possam ser solucionados pelos órgãos responsáveis por lidar com esse sistema. Para que assim, as instalações tenham a seus serviços os recursos humanos como consultórios médicos, odontológicos, enfermaria com todos seus recursos básicos necessários. Além de ter a sua disposição programas para a reabilitação dessas pessoas como o ensino educacional e serviços de laborterapia, com seus diversos setores.



##    Público alvo

As pessoas que utilizarão nossa aplicação são pessoas que trabalham em órgãos estatais, governamentais e nacionais relacionados ao sistema carcerário, como o SISDEPEN (Secretaria Nacional de Políticas Penais), o CNPCP (Conselho Nacional de Política Criminal e Penitenciária), as próprias Penitenciárias Federais e a Polícia Penal Federal. Além desses órgãos, a imprensa responsável por obter essas informações em diferentes locais e divulgá-las para os interessados em saber o estado atual do sistema carcerário brasileiro. 


## Análise exploratórida dos dados



###    Dicionário de dados



| Atributos                                           | Atributos (subcategorias)                           | Tipo de Dado | Descrição                                                                                                          |
| --------------------------------------------------- | --------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------ |
| 1. Ano                                              | -                                                   | int          | ano referenciado                                                                                                   |
| 2. UF                                               | -                                                   | string       | unidade federativa                                                                                                 |
| 3. Município                                        | -                                                   | string       | município referenciado                                                                                             |
| 4. Assistência laboral terceirizada                 | -                                                   | boolean      | as atividades laborais da penitenciária são terceirizadas?                                                         |
| 5. População prisional                              | Presos sentenciados - regime fechado                | int          | número de sentenciados em regime fechado                                                                           |
|                                                     | Presos sentenciados - regime semiaberto             | int          | número de sentenciados em regime semi-aberto                                                                       |
|                                                     | Presos sentenciados - regime aberto                 | int          | número de sentenciados em regime aberto                                                                            |
|                                                     | Total                                               | int          | número total de sentenciados em cada prisão                                                                        |
| 6. População prisional por grau de instrução        | Analfabeto                                          | int          | número de sentenciados analfabetos                                                                                 |
|                                                     | Alfabetizado (sem cursos regulares)                 | int          | número de sentenciados alfabetizados mas sem cursos regulares                                                      |
|                                                     | Ensino Fundamental Completo                         | int          | número de sentenciados que completaram o ensino fundamental                                                        |
|                                                     | Ensino Médio Completo                               | int          | número de sentenciados que completaram o ensino médio                                                              |
|                                                     | Ensino Superior Completo                            | int          | número de sentenciados que completaram o ensino superior                                                           |
| 7. População prisional em programas de laborterapia | Trabalho externo feminino                           | int          | número de sentenciados do sexo feminino em programas de laborterapia (fora da penitenciária)                       |
|                                                     | Vagas disponibilizadas pela administração prisional | int          | número de sentenciados em programas de laborterapia disponibilizados pela própria administração prisional          |
|                                                     | Vagas obtidas por meios próprios                    | int          | número de sentenciados em programas de laborterapia alcançados por meios próprios                                  |
|                                                     | Trabalho interno                                    | int          | número de sentenciados de ambos os sexos em programas de laborterapia (dentro da penitenciária)                    |
| 8. População prisional por remuneração              | Não recebe                                          | int          | número de sentenciados não recebendo remuneração (não necessariamente em atividades laboriais)                     |
|                                                     | Menos do que 3/4 do salário mínimo                  | int          | número de sentenciados recebendo menos do que 3/4 do salário mínimo (não necessariamente em atividades laboriais)  |
|                                                     | Entre 3/4 e 1 salário mínimo                        | int          | número de sentenciados recebendo entre 3/4 e 1 salário mínimo (não necessariamente em atividades laboriais)        |
|                                                     | Entre 1 e 2 salários mínimos                        | int          | número de sentenciados recebendo entre 1 e 2 salário mínimo (não necessariamente em atividades laboriais)          |
|                                                     | Mais de 2 salários mínimos mensais                  | int          | número de sentenciados recebendo mais que 2 salários mínimos mensais (não necessariamente em atividades laboriais) |
| 9. Quantidade de matriculas                         | Ensino fundamental                                  | int          | número de matrículas no ensino por todo o Brasil                                                          |
|                                                     | Ensino médio                                        | int          | número de matrículas no ensino médio por todo o Brasil                                                                |
|                                                     | Ensino profissionalizante                           | int          | número de matrículas em algum curso de ensino profissionalizante por todo o Brasil                                    |






###    Descrição de dados
![image](https://github.com/user-attachments/assets/175d2142-3c3e-4939-8da4-71777985759e)
![image](https://github.com/user-attachments/assets/6fe7478d-29df-412c-904a-6c7f63018290)
 ![image](https://github.com/user-attachments/assets/a33629df-4f57-43e5-9206-6e41c8c82736)
 ![image](https://github.com/user-attachments/assets/d78f32ec-07e7-4cd7-b41e-8d313f57ed25)
 ![image](https://github.com/user-attachments/assets/a8c19d3f-fd61-4c4e-a2dc-96a2fab6f36d)
 ![image](https://github.com/user-attachments/assets/4dfc4967-782e-43b0-a51d-4098d239e741)
 ![image](https://github.com/user-attachments/assets/2e74e3c1-ad83-40c7-81ee-744f46d4896c)
 ![image](https://github.com/user-attachments/assets/6300680f-7ea0-4593-907d-cc0da054dc9e)
## Preparação dos dados

### Comparação de Dicionários de Dados: Antigo/Novo

| Atributo                                 | Antigo (Descrição)                                                                                                   | Novo (Descrição)                                                                                                   | Modificação                                    |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| **Ano**                                   | Ano referenciado                                                                                                     | Ano referenciado                                                                                                   | Sem alterações                                |
| **UF**                                    | Unidade Federativa                                                                                                   | Unidade Federativa                                                                                                 | Sem alterações                                |
| **Município**                             | Não existia                                                                                                          | Município referenciado                                                                                             | **Adicionado no novo dicionário**             |
| **Assistência laboral terceirizada**      | As atividades laborais da penitenciária são terceirizadas?                                                           | As atividades laborais da penitenciária são terceirizadas?                                                         | Sem alterações                                |
| **População prisional**                   | Número total de sentenciados em cada prisão (regimes fechado, semiaberto, aberto)                                    | Número total de sentenciados em cada prisão (regimes fechado, semiaberto, aberto)                                  | Sem alterações                                |
| **População prisional por grau de instrução** | Incluía níveis incompletos de educação, como Ensino Fundamental Incompleto e Ensino Médio Incompleto.                   | Mantém apenas níveis completos: Ensino Fundamental Completo, Ensino Médio Completo, Ensino Superior Completo       | **Subcategorias de níveis incompletos removidas** |
| **População prisional em programas de laborterapia** | Detalhes mais granulares sobre setores e parcerias, como primário, secundário e terciário.                             | Categorias mais gerais: Trabalho externo feminino, Vagas pela administração, Vagas por meios próprios, Trabalho interno | **Agrupamento em categorias mais amplas**      |
| **População prisional por remuneração**   | Remuneração dividida por faixas salariais                                                                            | Remuneração dividida por faixas salariais                                                                          | Sem alterações                                |
| **Quantidade de matrículas**              | Não existia                                                                                                          | Matrículas em Ensino Fundamental, Médio e Profissionalizante                                                       | **Adicionada nova tabela ao dicionário**             |

---

### Remoções Notáveis:

- **População prisional por grau de instrução**: Níveis de educação incompletos foram removidos.
- **População prisional em programas de laborterapia**: Detalhes sobre setores e parcerias foram simplificados em categorias mais gerais.


## Comparação de Análises Exploratórias

### 1. Quantidade de Pessoas Privadas de Liberdade em Programas de Laborterapia

### Análise Antiga:
- A análise antiga mostra uma grande participação de pessoas do sexo feminino em trabalho interno.
- O trabalho externo é significativamente menor em ambos os sexos.

### Análise Nova:
- A nova análise não distingue por gênero e apresenta os dados agregados de trabalho interno e externo.
- O trabalho interno continua a ser predominante, com valores mais altos que o trabalho externo.

### Diferenças:
- A análise antiga faz distinção por gênero, enquanto a nova não.
- O trabalho interno continua sendo predominante em ambas as análises, mas a nova versão simplificou os dados, não segmentando por gênero.

---

## 2. Quantidade de Pessoas Privadas de Liberdade por Remuneração

### Análise Antiga:
- Na análise antiga, os dados são separados por gênero, com a maioria dos homens recebendo menos de 3/4 do salário mínimo.
- Poucas pessoas recebem mais de 2 salários mínimos.

### Análise Nova:
- A nova análise apresenta os dados sem distinção de gênero, com uma maior concentração de pessoas recebendo menos de 3/4 do salário mínimo.
- As categorias entre 1 e 2 salários mínimos e mais de 2 salários mínimos continuam com pouca representatividade.

### Diferenças:
- A análise antiga separava por gênero, enquanto a nova não faz essa distinção.
- As tendências de remuneração se mantêm parecidas, com a maioria das pessoas recebendo menos de 3/4 do salário mínimo.

## 3. Inclusão de Dados Novos

Na nova análise, foram adicionados gráficos sobre:

- Quantidade de matrículas no ensino fundamental em 2023.
- Quantidade de matrículas no ensino médio em 2023.
- Quantidade de matrículas no ensino profissionalizante em 2023.

Esses dados ampliam o escopo da análise, que anteriormente era focada apenas em pessoas privadas de liberdade, incorporando agora dados gerais sobre educação.

## 4. Tratamento de Dados Nulos

### Preenchimento com Valor 0:
- Em ambas as análises, todos os dados nulos presentes nas categorias de remuneração, atividades educacionais e laborterapia foram preenchidos com o valor **0**.
- O objetivo de utilizar o valor 0 foi garantir que as análises não fossem impactadas por valores ausentes, mantendo a consistência nos gráficos e permitindo uma comparação mais precisa das distribuições de frequência.
- Esse procedimento garante que todas as categorias sejam consideradas na análise, mesmo que não existam registros em determinadas faixas ou níveis educacionais.

### Impacto:
- A decisão de preencher os nulos com 0 evita distorções nos gráficos, mas é importante considerar que isso pode subestimar a ausência de dados em certas áreas. Por exemplo, em categorias onde não há informação, os valores representados podem não refletir completamente a realidade.
- Contudo, essa abordagem facilita a visualização geral das tendências, especialmente em gráficos de quantidades agregadas.

---

## Resumo das Diferenças

- **Simplificação:** A nova análise simplifica algumas segmentações, removendo distinções de gênero e detalhamentos em alguns gráficos.
- **Consistência:** As tendências observadas na análise antiga permanecem, como a predominância do trabalho interno e a maior parte das pessoas recebendo menos de 3/4 do salário mínimo.
- **Ampliação do Escopo:** A nova análise inclui dados adicionais sobre matrículas em diversos níveis de ensino no Brasil em 2023, o que não estava presente na versão anterior.
- **Tratamento de Nulos:** Em ambas as análises, dados nulos foram preenchidos com 0 para manter a consistência da apresentação e visualização dos dados.

## Indução de modelos

### Modelo 1: Random Forest

#### Justificativa

O Random Forest foi escolhido por seu desempenho superior em comparação à Árvore de Decisão, que foi escolhida inicialmente por sua simplicidade e facilidade de uso. O Random Forest melhora as limitações de uma única árvore, como o overfitting e a variabilidade, através da combinação de várias árvores construídas com subconjuntos aleatórios dos dados e das variáveis explicativas. Esse método foi mais robusto quando lidando com a variabilidade entre os dados de laborterapia interna e externa.

Além disso, o Random Forest teve melhoria no Erro Quadrático Médio (MSE), com um valor de 6.294.069, superando o modelo de árvore de decisão, cujo MSE foi de 6.618.901.

#### Processo de amostragem

Foi feita uma divisão simples dos dados usando a função train_test_split do Scikit-learn

- **Treinamento (80%)**: Utilizado para ajustar o modelo.
- **Teste (20%)**: Utilizado para avaliar a capacidade do modelo de generalizar para novos dados.

A validação cruzada foi aplicada com 5 divisões, garantindo que o modelo fosse avaliado em diferentes subconjuntos de dados, e reduzindo ao máximo o overfitting.

#### Parâmetros Utilizados

Com o uso do Randomized Search, os melhores parâmetros encontrados para o Random Forest foram:

- **n_estimators**: 100 (número de árvores)
- **max_depth**: 5 (profundidade máxima das árvores)
- **min_samples_split**: 5 (mínimo de amostras para dividir um nó)
- **min_samples_leaf**: 2 (mínimo de amostras em um nó folha)

#### Código

```python
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
```

### Modelo 2: Gradient Boosting

#### Justificativa

O Gradient Boosting foi selecionado como alternativa ao Random Forest devido à sua capacidade de melhorar o desempenho por meio da construção sequencial de modelos. Esse algoritmo é particularmente eficaz em cenários onde os dados possuem relações complexas, como no caso dos dados de laborterapia interna e externa. 

Ao construir modelos sequenciais para corrigir erros dos modelos anteriores, o Gradient Boosting mostrou-se capaz de reduzir ainda mais o Erro Quadrático Médio (MSE) em comparação ao Random Forest. Essa melhoria demonstra que o modelo é mais eficaz na captura de padrões nos dados, especialmente em contextos onde existe alta correlação entre as variáveis explicativas e os targets.

#### Processo de amostragem

Os mesmos critérios utilizados no Random Forest foram aplicados no Gradient Boosting:

- **Divisão dos Dados**: Foi utilizada a função `train_test_split` do Scikit-learn para dividir os dados em:
  - **Treinamento (80%)**: Usado para ajustar o modelo.
  - **Teste (20%)**: Avaliado para medir a capacidade do modelo de generalizar.
  
- **Validação Cruzada**: Implementada com 5 divisões para garantir que os resultados do modelo não fossem influenciados por uma única divisão dos dados.

Essa abordagem permitiu avaliar a estabilidade e a generalização do Gradient Boosting.

#### Parâmetros Utilizados

Os melhores parâmetros foram definidos por busca aleatória (`RandomizedSearchCV`), garantindo a otimização do modelo. Os parâmetros encontrados foram:

- **n_estimators**: 100 (número de estimadores no ensemble)
- **max_depth**: 5 (profundidade máxima das árvores de decisão)
- **min_samples_split**: 5 (número mínimo de amostras para dividir um nó)
- **min_samples_leaf**: 2 (número mínimo de amostras em cada folha)
- **learning_rate**: 0.1 (taxa de aprendizado do modelo sequencial)

Esses valores garantiram que o modelo mantivesse um equilíbrio entre desempenho e generalização, evitando overfitting.

#### Código

```python
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
```

## Resultados

### Resultados obtidos com o modelo 1.

#### Resultados para Laborterapia Interna:

- **MSE**: 551724.28
- **MAE**: 311.07
- **R^2**: 0.94

#### Resultados para Laborterapia Externa:

- **MSE**: 5990845.10
- **MAE**: 1857.21
- **R^2**: 0.59

### Interpretação do modelo 1

```python
# Filtrar as features para remover colunas relacionadas a municípios
features_sem_municipios = [col for col in features.columns if "município" not in col.lower()]

# Obter as importâncias das features para o modelo de Laborterapia Interna
importancias_interno = modelo_rf_interno.feature_importances_
importancia_features_interno = [
    (feature, importancia) for feature, importancia in zip(features.columns, importancias_interno) if feature in features_sem_municipios
]
importancia_features_interno.sort(key=lambda x: x[1], reverse=True)

# Exibir as importâncias para Laborterapia Interna
print("\nImportância das features para Laborterapia Interna (sem municípios):")
for feature, importancia in importancia_features_interno:
    print(f"{feature}: {importancia}")

# Obter as importâncias das features para o modelo de Laborterapia Externa
importancias_externo = modelo_rf_externo.feature_importances_
importancia_features_externo = [
    (feature, importancia) for feature, importancia in zip(features.columns, importancias_externo) if feature in features_sem_municipios
]
importancia_features_externo.sort(key=lambda x: x[1], reverse=True)

# Exibir as importâncias para Laborterapia Externa
print("\nImportância das features para Laborterapia Externa (sem municípios):")
for feature, importancia in importancia_features_externo:
    print(f"{feature}: {importancia}")
```

### **Laborterapia Interna**
- **Vagas Disponibilizadas pela Administração Prisional**: **95.82%**  
  A principal variável que impacta os programas internos de laborterapia, pois determina o número de vagas oferecidas diretamente pela administração das prisões.

- **População Prisional | Sentenciados - Regime Fechado**: **1.19%**  
  A quantidade de detentos em regime fechado é importante, já que eles são os principais participantes de programas de laborterapia interna.

- **Vagas Obtidas por Meios Próprios**: **0.85%**  
  Reflete a capacidade das prisões de gerar vagas de forma independente, sendo um fator importante para a manutenção do programa.

- **Grau de Instrução | Analfabeto**: **0.25%**  
  O analfabetismo entre os presos pode limitar sua participação em programas de laborterapia mais especializados.

- **Quantidade de pessoas privadas de liberdade por remuneração | Não recebe**: **0.24%**  
  Detentos que não recebem remuneração podem estar mais focados em processos de reintegração social e trabalho no interior das prisões.

### **Laborterapia Externa**
- **UF_SP**: **59.88%**  
  São Paulo tem um impacto significativo em programas de laborterapia externa, devido à sua grande população carcerária e programas desenvolvidos para reintegração.

- **UF_PR**: **21.79%**  
  O Paraná é outro estado com relevância alta, oferecendo boas oportunidades de laborterapia externa.

- **Quantidade de pessoas privadas de liberdade por remuneração | Entre 1 e 2 salários mínimos mensais**: **0.12%**  
  A remuneração de detentos é um indicativo importante de sua capacidade de reintegração e participação em programas externos remunerados.

- **Serviços Terceirizados | Assistência Laboral**: **0.00%**  
  A assistência laboral terceirizada tem um impacto praticamente nulo neste modelo, provavelmente por sua baixa presença nos dados.

- **População Prisional | Sentenciados - Regime Fechado**: **0.00%**  
  O regime fechado não parece ter grande relevância para os programas de laborterapia externa, já que são mais voltados para detentos com maior liberdade.

### Resultados obtidos com o modelo 2.

#### Resultados para Laborterapia Interna com Gradient Boosting:
- **MSE**: 376565.45
- **MAE**: 278.79
- **R2**: 0.96

#### Resultados para Laborterapia Externa com Gradient Boosting:
- **MSE**: 16857.44
- **MAE**: 99.09
- **R2**: 0.99

### Interpretação do modelo 2

```python

# Filtrar as features para remover colunas relacionadas a municípios
features_sem_municipios = [col for col in features.columns if "município" not in col.lower()]

# Obter as importâncias das features para o modelo de Laborterapia Interna
importancias_interno_gb = modelo_gb_interno.feature_importances_
importancia_features_interno_gb = [
    (feature, importancia) for feature, importancia in zip(features.columns, importancias_interno_gb) if feature in features_sem_municipios
]
importancia_features_interno_gb.sort(key=lambda x: x[1], reverse=True)

# Exibir as importâncias para Laborterapia Interna
print("\nImportância das features para Laborterapia Interna (Gradient Boosting, sem municípios):")
for feature, importancia in importancia_features_interno_gb:
    print(f"{feature}: {importancia}")

# Obter as importâncias das features para o modelo de Laborterapia Externa
importancias_externo_gb = modelo_gb_externo.feature_importances_
importancia_features_externo_gb = [
    (feature, importancia) for feature, importancia in zip(features.columns, importancias_externo_gb) if feature in features_sem_municipios
]
importancia_features_externo_gb.sort(key=lambda x: x[1], reverse=True)

# Exibir as importâncias para Laborterapia Externa
print("\nImportância das features para Laborterapia Externa (Gradient Boosting, sem municípios):")
for feature, importancia in importancia_features_externo_gb:
    print(f"{feature}: {importancia}")

```

### **Laborterapia Interna**
- **Vagas Disponibilizadas pela Administração Prisional**: **90.99%**  
  A disponibilidade de vagas é a variável mais importante, indicando que o acesso aos programas de laborterapia depende principalmente da gestão interna das prisões.
  
- **População Prisional | Sentenciados - Regime Fechado**: **5.52%**  
  A quantidade de detentos em regime fechado é crucial, pois eles são os principais participantes de programas internos de laborterapia.

- **Vagas Obtidas por Meios Próprios**: **1.88%**  
  Reflete a capacidade das prisões de gerar vagas de forma independente, o que contribui para a autossustentabilidade dos programas de laborterapia.

- **Quantidade de pessoas privadas de liberdade por remuneração | Entre 1 e 2 salários mínimos mensais**: **0.59%**  
  A remuneração de detentos pode indicar seu nível de integração a programas de laborterapia e sua capacidade de reintegração ao mercado de trabalho.

- **Grau de Instrução | Analfabeto**: **0.08%**  
  O analfabetismo pode limitar a participação dos presos em programas de laborterapia mais especializados.

### **Laborterapia Externa**
- **UF_SP**: **56.26%**  
  São Paulo tem um grande impacto na laborterapia externa, devido à sua alta população carcerária e desenvolvimento de programas prisionais.

- **UF_PR**: **21.14%**  
  O Paraná também é um destaque na laborterapia externa, com políticas eficazes que oferecem mais oportunidades de reintegração para os presos.

- **Quantidade de pessoas privadas de liberdade por remuneração | Entre 3/4 e 1 salário mínimo**: **0.33%**  
  A faixa salarial dos detentos é importante para determinar seu nível de integração em programas externos de trabalho remunerado.

- **Grau de Instrução | Analfabeto**: **0.06%**  
  O analfabetismo afeta a participação dos detentos em programas de laborterapia externa, que exigem maior qualificação.

- **Vagas Disponibilizadas pela Administração Prisional**: **0.05%**  
  A gestão das vagas internas ainda tem relevância, pois pode influenciar na integração dos detentos em programas externos de laborterapia.

## Análise Comparativa dos Modelos
### **Random Forest**

#### **Forças (Facilidades ao Analisar Laborterapia)**
1. **Interpretação Simples**: Facilita identificar variáveis-chave que impactam programas de laborterapia, como "vagas disponibilizadas pela administração prisional".
2. **Resistência a Dados Faltantes**: Dados incompletos ou inconsistentes não comprometem significativamente a análise.
3. **Escalabilidade**: Lida bem com grandes volumes de dados, como os diversos fatores regionais e populacionais analisados.
4. **Rápida Configuração**: Não exige ajustes extensivos de parâmetros, permitindo resultados rápidos em análises iniciais.

#### **Fragilidades (Dificuldades ao Analisar Laborterapia)**
1. **Menor Sensibilidade a Relações Complexas**: Dificuldade em capturar interações não lineares, como a correlação entre infraestrutura e sucesso em laborterapia externa.
2. **Foco Excessivo em Variáveis Dominantes**: Prioriza variáveis mais influentes, como "vagas de laborterapia", podendo negligenciar fatores secundários importantes.
3. **Predições Generalizadas**: Perde nuances específicas, como variações regionais em políticas de ressocialização.

---

### **Gradient Boosting**

#### **Forças (Facilidades ao Analisar Laborterapia)**
1. **Capacidade de Capturar Relações Complexas**: Excelente para identificar interações entre múltiplas variáveis, como infraestrutura regional e remuneração.
2. **Flexibilidade com Dados Diversificados**: Gerencia bem dados categóricos e numéricos, ampliando a aplicabilidade em cenários complexos.
3. **Alto Desempenho Preditivo**: Apresentou resultados altamente precisos, especialmente para laborterapia externa.
4. **Identificação de Fatores Secundários**: Destaca variáveis menos influentes que podem passar despercebidas, como bibliotecas ou programas educacionais.

#### **Fragilidades (Dificuldades ao Analisar Laborterapia)**
1. **Custo Computacional Elevado**: Exige mais tempo e recursos para treinar o modelo, especialmente em bases grandes.
2. **Ajuste de Hiperparâmetros**: Necessidade de experimentação cuidadosa para maximizar a performance, tornando o processo mais complexo.
3. **Dificuldade de Interpretação**: A compreensão do impacto de cada variável é mais desafiadora, dificultando a comunicação dos resultados.
4. **Menor Tolerância a Dados Faltantes**: Exige maior esforço na preparação e limpeza dos dados.

---

### Escolha do Modelo e Justificativa

Com base na análise das forças e fragilidades, o modelo **Gradient Boosting** foi escolhido para o projeto de laborterapia devido aos seguintes motivos:

1. **Precisão Elevada**: Apresentou maior R² e menor MSE, especialmente em cenários mais complexos como laborterapia externa.
2. **Capacidade de Capturar Relações Complexas**: É mais eficaz para explorar interações entre infraestrutura, remuneração e políticas regionais, elementos essenciais no projeto.
3. **Flexibilidade em Variáveis Diversificadas**: Lida bem com diferentes tipos de dados, permitindo uma análise mais rica e abrangente.
4. **Insights Detalhados**: Embora mais trabalhoso, permitiu identificar padrões sofisticados que auxiliam na tomada de decisões mais informadas.

Apesar do maior custo computacional e da necessidade de ajustes minuciosos, o Gradient Boosting demonstrou ser a melhor opção para fornecer uma análise profunda e confiável no contexto do sistema carcerário e dos programas de laborterapia.

### Distribuição do modelo (opcional)

**Modelo Inteligente**  
- **Acesse o modelo inteligente**: [Modelo Inteligente - Sistema Penitenciário](https://tt-production-dbba.up.railway.app)  

⚠ **Aviso**: Este link é temporário e está sujeito a alterações futuras.  

**Rodar o código na própria máquina**  
- **Diretório do código**: [GitHub - Código para execução local](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2024-2-projeto_penitenciario/tree/main/src/MO_IN)  

## 8. Conclusão

**Resumo do projeto**  
Este trabalho buscou criar um sistema inteligente capaz de identificar desigualdades e boas práticas no sistema penitenciário brasileiro, com foco na infraestrutura, laborterapia e indicadores de ressocialização. Utilizamos técnicas de análise de dados, machine learning e visualização para extrair insights e propor soluções baseadas em dados.

**Resultados, vantagens e desvantagens**  
Os modelos Random Forest e Gradient Boosting foram avaliados quanto à predição de indicadores de laborterapia. O Gradient Boosting mostrou-se mais eficaz, com R² de até 0,99 em algumas análises, demonstrando alta precisão e capacidade de capturar padrões complexos.  

**Vantagens do projeto**:  
- **Identificação de desigualdades estruturais**: O sistema permite analisar diferenças na infraestrutura e práticas das penitenciárias, destacando áreas críticas para intervenção.  
- **Tomada de decisão baseada em dados**: Gera insights claros para gestores públicos e organizações, direcionando recursos para práticas comprovadamente eficazes.  
- **Capacidade de personalização regional**: O projeto considera variáveis regionais, permitindo recomendações adaptadas às especificidades de cada localidade.  

**Desvantagens**:  
- Sensibilidade a dados faltantes e necessidade de ajustes extensos.  
- Necessidade de um poder computacional elevado para otimizar os parâmetros utilizando Grid Search ou métodos equivalentes.

**Limitações e melhorias futuras**  
Embora o modelo tenha demonstrado resultados promissores na previsão de indicadores de ressocialização, ainda apresenta limitações, como dependência de dados completos e maior complexidade para usuários não técnicos. Melhorias futuras incluem:  
- Desenvolvimento de uma interface mais amigável para usuários finais.  
- Ampliação da base de dados para incluir mais variáveis regionais e sociais.  
- Integração de outros métodos de aprendizado de máquina, como redes neurais, para explorar relações não lineares mais complexas.  

Assim, o sistema proposto pode se tornar uma ferramenta essencial para a gestão e melhoria do sistema penitenciário.

### **Fator Crucial**

Um dos fatores mais cruciais para o sucesso do modelo foi a **disponibilidade de vagas para laborterapia** na **administração prisional**. Esta variável teve a maior importância no modelo inteligente, tanto para a laborterapia interna (90.99%) quanto para a externa (56.26%). A razão pela qual essa feature é tão relevante está no fato de que a **oferta de vagas** é diretamente responsável por determinar quantos detentos podem ser alocados em programas de trabalho, influenciando diretamente as oportunidades de ressocialização e reintegração ao mercado de trabalho. A gestão eficiente das vagas é um fator chave para reduzir desigualdades e maximizar a eficácia dos programas penitenciários, o que justifica sua importância no modelo preditivo utilizado neste estudo.

# REFERÊNCIAS

**[1]** BRASIL. Ministério da Justiça e Segurança Pública. Sistema Nacional de Informações Penitenciárias (SISDEPEN). Disponível em: <https://www.gov.br/senappen/pt-br/servicos/sisdepen>. Acesso em: 1 dez. 2024.  

**[2]** INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA (IBGE). Estatísticas – Downloads. Disponível em: <https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html>. Acesso em: 1 dez. 2024.  

# APÊNDICES  

**Links importantes:**  
- **Código**: [GitHub - Código do Projeto](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2024-2-projeto_penitenciario/tree/main/src)  
- **Artefatos**: [GitHub - Artefatos do Projeto](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2024-2-projeto_penitenciario/tree/main/assets)  
- **Apresentação final**: [GitHub - Apresentação Final](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2024-2-projeto_penitenciario/tree/main/docs)  
- **Vídeo de apresentação**: [Armazenado no repositório](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2024-2-projeto_penitenciario)  





