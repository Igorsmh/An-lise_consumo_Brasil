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
groupAno.drop(axis=1,columns = ['mes','numero_consumidores'],inplace = True)

ano = groupAno['ano']
# consumo em Gigawatt-hora
consumo_tot = (groupAno['consumo']/1000).astype('int64')

plt.title("Gráfico do consumo de energia por ano")
plt.xlabel("Ano")
plt.ylabel("Consumo em GWh")
plt.scatter(ano,consumo_tot)
plt.show()


# Consumo por anos em porcentagem

plt.title("Gráfico do consumo de energia por estado")
plt.xlabel("Estado")
plt.ylabel("Consumo")



plt.scatter(ano,consumo_por )
plt.plot(ano, consumo_por)
plt.show()

# Comparação do consumo de energia elétrica por estado e região

groupUf = df.groupby(df['sigla_uf']).sum()
groupUf = groupUf.reset_index()

print(groupUf)

# Consumo de cada estado de 2004 a 2021
sigla_uf = groupUf['sigla_uf']
consumo_estado = groupUf['consumo']

plt.title("Gráfico do consumo de energia por estado")
plt.xlabel("Estado")
plt.ylabel("Consumo")

plt.bar(sigla_uf, consumo_estado)
plt.show()

# Análise da relação entre o consumo de energia elétrica e o PIB (Produto Interno Bruto)







# Análise do impacto do uso de fontes de energia renováveis no consumo de energia elétrica
# Análise da eficiência energética em diferentes setores da economia brasileira.