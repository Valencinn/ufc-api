import _mysql_connector
import os #modulo estandar para que python pueda interactuar con el sistema operativo
from dotenv import load_dotenv #dotenv es una libreria que permite cargar variables de entorno desde un archivo .env, .env es privado no lo ve GitHub ni nadie, sirve para no poner contraseñas en el codigo

load_dotenv()

def get_db_connection():
    #Esta funcion establece una conexión a la base de datos MySQL utilizando las variables de entorno.

    return _mysql_connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_NAME")
    )