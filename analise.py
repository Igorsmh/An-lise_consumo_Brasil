import basedosdados as bd
import matplotlib.pyplot as plt
import pandas as pd
# Para carregar o dado direto no pandas
df = bd.read_table(dataset_id='br_mme_consumo_energia_eletrica',
                   table_id='uf', billing_project_id="robust-slice-376003")

print(df.info())

# Evolução do consumo de energia elétrica no Brasil nos últimos 10 anos

groupAno = df.groupby(df['ano']).sum()
groupAno = groupAno.reset_index()
groupAno.drop(axis=1, columns=['mes', 'numero_consumidores'], inplace=True)

# consumo em Gigawatt-hora e inteiro para facilitar
groupAno['consumo'] = (groupAno['consumo']/1000).astype('int64')


plt.title("Gráfico do consumo de energia por ano")
plt.xlabel("Ano")
plt.ylabel("Consumo em GWh")
plt.scatter(groupAno['ano'], groupAno['consumo'])
plt.show()


# Consumo por anos em porcentagem



# Comparação do consumo de energia elétrica por estado e região


# Consumo de cada estado de 2004 a 2021


# Análise da relação entre o consumo de energia elétrica e o PIB (Produto Interno Bruto)


# Análise do impacto do uso de fontes de energia renováveis no consumo de energia elétrica
# Análise da eficiência energética em diferentes setores da economia brasileira.
