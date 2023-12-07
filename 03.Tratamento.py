import os
import pandas as pd
import requests
import json

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

# verifica se a solicitação foi bem sucedida
if response.status_code == 200:
    # extrai os dados do JSON da resposta
    data_opt = response.json()

    # Transforma os dados em um DataFrame do Pandas
    df = pd.DataFrame(data_opt['deals'])

    # Ajusta os tipos de dados conforme necessário
    columns_to_convert = [
        "_id", "id", "name", "amount_montly", "amount_unique", "amount_total", "prediction_date", "markup",
        "last_activity_at", "interactions", "markup_last_activities", "created_at", "updated_at", "rating", "markup_created",
        "last_activity_content", "user_changed", "hold", "win", "closed_at", "stop_time_limit", "organization", "user",
        "deal_stage", "deal_source", "campaign", "deal_lost_reason", "next_task", "contacts", "deal_custom_fields", "deal_products",
        "deals._id", "deals.id", "deals.name", "deals.amount_montly", "deals.amount_unique", "deals.amount_total", "deals.prediction_date",
        "deals.markup", "deals.last_activity_at", "deals.interactions", "deals.markup_last_activities", "deals.created_at",
        "deals.updated_at", "deals.rating", "deals.markup_created", "deals.last_activity_content", "deals.user_changed",
        "deals.hold", "deals.win", "deals.closed_at", "deals.stop_time_limit", "deals.organization", "deals.user",
        "deals.deal_stage", "deals.deal_source", "deals.campaign", "deals.deal_lost_reason", "deals.next_task", "deals.contacts",
        "deals.deal_custom_fields", "deals.deal_products"
    ]

    for column in columns_to_convert:
        if column in df.columns:
            if column in ["deals.last_activity_at", "deals.created_at", "deals.updated_at", "deals.closed_at",
                          "deals.stop_time_limit.expiration_date_time", "deals.deal_stage.created_at",
                          "deals.deal_stage.updated_at", "deals.deal_source.created_at", "deals.deal_source.updated_at",
                          "deals.campaign.created_at", "deals.campaign.updated_at", "deals.deal_lost_reason.created_at",
                          "deals.deal_lost_reason.updated_at", "deals.next_task.date", "deals.next_task.hour"]:
                df[column] = pd.to_datetime(df[column])
            elif column in ["deals.user_changed", "deals.hold", "deals.win", "deals.stop_time_limit.expired"]:
                df[column] = df[column].astype(bool)
            elif column in ["deals._id", "deals.id", "deals.name", "deals.markup", "deals.markup_last_activities",
                            "deals.markup_created", "deals.last_activity_content", "deals.organization._id",
                            "deals.organization.id", "deals.organization.name", "deals.organization.address",
                            "deals.organization.user._id", "deals.organization.user.id", "deals.organization.user.name",
                            "deals.organization.user.email", "deals.organization.organization_segments",
                            "deals.user._id", "deals.user.id", "deals.user.name", "deals.user.nickname",
                            "deals.user.email", "deals.deal_stage._id", "deals.deal_stage.id", "deals.deal_stage.name",
                            "deals.deal_stage.nickname", "deals.deal_source._id", "deals.deal_source.id",
                            "deals.deal_source.name", "deals.campaign._id", "deals.campaign.id",
                            "deals.deal_lost_reason._id", "deals.deal_lost_reason.id", "deals.deal_lost_reason.name",
                            "deals.next_task._id", "deals.next_task.id", "deals.next_task.subject",
                            "deals.next_task.type", "deals.contacts", "deals.deal_custom_fields", "deals.deal_products",
                            "deals.amount_montly", "deals.amount_unique", "deals.amount_total", "deals.prediction_date",
                            "deals.interactions", "deals.rating", "deals.stop_time_limit.expired_days",
                            "deals.organization.address_latitude", "deals.organization.address_longitude"]:
                df[column] = df[column].astype(str)

    # Expandindo colunas que contenham dicionários ou listas
    columns_to_expand = ['stop_time_limit', 'organization', 'organization.user', 'user', 'deal_stage', 'campaign',
                         'deal_lost_reason', 'next_task', 'contacts', 'deal_custom_fields', 'deal_products']

    for col in columns_to_expand:
        if col in df.columns:
            df = pd.concat([df.drop([col], axis=1), df[col].apply(pd.Series)], axis=1)

    # Exibe o DataFrame resultante
    print(df.head())  # Exemplo de exibição dos primeiros registros do DataFrame resultante

    # Caminho para a pasta de downloads
    pasta_downloads = r'C:\Users\Victor\Downloads'

    # Salvar o DataFrame em um arquivo Excel na pasta de downloads
    caminho_arquivo = os.path.join(pasta_downloads, 'dados_deals.xlsx')
    df.to_excel(caminho_arquivo, index=False)
    print(f"DataFrame salvo com sucesso em '{caminho_arquivo}'")

else:
    # lida com erros de solicitação
    print(f'Erro ao fazer solicitação: {response.status_code}')