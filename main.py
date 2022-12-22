
from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
import models
from models import Joias
from database import engine, SessionLocal
from repositorios import JoiasRepository
from schemas import JoiasRequest, JoiasResponse


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@app.post("/newtry/joias", response_model=JoiasResponse, status_code=status.HTTP_201_CREATED)
def create(request: JoiasRequest, db: Session = Depends(get_db)):
    joia = JoiasRepository.save(db, Joias(**request.dict()))
    return JoiasResponse.from_orm(joia)

@app.get("/newtry/joias", response_model=list[JoiasResponse])
def get_all(db: Session = Depends(get_db)):
    joia = JoiasRepository.find_all(db)
    return JoiasResponse.from_orm(joia)
    
@app.get("/newtry/joias/{joia}", response_model=JoiasResponse)
def find_by_name(joia: str, db: Session = Depends(get_db)):
    joia = JoiasRepository.find_by_name(db, joia)
    if not joia:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    return JoiasResponse.from_orm(joia)
    
@app.delete("/newtry/joias/{joia}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_name(joia: str, db: Session = Depends(get_db)):
    if not JoiasRepository.exists_by_name(db, joia):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    JoiasRepository.delete_by_name(db, joia)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    
@app.put("/newtry/joais/{joia}", response_model=JoiasResponse)
def update(joia: str, request: JoiasRequest, db: Session = Depends(get_db)):
    if not JoiasRepository.exists_by_name(db, joia):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    joia = JoiasRepository.save(db, Joias(joia=joia, **request.dict()))
    return JoiasResponse.from_orm(joia)
