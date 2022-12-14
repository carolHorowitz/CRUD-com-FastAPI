
import mysql.connector
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#CONFIGURAÇÃO DE CONEXÃO COM BANCO DE DADOS

#conexao é o ponto de partida para conexão com bd; a função mysql.connector é usada para criar o ponto de partida e recebe como parâmetro a string de conexão com bd
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ac018411.',
    database='projeto-mentoria',
)

#a classe SessionLocal representa uma sessão com o BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=conexao)

#o método declarative_base() cria a classe Base que será usada para criação das classes de modelo do BD
Base = declarative_base()

#a função get_db disponibiliza uma instância da classe SessionLocal; através dela serão criadas novas sessões com o BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

cursor = conexao.cursor()


cursor.close()
conexao.close()





