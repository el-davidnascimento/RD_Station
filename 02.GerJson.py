import os.path
import os
import requests
import json

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

    # escreve os dados em um arquivo JSON
    directory = r'C:\Users\Victor\PycharmProjects\RD_Station\Oportunidade'
    filename = f'oportunidades_{params["page"]}.json'
    path = os.path.join(directory,filename)
    with open(path, 'w') as f:
        json.dump(data_opt, f)

    # verifica se há mais páginas
    has_more = data_opt.get('has_more', False)

    # atualiza os parâmetros para a próxima página
    params['page'] += 1


############# ANOTACOES #######################

# URL base da API
base_anot_url = 'https://crm.rdstation.com/api/v1/activities?token=6352b03536af500023d5212a'
response = requests.get(base_anot_url)
data_anot = response.json()

# escreve os dados em um arquivo JSON
directory = r'C:\Users\Victor\PycharmProjects\RD_Station\Anotacoes'
filename = f'anotacoes_{params["page"]}.json'
path = os.path.join(directory, filename)
with open(path, 'w') as f:
    json.dump(data_anot, f)


############# TAREFAS #######################
# URL base da API
base_tar_url = 'https://crm.rdstation.com/api/v1/tasks?token=6352b03536af500023d5212a'

# parâmetros iniciais da consulta
params = {
    'page': 1,
    'per_page': 100
}

has_more = True
while has_more:
    response = requests.get(base_tar_url, params=params)
    data_tar = response.json()

    # escreve os dados em um arquivo JSON
    directory = r'C:\Users\Victor\PycharmProjects\RD_Station\Tarefas'
    filename = f'tarefa_{params["page"]}.json'
    path = os.path.join(directory, filename)
    with open(path, 'w') as f:
        json.dump(data_tar, f)

    # verifica se há mais páginas
    has_more = data_tar.get('has_more', False)

    # atualiza os parâmetros para a próxima página
    params['page'] += 1

############# FUNIL #######################

# URL base da API
base_funil_url = 'https://crm.rdstation.com/api/v1/deal_pipelines?token=6352b03536af500023d5212a'
response = requests.get(base_funil_url)
data_funil = response.json()

# escreve os dados em um arquivo JSON
directory = r'C:\Users\Victor\PycharmProjects\RD_Station\Funil'
filename = f'funil_{params["page"]}.json'
path = os.path.join(directory, filename)
with open(path, 'w') as f:
    json.dump(data_funil, f)