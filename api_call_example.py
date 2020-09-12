# %%
from pprint import pprint as pp
import requests
import json

# %%
r = requests.get('https://pokeapi.co/api/v2/pokemon/charmander')
pokemon = json.loads(r.content)

# %%
for ability in pokemon['abilities']:
    print("Ability name: %s" % ability['ability']['name'])
