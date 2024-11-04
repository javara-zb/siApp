import psycopg2

conn = psycopg2.connect(database="postgres",  
                        user="southerninterests_webapp", 
                        password="600Bonaventure!",  
                        host="southern-interests-db.postgres.database.azure.com", port="5432") 

c = conn.cursor()

users = c.fetchall()
print(users)