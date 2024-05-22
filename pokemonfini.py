import csv

def pokémon_csv(pok_csv):
    pokemons = {}
    with open(pok_csv, 'r', encoding='utf-8') as csvfile:
        csv_r = csv.reader(csvfile)
        for row in csv_r:
            nom = row[0]
            stats = list(map(int, row[1:]))
            pokemons[nom] = stats
    return pokemons

#test
pkmn = pokémon_csv('pokemon.csv')
for nom, stats in pkmn.items():
    print(f'{nom}: {stats}')

