from project import *
from pokemon import *

import pytest


def test_create_pokemon():
    pikachu = Pokemon('pikachu')
    assert pikachu.color == 'yellow'
    assert pikachu.id == 25
    assert pikachu.genus == 'Mouse Pokémon'


def test_pokedex_num():
    squirtle = Pokemon('7')
    assert squirtle.color == 'blue'
    assert squirtle.name == 'squirtle'
    assert squirtle.genus == 'Tiny Turtle Pokémon'


def test_invalid_pokemon():
    with pytest.raises(requests.exceptions.HTTPError) as e:
        inv = Pokemon('invalidate')
