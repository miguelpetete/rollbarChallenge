import psycopg2
from dotenv import dotenv_values

config = dotenv_values(".env")

def postgres_test():
    try:
        conn = psycopg2.connect(host=config["HOST"], 
                                port = config["PORT"], 
                                dbname=config["DBNAME"],
                                user=config["USER"], 
                                password=config["PASSWORD"])
        conn.close()
        return True
    except:
        return False