import psycopg2

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
################ OPORTUNIDADES 2 ###################

cur.execute('''CREATE TABLE TESTESOPORTUNIDADE2 (
               insert_time DATE,
               deal_id VARCHAR(255),
               deal_name VARCHAR(255),
               deal_amount_montly VARCHAR(255),
               deal_amount_unique VARCHAR(255),
               deal_amount_total VARCHAR(255),
               deal_prediction_date VARCHAR(255),
               deal_markup VARCHAR(255),
               deal_last_activity_at VARCHAR(255),
               deal_interactions VARCHAR(255),
               deal_markup_last_activities VARCHAR(255),
               deal_created_at VARCHAR(255),
               deal_update_at VARCHAR(255),
               deal_rating VARCHAR(255),
               deal_markup_created VARCHAR(255),
               deal_last_activity_content VARCHAR(255),
               deal_user_changed VARCHAR(255),
               deal_hold VARCHAR(255),
               deal_win VARCHAR(255),
               deal_closed_at VARCHAR(255),
               deal_expiration_date_time VARCHAR(255),
               deal_expired VARCHAR(255),
               deal_expired_days VARCHAR(255),
               deal_organization_id VARCHAR(255),
               deal_organization_name VARCHAR(255),
               deal_organization_address VARCHAR(255),
               deal_organization_address_latitude VARCHAR(255),
               deal_organization_address_longitude VARCHAR(255),
               deal_user_id VARCHAR(255),
               deal_user_name VARCHAR(255),
               deal_user_email VARCHAR(255),
               deal_deal_stage_id VARCHAR(255),
               deal_deal_stage_name VARCHAR(255),
               deal_deal_stage_created_at VARCHAR(255),
               deal_deal_stage_updated_at VARCHAR(255),
               deal_deal_source_id VARCHAR(255),
               deal_deal_source_name VARCHAR(255),
               deal_deal_source_created_at VARCHAR(255),
               deal_deal_source_updated_at VARCHAR(255),
               deal_campaign_id VARCHAR(255),
               deal_campaign_name VARCHAR(255),
               deal_campaign_created_at VARCHAR(255),
               deal_campaign_updated_at VARCHAR(255),
               deal_contacts_name VARCHAR(255),
               deal_contacts_title VARCHAR(255),
               deal_contacts_birthday VARCHAR(255),
               deal_contacts_email VARCHAR(255),
               custom_field_id VARCHAR(255),
               custom_field_label VARCHAR(255),
               custom_field_type VARCHAR(255)
               
               );''')


conn.commit()
cur.close()
conn.close()