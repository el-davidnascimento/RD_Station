import requests

######### OPORTUNIDADE ##################
# URL base da API
base_opt_url = 'https://crm.rdstation.com/api/v1/deals?token=6352b03536af500023d5212a'

# faz uma solicitação GET para a API
response = requests.get(base_opt_url)

# verifica se a solicitação foi bem sucedida
if response.status_code == 200:
    # extrai os dados do JSON da resposta
    data_opt = response.json()

else:
    # lida com erros de solicitação
    print(f'Erro ao fazer solicitação: {response.status_code}')

######### ANOTAÇÕES ##################
# URL base da API
base_anot_url = 'https://crm.rdstation.com/api/v1/activities?token=6352b03536af500023d5212a'

# faz uma solicitação GET para a API
response = requests.get(base_anot_url)

# verifica se a solicitação foi bem sucedida
if response.status_code == 200:
    # extrai os dados do JSON da resposta
    data_anot = response.json()
else:
    # lida com erros de solicitação
    print(f'Erro ao fazer solicitação: {response.status_code}')

######### TAREFAS ##################
# URL base da API
base_tar_url = 'https://crm.rdstation.com/api/v1/tasks?token=6352b03536af500023d5212a'

# faz uma solicitação GET para a API
response = requests.get(base_tar_url)

# verifica se a solicitação foi bem sucedida
if response.status_code == 200:
    # extrai os dados do JSON da resposta
    data_tar = response.json()
else:
    # lida com erros de solicitação
    print(f'Erro ao fazer solicitação: {response.status_code}')

######### FUNIL ##################
# URL base da API
base_funil_url = 'https://crm.rdstation.com/api/v1/deal_pipelines?token=6352b03536af500023d5212a'

# faz uma solicitação GET para a API
response = requests.get(base_funil_url)

# verifica se a solicitação foi bem sucedida
if response.status_code == 200:
    # extrai os dados do JSON da resposta
    data_funil = response.json()
else:
    # lida com erros de solicitação
    print(f'Erro ao fazer solicitação: {response.status_code}')

