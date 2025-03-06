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




class pokemon :
    def __init__(self, name, types, moves, EVs, pics, health ='=============================='):
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
    
    
    

        element = ['Grass', 'Fire', 'Water']

        def calculate_effectiveness(move_type, defender_type):
            for i, k in enumerate(element):
                if move_type == k:
                    if defender_type == element[(i + 1) % 3]:
                        return 2  # Super effective
                    elif defender_type == element[(i + 2) % 3]:
                        return 0.5  # Not very effective
            return 1  # Neutral



        while (pokemon2.healthBar > 0) and (self.healthBar > 0):

            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(self.pics)
            print(f"\n{pokemon2.name}\t\tHLTH\t{pokemon2.health}")
            print(pokemon2.pics)

            print(f'GO {self.name}!')
            for i, x in enumerate(self.moves):
                print(f'{i + 1}.', x)
            index = int(input('PICK A MOVE'))
            print(f'{self.name} used {self.moves[index - 1]}!')
            time.sleep(1)
            
            effectiveness = calculate_effectiveness(move_type, pokemon2.types)
            damage = self.attack * effectiveness

            if effectiveness == 2:
                print("\nIT'S SUPER EFFECTIVE!")
            elif effectiveness == 0.5:
                print("\nIT'S NOT VERY EFFECTIVE...")

            print(f"pokemon2's health: {pokemon2.healthBar}")
            pokemon2.healthBar -= damage
            pokemon2.health = '=' * int(pokemon2.healthBar + 0.1 * pokemon2.defense)
            

            print(f'\n{string_1_attack}')

            
                

            for j in range(int(pokemon2.healthBar+.1 * pokemon2.defense)):
                pokemon2.health += '='

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

            print(f"{self.name} health: {self.healthBar}")
            

            
    
            print(f'GO {pokemon2.name}!')
            for i, x in enumerate(pokemon2.moves):
                print(f'{i + 1}.', x)
            index = int(input('PICK A MOVE'))
            print(f'{pokemon2.name} used {pokemon2.moves[index - 1]}!')
            time.sleep(1)
            

            self.healthBar -= pokemon2.attack
            self.health = ''

            print(f'\n{string_2_attack}')

            for j in range(int(self.healthBar+.1 * self.defense)):
                self.health += '='

            
            if self.healthBar <= 0:
                print(f"\n... {self.name} fainted")
                print(f"\n {pokemon2.name} has won!")
                break




if __name__ == "__main__":
    
    Charmander = pokemon('CHARMANDER', 'Fire', [('SCRATCH', 'Normal'), ('EMBER', 'Fire'), ('FLAMETHROWER', 'Fire'), ('TACKLE', 'Normal')], {'ATTACK': 4, 'DEFENSE': 2}, charmanderArt)
    Squirtle = pokemon('SQUIRTLE', 'Water', [('TACKLE', 'Normal'), ('SURF', 'Water'), ('BUBBLE BLAST', 'Water'), ('WATERGUN', "Water")], {'ATTACK': 3, 'DEFENSE': 3}, squirtleArt)
    # Bulbasaur = pokemon('BULBASAUR', 'Grass',['VINE WHIP', 'RAZOR LEAF', 'TACKLE', 'LEECH SEED'], {'ATTACK': 2, 'DEFENSE': 4}, bulbasaurArt)

    Charmander.fight(Squirtle)

    