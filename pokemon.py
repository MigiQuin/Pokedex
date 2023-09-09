import requests


class Pokemon:
    def __new__(self, pokemon):
        response = requests.get(
            "https://pokeapi.co/api/v2/pokemon/" + pokemon)
        response.raise_for_status()
        pokemon_entry = response.json()
        """
        except requests.exceptions.ConnectionError:
            print("A connection error occurred. Please check your internet connection.")
            return
        except requests.exceptions.Timeout:
            print("The request timed out.")
            return
        except requests.exceptions.HTTPError:
            prpokemon_entryn.")
            return
        except requests.exceptions.RequestException as e:
            print("An error occurred: ", e)
            return"""

        # Pokedex entry number of the pokemon
        self._id = pokemon_entry["id"]

        # Get the name of the pokemon
        self._name = pokemon_entry["forms"][0]["name"]

        # Stores the list of numbers from the API into a list
        self._stats_list = []
        for stat in pokemon_entry["stats"]:
            self._stats_list.append(stat["base_stat"])

        # From that list, we get the stats of each of the pokemon
        self._hp = self._stats_list[0]
        self._attack = self._stats_list[1]
        self._defense = self._stats_list[2]
        self._special_attack = self._stats_list[3]
        self._special_defense: self._stats_list[4]
        self._speed = self._stats_list[5]

        # Getting the type of the pokemon, putting it into the list because a pokemon might have two types (ex Charizards -> Fire, Flying)
        self._types_list = []
        for type in pokemon_entry["types"]:
            self._types_list.append(type['type']['name'])

        # Getting the height and weight of the pokemon
        self._height = pokemon_entry["height"]  # decimetres.
        self._weight = pokemon_entry["weight"]  # hectograms.
        # This API will get the descriptions of the pokemons
        response2 = requests.get(
            "https://pokeapi.co/api/v2/pokemon-species/" + pokemon)

        pokemon_species = response2.json()

        # NOTE For the description, there can be multiple entries in English depending on the version of the game
        # For simplicity we will only focus on the latest entry we can find
        for species in pokemon_species["flavor_text_entries"]:
            if species["language"]["name"] == "en":
                self._description = species["flavor_text"]

        # The genus of the pokemon: Ex Pikachu is the "Mouse Pokemon"
        for species in pokemon_species["genera"]:
            if species["language"]["name"] == "en":
                self._genus = species["genus"]

        # Get's the color of the pokemon, if the color is black, we will invert it to white to show on the window
        if pokemon_species["color"]["name"] == 'black':
            self._color = 'white'
        else:
            self._color = pokemon_species["color"]["name"]

        # Getting the front image link for what the pokemon looks like
        self._imageLink = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{self._id}.png"

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def stats(self):
        return self._stats_list

    @property
    def description(self):
        return self._description

    @property
    def height(self):
        return self._height

    @property
    def weight(self):
        return self._weight

    @property
    def genus(self):
        return self._genus

    @property
    def color(self):
        return self._color

    @property
    def imageLink(self):
        return self._imageLink
