import json
from google.cloud import storage
import requests

# Autenticando o acesso ao Cloud Storage
client = storage.Client()
bucket_name = 'SEU_NOME_DO_BUCKET'

# Função para salvar dados no Cloud Storage
def salvar_no_cloud_storage(dados, nome_do_arquivo):
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(nome_do_arquivo)
    blob.upload_from_string(json.dumps(dados), content_type='application/json')

############# OPORTUNIDADE #######################
# URL base da API
base_opt_url = 'https://crm.rdstation.com/api/v1/deals?token=6352b03536af500023d5212a&limit=200'

# parâmetros iniciais da consulta
params = {
    'page': 1,
    'per_page': 100
}

has_more = True
while has_more:
    response = requests.get(base_opt_url, params=params)
    data_opt = response.json()

    # Salvar no Cloud Storage
    nome_arquivo = f'oportunidades_{params["page"]}.json'
    salvar_no_cloud_storage(data_opt, nome_arquivo)


