import numpy as np
import requests
import time
import sys


charmanderArt = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠛⠛⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣀⣸⣿⣿⣿⣿⣇⣀⠿⢿⣿⣿⣿⣿⣿⣿⣿⡇⢘⣝⣀⡸⢿⣿⣿
⣿⣿⡿⠿⣀⣿⣿⣿⣿⣿⣿⣿⣿⣀⡸⢿⣿⣿⣿⣿⣿⣿⡇⢘⣍⣩⡁⢸⣿⣿
⣿⡟⢣⣿⣿⣿⣿⡿⡛⡛⢻⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⡇⢘⣩⣍⣩⣍⡁⢸⣿
⣿⡇⢸⣿⣿⣿⣿⡇⡪⡪⢸⣿⣿⣿⣷⣶⠉⣿⣿⣿⣿⣇⡸⢭⣍⣩⣍⡁⢸⣿
⣿⣷⡎⢹⣿⣿⣿⣷⣶⣶⣾⣿⣿⣿⣿⣿⣶⠉⢹⣿⣿⣿⡇⢘⣭⢘⢰⣾⣿⣿
⣿⣿⣿⣇⣀⣀⡸⠿⠿⠿⢿⣿⣿⠿⢿⣿⣿⣿⡇⢸⠿⣀⣸⡿⠿⢇⣸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⡆⢐⢔⢔⢕⠍⣶⣾⣿⣿⣿⣿⡇⢸⣿⣿⡇⢸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡟⢣⣴⠑⢑⢕⢕⢄⢄⣼⣿⣿⣿⡇⠘⠛⢣⣼⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣆⣀⣀⣀⡰⠕⠕⠕⣿⣿⠿⠇⢀⣀⣀⣸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⡆⢰⣾⣿⣤⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣀⣀⣀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

squirtleArt = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿
⣿⣿⣿⡇⢰⣿⣿⣿⣿⣿⠉⠉⢹⣿⣿⣿⣿⣿⣿⣿⡏⢱⣶⣶⣶⣶⡎⢹⣿⣿
⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣶⠉⠉⢹⣿⠉⢱⣿⣿⣿⠛⣿⣿⡇⢸⣿
⣿⡇⢈⣸⣿⣿⣿⡟⡛⠛⣿⣿⣧⡜⢻⣿⣿⣇⣀⠿⢿⣿⡇⢸⣿⣿⡿⢇⣸⣿
⣿⡇⢸⣿⣿⣿⣿⡇⢸⠉⣿⣿⣿⡇⠸⠿⢿⣿⣿⣀⡸⠇⢀⣀⣀⣀⣸⣿⣿⣿
⣿⣿⣧⣤⠛⠛⣿⣷⣶⣶⣿⡏⠉⢱⣶⣶⡆⢸⣿⣿⡇⢰⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣤⠛⠃⢠⣤⣤⡄⢸⣿⣿⣿⡏⠉⢹⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⢇⣸⣿⣿⣇⣀⣀⣀⣀⡀⢸⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣧⡜⠃⠈⠉⠉⢹⣿⣿⣿⡇⠸⢇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⡄⢠⣤⣿⣧⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣀⣀⣀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

