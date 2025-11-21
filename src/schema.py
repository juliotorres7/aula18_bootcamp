import requests
from pydantic import BaseModel

class PokemonSchema(BaseModel): #contrato de dados, schema de dados
    name: str
    type: str

    class Config:
        from_attributes = True