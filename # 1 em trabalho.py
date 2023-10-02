import psycopg2
import json
import os

# Conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="Multiverso",
    user="postgres",
    password="Multiverso@Educa"
)

# Cursor
cur = conn.cursor()

################# OPORTUNIDADE ###############################

# Define o diretório onde os arquivos JSON estão armazenados
directory = r'C:\Users\Victor\PycharmProjects\pythonProject\Oportunidade'

# Lista os nomes dos arquivos JSON no diretório
json_opt_files = os.listdir(directory)

# Loop através de cada arquivo JSON
for oportjson in json_opt_files:
    # Verifica se o arquivo é um arquivo JSON válido
    if oportjson.endswith('.json'):
        # Caminho completo para o arquivo JSON
        json_file_path = os.path.join(directory, oportjson)

        # Abre o arquivo JSON
        with open(json_file_path, 'r') as f:
            # Carrega os dados do arquivo JSON
            data = json.load(f)

            # Loop através de cada "deal" no arquivo JSON
            for deal in data['deals']:
                # Verifica se a chave 'stop_time_limit' existe no dicionário 'deal'

                deal_id = deal['id'],
                deal_name = deal['name'],
                deal_amount_montly = deal['amount_montly'],
                deal_amount_unique = deal['amount_unique'],
                deal_amount_total = deal['amount_total'],
                deal_prediction_date = deal['prediction_date'],
                deal_markup = deal['markup'],
                deal_last_activity_at = deal['last_activity_at'],
                deal_interactions = deal['interactions'],
                deal_markup_last_activities = deal['markup_last_activities'],
                deal_created_at = deal['created_at'],
                deal_update_at = deal.get('update_at',0),
                deal_rating = deal['rating'],
                deal_markup_created = deal['markup_created'],
                deal_last_activity_content = deal['last_activity_content'],
                deal_user_changed = deal['user_changed'],
                deal_hold = deal['hold'],
                deal_win = deal['win'],
                deal_closed_at = deal['closed_at'],
                deal_expiration_date_time = deal['stop_time_limit'].get('expiration_date_time',0),
                deal_expired = deal['stop_time_limit'].get('expired', 0),
                deal_expired_days = deal['stop_time_limit'].get('expired_days', 0),
                if 'organization' in deal:
                    deal_organization_id = deal['organization'].get('id', 0),
                    deal_organization_name = deal['organization'].get('name', 0),
                    deal_organization_address = deal['organization'].get('address', 0),
                    deal_organization_address_latitude = deal['organization'].get('address_latitude', 0),
                    deal_organization_address_longitude = deal['organization'].get('address_longitude', 0),
                else:
                    deal_organization_id = 0,
                    deal_organization_name = 0,
                    deal_organization_address = 0,
                    deal_organization_address_latitude = 0,
                    deal_organization_address_longitude = 0,

                if 'user' in deal:
                    deal_user_id = deal['user']['id'],
                    deal_user_name = deal['user']['name'],
                    deal_user_email = deal['user']['email'],
                else:
                    deal_user_id = 0,
                    deal_user_name = 0,
                    deal_user_email = 0,

                if 'deal_stage'in deal:
                    deal_deal_stage_id = deal['deal_stage'].get('id',0),
                    deal_deal_stage_name = deal['deal_stage'].get('name',0),
                    deal_deal_stage_created_at = deal['deal_stage'].get('created_at',0),
                    deal_deal_stage_updated_at = deal['deal_stage'].get('updated_at', 0),
                else:
                    deal_deal_stage_id = 0,
                    deal_deal_stage_name = 0,
                    deal_deal_stage_created_at = 0,
                    deal_deal_stage_updated_at = 0,

                if 'deal_source' in deal:
                    deal_deal_source_id = deal['deal_source'].get('id',0),
                    deal_deal_source_name = deal['deal_source'].get('name',0),
                    deal_deal_source_created_at = deal['deal_source'].get('created_at',0),
                    deal_deal_source_updated_at = deal['deal_source'].get('updated_at', 0),
                else:
                    deal_deal_source_id = 0,
                    deal_deal_source_name = 0,
                    deal_deal_source_created_at = 0,
                    deal_deal_source_updated_at = 0,

                if 'campaign' in deal:
                    deal_campaign_id = deal['campaign'].get('id',0),
                    deal_campaign_name = deal['campaign'].get('name', 0),
                    deal_campaign_created_at = deal['campaign'].get('created_at', 0),
                    deal_campaign_updated_at = deal['campaign'].get('updated_at', 0),
                else:
                    deal_campaign_id = 0,
                    deal_campaign_name = 0,
                    deal_campaign_created_at = 0,
                    deal_campaign_updated_at = 0,

                for contact in deal['contacts']:
                    deal_contacts_name = contact.get('name',0),
                    deal_contacts_title = contact.get('title', 0),
                    deal_contacts_birthday = contact.get('birthday', 0),
                    deal_contacts_email = contact.get('email', 0),


                cur.execute("""INSERT INTO TESTES2 (
                insert_time,
                deal_id,
                deal_name,
                deal_amount_montly,
                deal_amount_unique,
                deal_amount_total,
                deal_prediction_date,
                deal_markup,
                deal_last_activity_at,
                deal_interactions,
                deal_markup_last_activities,
                deal_created_at,
                deal_update_at,
                deal_rating,
                deal_markup_created,
                deal_last_activity_content,
                deal_user_changed,
                deal_hold,
                deal_win,
                deal_closed_at,
                deal_expiration_date_time,
                deal_expired,
                deal_expired_days,
                deal_organization_id,
                deal_organization_name,
                deal_organization_address,
                deal_organization_address_latitude,
                deal_organization_address_longitude,
                deal_user_id,
                deal_user_name,
                deal_user_email,
                deal_deal_stage_id,
                deal_deal_stage_name,
                deal_deal_stage_created_at,
                deal_deal_source_id,
                deal_deal_source_name,
                deal_deal_source_created_at,
                deal_deal_source_updated_at,
                deal_campaign_id,
                deal_campaign_name,
                deal_campaign_created_at,
                deal_campaign_updated_at,
                deal_contacts_name,
                deal_contacts_title,
                deal_contacts_birthday,
                deal_contacts_email
                 
                ) VALUES (
                NOW(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                );""",
                            (
                                deal_id,
                                deal_name,
                                deal_amount_montly,
                                deal_amount_unique,
                                deal_amount_total,
                                deal_prediction_date,
                                deal_markup,
                                deal_last_activity_at,
                                deal_interactions,
                                deal_markup_last_activities,
                                deal_created_at,
                                deal_update_at,
                                deal_rating,
                                deal_markup_created,
                                deal_last_activity_content,
                                deal_user_changed,
                                deal_hold,
                                deal_win,
                                deal_closed_at,
                                deal_expiration_date_time,
                                deal_expired,
                                deal_expired_days,
                                deal_organization_id,
                                deal_organization_name,
                                deal_organization_address,
                                deal_organization_address_latitude,
                                deal_organization_address_longitude,
                                deal_user_id,
                                deal_user_name,
                                deal_user_email,
                                deal_deal_stage_id,
                                deal_deal_stage_name,
                                deal_deal_stage_created_at,
                                deal_deal_stage_updated_at,
                                deal_deal_source_id,
                                deal_deal_source_name,
                                deal_deal_source_created_at,
                                deal_deal_source_updated_at,
                                deal_campaign_id,
                                deal_campaign_name,
                                deal_campaign_created_at,
                                deal_campaign_updated_at,
                                deal_contacts_name,
                                deal_contacts_title,
                                deal_contacts_birthday,
                                deal_contacts_email
                            ))

# Commit e fechamento da conexão
conn.commit()
cur.close()
conn.close()
deal_deal_stage_updated_at,
