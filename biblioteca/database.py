from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configura tu cadena de conexión
USERNAME = "tu_usuario"
PASSWORD = "tu_password"
HOST = "localhost"
DB_NAME = "biblioteca"

DATABASE_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DB_NAME}"

# Crear motor de conexión
engine = create_engine(DATABASE_URL, echo=True)

# Crear sesión
SessionLocal = sessionmaker(bind=engine)

# Base para modelos
Base = declarative_base()
