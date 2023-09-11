from pokemon import *
from window import *


def main():
    # Asks the user to enter a pokemon (Enter x to quit)
    while (pokemon := input("Enter a pokemon or a pokedex number: (Press x to exit) ").lower()) != "x":
        # Creating a new pokemon object
        try:
            pokemon_selected = Pokemon(pokemon)
            create_window(pokemon_selected)
        except:
            continue


if __name__ == '__main__':
    main()
