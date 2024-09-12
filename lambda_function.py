import json
import requests

def lambda_handler(event, context):
    pokemon_name = event['pokemon_name']
    
    # Requisição à PokeAPI
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}')
    
    if response.status_code == 200:
        pokemon_data = response.json()
        
        # Filtrar dados relevantes
        filtered_data = {
            "name": pokemon_data["name"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
            "types": [ptype["type"]["name"] for ptype in pokemon_data["types"]]
        }
        
        return {
            'statusCode': 200,
            'pokemon_data': filtered_data
        }
    else:
        return {
            'statusCode': response.status_code,
            'message': 'Pokemon not found'
        }
