# %%
from pprint import pprint as pp

# %%
# Variaveis
poke_id     = 1
poke_name   = "diegosaur"
poke_attack = 10.2
poke_status = "shiny"

# %%
# Coleções
poke_moves = [
    "tackle", "punch", "splash",
    "tackle", "punch", "splash",
    "tackle", "punch", "splash",
    "tackle", "punch", "splash",
    "tackle", "punch", "splash",
    "tackle", "punch", "splash"
]
poke_moves2 = ("tackle", "punch", "splash")

clean = []
clean.append(1)
clean.append(2)
clean.append(3)
clean.append(4)
clean.append(5)
print(clean.pop())
print(clean.pop())
print(clean.pop())
print(clean.pop())
print(clean.pop())

# %%
# Iterações
uniq_moves = set(poke_moves)
for index, move in enumerate(uniq_moves):
    print("# %2d %s" % (index+1, move))

# %%
# Funções
def outrasCoisas():
    uniq_moves = set(poke_moves)
    for index, move in enumerate(uniq_moves):
        print("# %2d %s" % (index+1, move))

def attack(pokeName, damage):
    print(pokeName, damage)
    outrasCoisas()

attack("pikachu", 150)

# %%

if "tackle" in poke_moves:
    print("Ataque encontrado")
