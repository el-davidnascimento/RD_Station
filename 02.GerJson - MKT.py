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
    directory = r'G:\.shortcut-targets-by-id\1kArAZwgCxrjbQwQOPEzeJLtMUll3VVJ7\13. Dados\13.10. Marketing\13.10.2. Base Oportunidades'
    filename = f'oportunidades_{params["page"]}.json'
    path = os.path.join(directory,filename)
    with open(path, 'w') as f:
        json.dump(data_opt, f)

    # verifica se há mais páginas
    has_more = data_opt.get('has_more', False)

    # atualiza os parâmetros para a próxima página
    params['page'] += 1