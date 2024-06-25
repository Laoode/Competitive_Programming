s = input().strip()
pokemon_ids = input().strip()

encoding = {}
for i, char in enumerate(s):
    encoding[str(i+1).zfill(3)] = char

decoded_message = ''
for i in range(0, len(pokemon_ids), 3):
    id_pokemon = pokemon_ids[i:i+3]
    decoded_message += encoding[id_pokemon]

print(decoded_message)