bulbasaurArt = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠏⣉⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⢅⣿⢄⣤⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⠉⢔⣾⢕⣿⢕⣶⠉⠉⠿⢷⣶⣉⣉⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣇⣸⣿⣿⣿⢕⣿⢕⣿⢕⣿⣿⣿⣧⣤⠛⣿⣿⡸⢿⣿⣿
⣿⣿⣿⡟⠛⠛⣿⡇⢸⡟⠛⠛⢪⣿⠓⠛⣤⣤⡜⢻⣿⣿⣿⣿⣀⢿⣧⡜⢻⣿
⣿⣿⡇⢸⣿⠉⢰⣶⣶⡎⠉⣿⣷⣶⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⢕⢸⢕⡇⢸⣿
⣿⡇⢸⣿⣿⣿⣿⣿⣧⣤⣿⠛⣿⣿⠿⢿⣿⣿⣿⡇⢸⣿⣿⣿⠿⣸⡟⢣⣼⣿
⣿⡏⢱⣆⠸⣿⣀⣸⣿⣿⣀⠿⠉⡀⢿⣷⡎⢹⣿⣷⡎⢉⣹⠉⠶⢏⣱⣾⣿⣿
⡇⢸⡟⠓⢡⣿⣿⣿⣿⣿⣿⡀⠛⠊⢸⣿⣧⣼⣿⣿⡇⢸⣿⣶⣶⣧⡜⢻⣿⣿
⣷⡎⠉⠹⢷⡾⠿⠷⠾⠿⢏⣉⣉⡹⢏⣱⡆⣀⣿⡏⢹⣿⡿⢿⣿⡿⢷⡎⢹⣿
⣿⣿⡇⢠⡜⢣⣤⡀⢀⢔⢕⢕⢕⠕⠛⢣⣼⡟⠃⣤⣀⠘⢻⡇⢸⠃⣼⣧⡜⢻
⣿⡇⢸⣿⣿⣶⣶⣉⡁⠰⠶⠶⠶⠶⣉⡉⢱⡆⣿⣿⣿⣶⣾⡇⠰⣿⡏⢹⡇⢸
⣿⢸⡟⢻⣿⣿⠿⣀⣸⣿⣿⣿⣿⣿⣿⣿⡇⢸⡟⢻⣿⡟⢣⣼⣿⣿⣿⣿⣿⣿
⣿⣷⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣤⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿
"""




import time

class Pokemon:
    def __init__(self, name, types, moves, EVs, pics, health='=============================='):
        self.name = name
        self.types = types
        self.moves = [(move, move_type) for move, move_type in moves]
        self.defense = EVs['DEFENSE']
        self.attack = EVs['ATTACK']
        self.pics = pics
        self.healthBar = 30
        self.health = health

    def fight(self, pokemon2):
        print("-----POKEMON BATTLE SIMULATOR-----")
        print(f"\n{self.name}")
        print(f"\nTYPE/ {self.types}")
        print(f"\nATTACK/ {self.attack}")
        print(f"\nDEFENSE/ {self.defense}")

        print(f"\n{pokemon2.name}")
        print(f"\nTYPE/ {pokemon2.types}")
        print(f"\nATTACK/ {pokemon2.attack}")
        print(f"\nDEFENSE/ {pokemon2.defense}")

        elements = ['Grass', 'Fire', 'Water']

        def calculate_effectiveness(move_type, defender_type):
            if move_type in elements and defender_type in elements:
                move_index = elements.index(move_type)
                defender_index = elements.index(defender_type)
                if (move_index - defender_index) % 3 == 1:  # Strong against next in cycle
                    return 2  # Super effective
                elif (move_index - defender_index) % 3 == 2:  # Weak against previous in cycle
                    return 0.5  # Not very effective
            return 1  # Neutral

        while pokemon2.healthBar > 0 and self.healthBar > 0:
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(self.pics)
            print(f"\n{pokemon2.name}\t\tHLTH\t{pokemon2.health}")
            print(pokemon2.pics)

            print(f'GO {self.name}!')
            for i, (move_name, move_type) in enumerate(self.moves):
                print(f'{i + 1}. {move_name}')
            index = int(input('PICK A MOVE: ')) - 1
            selected_move, move_type = self.moves[index]
            print(f'{self.name} used {selected_move}!')
            time.sleep(1)

            effectiveness = calculate_effectiveness(move_type, pokemon2.types)
            damage = self.attack * effectiveness

            if effectiveness == 2:
                print("\nIT'S SUPER EFFECTIVE!")
            elif effectiveness == 0.5:
                print("\nIT'S NOT VERY EFFECTIVE...")

            pokemon2.healthBar -= damage
            pokemon2.health = '=' * max(0, int(pokemon2.healthBar + 0.1 * pokemon2.defense))

            if pokemon2.healthBar <= 0:
                print(f"\n... {pokemon2.name} fainted")
                print(f"\n {self.name} has won!")
                break

            time.sleep(1)

            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(self.pics)
            print(f"\n{pokemon2.name}\t\tHLTH\t{pokemon2.health}")
            print(pokemon2.pics)

            time.sleep(0.5)

            print(f'GO {pokemon2.name}!')
            for i, (move_name, move_type) in enumerate(pokemon2.moves):
                print(f'{i + 1}. {move_name}')
            index = int(input('PICK A MOVE: ')) - 1
            selected_move, move_type = pokemon2.moves[index]
            print(f'{pokemon2.name} used {selected_move}!')
            time.sleep(1)

            effectiveness = calculate_effectiveness(move_type, self.types)
            damage = pokemon2.attack * effectiveness

            if effectiveness == 2:
                print("\nIT'S SUPER EFFECTIVE!")
            elif effectiveness == 0.5:
                print("\nIT'S NOT VERY EFFECTIVE...")

            self.healthBar -= damage
            self.health = '=' * max(0, int(self.healthBar + 0.1 * self.defense))

            if self.healthBar <= 0:
                print(f"\n... {self.name} fainted")
                print(f"\n {pokemon2.name} has won!")
                break


if __name__ == "__main__":
   
    

    Charmander = Pokemon('CHARMANDER', 'Fire', [('SCRATCH', 'Normal'), ('EMBER', 'Fire'), ('FLAMETHROWER', 'Fire'), ('TACKLE', 'Normal')], {'ATTACK': 4, 'DEFENSE': 2}, charmanderArt)
    Squirtle = Pokemon('SQUIRTLE', 'Water', [('TACKLE', 'Normal'), ('SURF', 'Water'), ('BUBBLE BLAST', 'Water'), ('WATERGUN', 'Water')], {'ATTACK': 3, 'DEFENSE': 3}, squirtleArt)

    Charmander.fight(Squirtle)
