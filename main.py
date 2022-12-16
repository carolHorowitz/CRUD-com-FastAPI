
import models
from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from models import Joias
from database import engine, Base, get_db
from repositorios import JoiasRepository
from schemas import JoiasRequest, JoiasResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ROTA DE CADASTRO DE PRODUTO

# Decorator que informa que é uma rota que lida com requisição do tipo POST que terá a rota /api/joias response_model
# informa qual tipo de dado estará contido no corpo da resposta (será um dado tipo JoiasReponse); status_code é o 
# parâmentro da função 

# Função que será responsável por lidar com as requisições de cadastro de novos produtos no método create passamos o 
# parâmetro chamado request que é do tipo JoiasRequest que recebe os dados que foram passados no corpo da requisição;

# O segundo parâmetro do método create é a db do tipo Session, que tem como valor padrão a instrução Depends(
# get_db)-> realiza a injeção de dependências do FastApi 
@app.post("/api/joias", response_model=JoiasResponse, status_code=status.HTTP_201_CREATED)
def create(request: JoiasRequest, db: Session = Depends(get_db)):
    joia = JoiasRepository.save(db, Joias(**request.dict()))
    return JoiasResponse.from_orm(joia)

# ROTA DE LISTAGEM

# A função chamada get_all irá processar as requisições feitas para a rota /api/cursos

# A função get_all recebe como parâmetro apenas a sessão do banco de dados via injeção de dependências 
@app.get("/api/joias", response_model=list[JoiasResponse])
def get_all(db: Session = Depends(get_db)):
    joia = JoiasRepository.find_all(db)
    return [JoiasResponse.from_orm(joia) for joia in joias]

# ROTA DE BUSCA POR ID

# A função find_by_id irá tratar a requisição

# A função find_by_id recebe o parâmetro id que será a parte variável da rota, ou seja, o id do curso que esta sendo 
# buscado e a injeção de dependências da sessão do banco de dados. 
@app.get("/api/joias/{id}", response_model=JoiasResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    joia = JoiasRepository.find_by_id(db, id)
    if not joia:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    return JoiasResponse.from_orm(joia)

# ROTA DE EXCLUSÃO POR ID

# passado como status code a constante HTTP_204_NO_CONTENT, que irá retornar o status code 204, que quer dizer que a 
# requisição foi processada com sucesso, porém não existe nada a ser retornado para quem realizou a requisição. 
@app.delete("/api/joias/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not JoiasRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    JoiasRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# ROTA DE ATUALIZAÇÃO
@app.put("/api/joais/{id}", response_model=JoiasResponse)
def update(id: int, request: JoiasRequest, db: Session = Depends(get_db)):
    if not JoiasRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
        )
    joia = JoiasRepository.save(db, Joias(id=id, **request.dict()))
    return JoiasResponse.from_orm(joia)






