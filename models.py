from sqlalchemy import Column, Integer, String
from database import Base

# CRIAÇÃO DA CAMADA MODELO: essa camada conterá classes que irão representar as tabelas do banco de dados e que o 
# SQLAlchemy irá utilizar para gerar essas tabelas de forma automática. 

class Joias(Base):
    __tablename__ = "estoque"

    idEstoque: int = Column(Integer, primary_key=True, index=True)
    produto: str = Column(String(100), nullable=False)
    quantidade: int = Column(Integer, nullable=False)
