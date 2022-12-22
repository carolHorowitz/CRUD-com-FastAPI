

from pydantic import BaseModel
class User(BaseModel):
    user: str


class JoiasBase(BaseModel):
    produto: str
    quantidade: int

class JoiasRequest(JoiasBase):
    ...

class JoiasResponse(JoiasBase):
    idEstoque: int

    class Config:
        orm_mode = True
