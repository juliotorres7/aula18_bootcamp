import requests
from pydantic import BaseModel

class PokemonSchema(BaseModel): #contrato de dados, schema de dados
    name: str
    type: str

    class Config:
        from_attributes = True

def pegar_pokemon(id: int):

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()

    data_types = data['types']
    type_list = []

    for name_info in data_types:
        type_list.append(name_info['type']['name'])

    types = ','.join(type_list)
    print(data['name'],types)

    return PokemonSchema(name=data['name'],type=types)

if __name__ == "__main__":
    pegar_pokemon(10)
    pegar_pokemon(6)
    pegar_pokemon(13)