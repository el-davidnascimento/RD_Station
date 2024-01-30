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
    directory = r'G:\.shortcut-targets-by-id\1kArAZwgCxrjbQwQOPEzeJLtMUll3VVJ7\13. Dados\13.9. Atendimento\13.9.2. RD Station\13.9.2.1. Oportunidade'
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
directory = r'G:\.shortcut-targets-by-id\1kArAZwgCxrjbQwQOPEzeJLtMUll3VVJ7\13. Dados\13.9. Atendimento\13.9.2. RD Station\13.9.2.2. Anotacoes'
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
    'per_page': 100,
    'data_start': '2022-01-01'
}

has_more = True
while has_more:
    response = requests.get(base_tar_url, params=params)
    data_tar = response.json()

    # escreve os dados em um arquivo JSON
    directory = r'G:\.shortcut-targets-by-id\1kArAZwgCxrjbQwQOPEzeJLtMUll3VVJ7\13. Dados\13.9. Atendimento\13.9.2. RD Station\13.9.2.5. Tarefa'
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
directory = r'G:\.shortcut-targets-by-id\1kArAZwgCxrjbQwQOPEzeJLtMUll3VVJ7\13. Dados\13.9. Atendimento\13.9.2. RD Station\13.9.2.4. Funil'
filename = f'funil_{params["page"]}.json'
path = os.path.join(directory, filename)
with open(path, 'w') as f:
    json.dump(data_funil, f)


########################## MBX ##################################

import requests
import json
import os
from datetime import datetime

url = "http://sip.mbxinteligencia.com.br/api/v1/calls/list"
headers = {
    "token-auth": "192f98a5-0716-4480-be3c-5d2d49243fed"
}

start_date = "2024-01-24"
end_date = "2024-01-26"
params = {
    "start_date": start_date,
    "end_date": end_date
}

output_folder = r"G:\.shortcut-targets-by-id\1kArAZwgCxrjbQwQOPEzeJLtMUll3VVJ7\13. Dados\13.9. Atendimento\13.9.4. MBX\13.9.4.1. MBX - GERAL"  # Substitua pelo caminho desejado

try:
    response = requests.get(url, headers=headers, params=params)


    # Verifique se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        data = response.json()

        # Gera um nome de arquivo com base nas datas de início e fim
        date_format = "%Y-%m-%d"
        start_date_obj = datetime.strptime(start_date, date_format).date()
        end_date_obj = datetime.strptime(end_date, date_format).date()

        filename = f"resposta_api_{start_date_obj}_{end_date_obj}.json"
        output_file = os.path.join(output_folder, filename)

        # Certifique-se de que a pasta de saída exista
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        with open(output_file, "w") as file:
            json.dump(data, file, indent=4)

        print(f"Resposta da API salva em {output_file}")
    else:
        print(f"Falha na solicitação. Código de status: {response.status_code}")

except Exception as e:
    print(f"Erro durante a solicitação: {e}")
