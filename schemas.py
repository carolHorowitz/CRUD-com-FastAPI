# CRIAÇÃO DA CAMADA SCHEMAS: contém as classes que irão representar os dados que serão recebidos e retornados no 
# corpo de uma requisição ou resposta HTTP 


# Pydantic: bilbioteca do FastApi - validação de dados através do uso da funcionalidade de Type Hints do Python
# BaseModel: classe a qual todas as classe de modelo do Pydantic devem herdar
from pydantic import BaseModel


# Definir tudo aquilo que é comum para as classes CursoRequest e CursoResponse evitando duplicação de código.
class JoiasBase(BaseModel):
    produto: str
    quantidade: int

# Recebe tudo que está no corpo das requisições HTTP
class JoiasRequest(JoiasBase):
    ...
# Tudo que queremos retornar no corpo das respostas HTTP. Tem definido o atributo id mais o atributo de JoiasBase
class JoiasResponse(JoiasBase):
    idEstoque: int

    # essa configuração habilita um método estático chamado from_orm que permite a criação de uma instância  do 
    # modelo pydantic a partir de uma classe de modelo na nossa ORM 
    class Config:
        orm_mode = True
