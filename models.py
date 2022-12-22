
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base



class Joias(Base):
    __tablename__ = "estoque"

    idEstoque: int = Column(Integer, primary_key=True, index=True)
    produto: str = Column(String(100), nullable=False)
    quantidade: int = Column(Integer, nullable=False)
