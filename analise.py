import basedosdados as bd
import matplotlib.pyplot as plt
import pandas as pd
# Para carregar o dado direto no pandas
df = bd.read_table(dataset_id='br_mme_consumo_energia_eletrica',
                   table_id='uf', billing_project_id="robust-slice-376003")


groupAno = df.groupby(df['ano']).sum()
groupAno = groupAno.reset_index()


ano = groupAno['ano']
consumo_tot = groupAno['consumo']


plt.title("Gráfico do consumo de energia por ano")
plt.xlabel("Ano")
plt.ylabel("Consumo")

plt.scatter(ano, consumo_tot)
plt.plot(ano, consumo_tot)
plt.show()


groupUf = df.groupby(df['sigla_uf']).sum()
groupUf = groupUf.reset_index()

print(groupUf)

# Consumo de cada estado de 2004 a 2021
sigla_uf = groupUf['sigla_uf']
consumo_estado = groupUf['consumo']

plt.bar(sigla_uf, consumo_estado)
plt.show()
