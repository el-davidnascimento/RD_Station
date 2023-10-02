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
################ FUNIL ###################

cur.execute('''CREATE TABLE TESTESFUNIL2 (
               insert_time DATE,
               funil_id VARCHAR(255),
               funil_name VARCHAR(255),
               deal_stages VARCHAR(255)
               
               );''')

conn.commit()
cur.close()
conn.close()