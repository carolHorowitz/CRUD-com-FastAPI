
# CRIAÇÃO DA CAMADA REPOSITÓRIO UTILIZANDO PADRÃO REPOSITORY PATTERN: isola as especificidade de acesso a base de 
# dados em uma única camada 


from sqlalchemy.orm import Session

from models import Joias

# Essa classe terá métodos estáticos que irão realizar as operações no BD

class JoiasRepository:
    @staticmethod
    # busca todos os produtos cadastrados
    def find_all(db: Session) -> list[Joias]:
        return db.query(Joias).all()

    @staticmethod
    # método usado para cadastro ou edição de um produto existente
    def save(db: Session, joia: Joias) -> Joias:
        print(joia)
        joiaexiste = db.query(Joias).filter(Joias.produto == joia).first()
        print(joiaexiste)
        if joiaexiste:
            db.merge(joia)
        else:
            db.add(joia)
        db.commit()
        return joia

    @staticmethod
    # busca um produto com base no id
    def find_by_id(db: Session, id: int) -> Joias:
        return db.query(Joias).filter(Joias.idEstoque == id).first()

    @staticmethod
    # verifica se existe algum produto cadastrado com base no id
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Joias).filter(Joias.idEstoque == id).first() is not None

    @staticmethod
    # exclui um produto com base no seu id
    def delete_by_id(db: Session, id: int) -> None:
        joia = db.query(Joias).filter(Joias.idEstoque == id).first()
        if joia is not None:
            db.delete(joia)
            db.commit()

    @staticmethod
    def find_by_name(db: Session, joia: str) -> Joias:
        return db.query(Joias).filter(Joias.produto == joia).first()
