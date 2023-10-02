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

################# FUNIL ###############################

# Define o diretório onde os arquivos JSON estão armazenados
directory = r'C:\Users\Victor\PycharmProjects\pythonProject\Funil'

# Lista os nomes dos arquivos JSON no diretório
json_files = [file for file in os.listdir(directory) if file.endswith('.json')]

# Loop através de cada arquivo JSON
for json_file in json_files:
    # Caminho completo para o arquivo JSON
    json_file_path = os.path.join(directory, json_file)

    # Abre o arquivo JSON
    with open(json_file_path, 'r') as f:
        data = json.load(f)
        # Itere sobre os objetos no JSON
        for item in data:
            funil_id = item.get('id', 0),
            funil_name = item.get('name', 0),
            deal_stages = item['deal_stages'].get('id',0)

            cur.execute("""INSERT INTO TESTESFUNIL2 (
            insert_time,
            funil_id,
            funil_name,
            deal_stages
            ) VALUES (
            NOW(), %s, %s, %s
            );""",
                        (
                            funil_id,
                            funil_name,
                            deal_stages
                        ))
# Commit e fechamento da conexão
conn.commit()
cur.close()
conn.close()