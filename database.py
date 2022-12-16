
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# CONFIGURAÇÃO DE CONEXÃO COM BANCO DE DADOS

# Conexao é o ponto de partida para conexão com bd; a função mysql.connector é usada para criar o ponto de partida e 
# recebe como parâmetro a string de conexão com bd 
DATABASE_URL = "mysql+mysqlconnector://root:Ac018411.@localhost:3306/projeto-mentoria"

engine = create_engine(DATABASE_URL)

# A classe SessionLocal representa uma sessão com o BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# O método declarative_base() cria a classe Base que será usada para criação das classes de modelo do BD
Base = declarative_base()

# A função get_db disponibiliza uma instância da classe SessionLocal; através dela serão criadas novas sessões com o BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()







