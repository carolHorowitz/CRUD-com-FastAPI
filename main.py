from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models import Joias
from database import conexao, Base, get_db
from repositorios import JoiasRepository
from schemas import JoiasRequest, JoiasResponse

app = FastAPI()

# Decorator que informa que é uma rota que lida com requisição do tipo POST que terá a rota /api/joias
# response_model informa qual tipo de dado estará contido no corpo da resposta
@app.post("/api/joias", response_model=JoiasResponse, status_code=status.HTTP_201_CREATED)

# função que será responsável por lidar com as requisições de cadastro de novos produtos
def create(request: JoiasRequest, db: Session = Depends(get_db)):
   joia = JoiasRepository.save(db, Joias(**request.dict()))
   return JoiasResponse.from_orm(joia)

#decorator: atribui uma funcionalidade nova a função que vem abaixo dele
#@app.get("/")


#def home():
#   return "Dados"
