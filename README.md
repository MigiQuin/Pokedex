# The Pokemon Pokedex
#### Description: This is a python program that prompts the user to enter a Pokemon or a Pokedex Number, and shows the user the stats and characteristics of the chosen pokemon

## Table of contents
* [Video Demo](#Video-Demo-from-Youtube)
* [Prerequesites](#Prerequesites)
* [Icon Photo](#Icon-Photo)
* [TKinter Linux](#Install-Tkinter-in-Linux)
* [Usage](#Usage)
* [API Used](#API-Documentation:)
* [Contact Me](#Contact-Me)

## Video Demo from Youtube
Here is a link to show what my goals were in doing developing this project
https://youtu.be/z4OCsJQDAgQ

## Prerequesites

You will need to install Pillow for this application.

Documentation: https://pillow.readthedocs.io/en/stable/
```zsh
pip install pillow
```
matplotlib is a library that is used to convert Colors into their Hex-Values and vise versa

Documentation: https://matplotlib.org/stable/index.html

```zsh
pip install matplotlib
```
We will need the requests library to handle requests to and from the Poke API

Documentation: https://pypi.org/project/requests/
```zsh
python -m pip install requests
```

## Icon Photo
A photo is required for the icon of this application.
If the image is not properly loaded, comment out lines 12-14 in window.py

```zsh
curl -o images.png https://w7.pngwing.com/pngs/283/854/png-transparent-game-pokeball-pokemon-pokemon-go-pokemongo-pokestop-pokemon-go-addict-icon.png
```



## Install Tkinter in Linux
Many Linux versions of Python do not come with tkinter supported, you may need to install it manually

#### For Debian Based Linux

```zsh
sudo apt-get install python-tk
```

#### For Arch based Linux

```zsh
sudo pacman -S tk
```

#### For Fedora based Linux

```zsh
sudo dnf install python3-tkinter
```

## Usage

python ./project.py
Enter a pokemon or a pokedex number: (Press x to exit) [ENTER POKEMON ID OR NAME HERE]

## API Documentation:
#### RESTful PokeAPI Interface:

Link: https://pokeapi.co/docs/v2

## Contact Me:

Email: MigiQuinones6@gmail.com
