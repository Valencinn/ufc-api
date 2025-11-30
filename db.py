#explicacion de como se crea el link: primero importas create_engine de sqlalchemy, luego definimos las variables de conexion (usuario, password, host, puerto y nombre de la base de datos) y finalmente creas el link con el formato adecuado para mysql y pymysql
#cabe alcarar los datos los consigue gracias al .env que esta oculto y la libreria dotenv que lee las variables de entorno

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv

load_dotenv()

password = quote_plus(os.getenv("DB_PASSWORD"))
DATABASE_URL = f"mysql+pymysql://root:{password}@localhost:3306/ufc"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()