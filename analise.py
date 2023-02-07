import basedosdados as bd
import matplotlib.pyplot as plt
import pandas as pd

# Para carregar o dado direto no pandas
df = bd.read_table(dataset_id='br_mme_consumo_energia_eletrica',
                   table_id='uf', billing_project_id="robust-slice-376003")

print(df.info())


# Evolução do consumo de energia elétrica no Brasil nos últimos 10 anos

group_consumo_ano = df.groupby(df['ano'])['consumo'].agg([sum, 'mean'])
group_consumo_ano = group_consumo_ano.reset_index()


plt.title("Gráfico do consumo de energia consumida por ano")
plt.xlabel("Ano")
plt.ylabel("Consumo em MWh")
plt.plot(group_consumo_ano['ano'], group_consumo_ano['sum'])
plt.scatter(data=group_consumo_ano, x="ano", y="sum")
plt.show()

#
plt.title("Gráfico da média de consumo a cada ano")
plt.xlabel("Ano")
plt.ylabel("Consumo Médio em MWh")
plt.bar(group_consumo_ano['ano'], group_consumo_ano['mean'])
plt.show()



# verificar alteração no consumo por quantidade de consumidores

# Bucketsize

# def bucketize(point: float, bucket_size: float) -> float:
#     return bucket_size * math.floor(point/bucket_size)

# def make_histogram(points:List[float], bucket_size:float) -> Dict[float,int]:
#     return Counter(bucketize(point,bucket_size) for point in points)

# def plot_histogram(points: List[float],bucket_size:float,title:str=""):
#     histogram = make_histogram(points,bucket_size)
#     plt.bar(histogram.keys(),histogram.values(),width=bucket_size)
#     plt.title(title)

# plot_histogram()

# Comparação do consumo de energia elétrica por estado e região


# Consumo de cada estado de 2004 a 2021


# Análise da relação entre o consumo de energia elétrica e o PIB (Produto Interno Bruto)


# Análise do impacto do uso de fontes de energia renováveis no consumo de energia elétrica
# Análise da eficiência energética em diferentes setores da economia brasileira.
