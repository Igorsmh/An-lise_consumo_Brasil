import basedosdados as bd
import matplotlib.pyplot as plt
import pandas as pd

# Para carregar o dado direto no pandas
df = bd.read_table(dataset_id='br_mme_consumo_energia_eletrica',
                   table_id='uf', billing_project_id="robust-slice-376003")

print(df.info())

# Evolução do consumo de energia elétrica no Brasil nos últimos 10 anos

groupTotAno = df.groupby(df['ano']).sum()
groupTotAno = groupTotAno.reset_index()
groupTotAno.drop(axis=1, columns=['mes', 'numero_consumidores'], inplace=True)

# consumo em Gigawatt-hora e inteiro para facilitar
groupTotAno['consumo'] = (groupTotAno['consumo']/1000).astype('int64')


plt.title("Gráfico do consumo de energia por ano")
plt.xlabel("Ano")
plt.ylabel("Consumo em GWh")
plt.plot(groupTotAno['ano'],groupTotAno['consumo'])
plt.scatter(data=groupTotAno, x="ano", y="consumo")
plt.show()


# Média de consumo por anos
groupMedianAno = df.groupby(df['ano']).mean()
groupMedianAno = groupMedianAno.reset_index()
groupMedianAno.drop(axis=1, columns=['mes', 'numero_consumidores'], inplace=True)

# consumo em Gigawatt-hora e inteiro para facilitar

plt.title("Gráfico da média de consumo a cada ano")
plt.xlabel("Ano")
plt.ylabel("Consumo Médio")
plt.bar(groupMedianAno['ano'],groupMedianAno['consumo'])
plt.show()


print(df.groupby(df['ano'])['consumo'].agg([sum,'mean']))


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
