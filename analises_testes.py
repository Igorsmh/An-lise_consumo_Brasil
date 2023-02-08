import basedosdados as bd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Para carregar o dado direto no pandas
df = bd.read_table(dataset_id='br_mme_consumo_energia_eletrica',
                   table_id='uf', billing_project_id="robust-slice-376003")



