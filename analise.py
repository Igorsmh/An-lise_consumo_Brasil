import basedosdados as bd
import matplotlib.pyplot as plt
import pandas as pd

# Para carregar o dado direto no pandas
df = bd.read_table(dataset_id='br_mme_consumo_energia_eletrica',
                   table_id='uf', billing_project_id="robust-slice-376003")

print(df.info())


# Evolução do consumo de energia elétrica no Brasil 

group_consumo_ano = df.groupby(df['ano'])['consumo'].agg([sum, 'mean'])
group_consumo_ano = group_consumo_ano.reset_index()


plt.title("Gráfico do consumo de energia consumida por ano")
plt.xlabel("Ano")
plt.ylabel("Consumo em MWh")
plt.plot(group_consumo_ano['ano'], group_consumo_ano['sum'])
plt.scatter(data=group_consumo_ano, x="ano", y="sum")
plt.show()


plt.title("Gráfico da média de consumo a cada ano")
plt.xlabel("Ano")
plt.ylabel("Consumo Médio em MWh")
plt.bar(group_consumo_ano['ano'], group_consumo_ano['mean'])
plt.show()


# verificar alteração no consumo por quantidade de consumidores

consumi_ano = df.groupby(by=['ano']).agg(
    Consumidores=('numero_consumidores', sum))
consumi_ano.reset_index(inplace=True)
consumi_ano.fillna(0, inplace=True)


plt.bar(group_consumo_ano['ano'], group_consumo_ano['sum'], label='Consumo')
plt.bar(consumi_ano['ano'], consumi_ano['Consumidores'],
        label='Número de consumidores')


plt.xlabel('Anos')
plt.ylabel('Número de consumidores / Consumo')
plt.title('Evolução do número de consumidores e consumo ao longo dos anos')
plt.legend()

plt.show()

# Comparação do consumo de energia elétrica por estado e região

consumo_por_regiao = pd.pivot_table(df,index = 'ano',columns = 'sigla_uf',values='consumo')


plt.plot(consumo_por_regiao)

plt.xlabel('Ano')
plt.ylabel('Consumo')
plt.title('Consumo de energia por estado')
plt.legend()

plt.show()


# estados que mais consumiram 


consumo_est = df.groupby(by=['sigla_uf']).agg(consumo=('consumo',sum))
total = consumo_est['consumo'].sum()
consumo_est['porcentagem'] = consumo_est['consumo']/total*100
consumo_est['porcentagem'] = round(consumo_est['porcentagem'],2)

consumo_est.sort_values('consumo',inplace=True,ascending=False)

print(consumo_est)

# Comparar o aumento do consumo com o tipo de consumo (Residencial,comum, industrial,etc...)




# Consumo de cada estado de 2004 a 2021


# Análise da relação entre o consumo de energia elétrica e o PIB (Produto Interno Bruto)


# Análise do impacto do uso de fontes de energia renováveis no consumo de energia elétrica

# Análise da eficiência energética em diferentes setores da economia brasileira.
