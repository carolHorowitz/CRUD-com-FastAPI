
from sqlalchemy.orm import Session

from models import Joias

class JoiasRepository:
    @staticmethod
    def find_all(db: Session) -> list[Joias]:
        return db.query(Joias).all()

    @staticmethod
    def save(db: Session, joia: Joias) -> Joias:
        if joia not in Joias:
            db.add(joia)
        db.commit()
        return joia

    @staticmethod
    def find_by_name(db: Session, joia: str) -> Joias:
        return db.query(Joias).filter(Joias.produto == joia).first()

    @staticmethod
    def exists_by_name(db: Session, joia: str) -> bool:
        return db.query(Joias).filter(Joias.produto == joia).first() is not None

    @staticmethod
    def delete_by_name(db: Session, joia: str) -> None:
        joia = db.query(Joias).filter(Joias.produto == joia).first()
        if joia is not None:
            db.delete(joia)
            db.commit()

    @staticmethod
    def find_by_name(db: Session, joia: str) -> Joias:
        return db.query(Joias).filter(Joias.produto == joia).first()
