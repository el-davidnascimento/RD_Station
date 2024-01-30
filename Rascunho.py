import os
import pandas as pd
import json
from flatten_json import flatten

directory = r'G:\.shortcut-targets-by-id\1kArAZwgCxrjbQwQOPEzeJLtMUll3VVJ7\13. Dados\13.9. Atendimento\13.9.2. RD Station\13.9.2.1. Oportunidade'

# Lista para armazenar os dados
data_list = []

# Itera sobre cada arquivo JSON na lista
for file_path in os.listdir(directory):
    if file_path.endswith('.json'):
        with open(os.path.join(directory, file_path), 'r') as file:
            # Lê o conteúdo do arquivo JSON
            data = json.load(file)

            # Verifica se a chave 'deals' está presente no dicionário
            if 'deals' in data:
                deals_list = data['deals']
                for i, deal in enumerate(deals_list):
                    # Utiliza flatten_json para achatamento
                    flat_deal = flatten(deal, separator='.')

                    # Adiciona uma coluna com o nome do arquivo e número do deal
                    flat_deal['File'] = file_path
                    flat_deal['Deal Number'] = i + 1

                    # Adiciona o dicionário à lista
                    data_list.append(flat_deal)

# Cria o DataFrame fora do loop para incluir todas as informações
df_resultados = pd.DataFrame(data_list)

# Exibe os tipos
print(df_resultados.dtypes)

# Caminho para a pasta de downloads
pasta_downloads = r'C:\Users\Victor\Downloads'

# Salvar o DataFrame em um arquivo CSV na pasta de downloads
caminho_arquivo = os.path.join(pasta_downloads, 'dados_deals_flatten.csv')
df_resultados.to_csv(caminho_arquivo, index=False, encoding='utf-8-sig')
print(f"DataFrame salvo com sucesso em '{caminho_arquivo}'")
