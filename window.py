from tkinter import *  # Our GUI library
from pokemon import *
from PIL import Image, ImageTk
import matplotlib


def create_window(pokemon_selected: Pokemon):
    window = Tk()  # Instantiate an instance of window
    window.geometry("1920x1080")  # Sets the size of the window
    window.title("Pokedex")
    # Setting the icon at the top left
    icon = PhotoImage(file="images.png")
    window.iconphoto(True, icon)

    # Setting the background color
    window.config(background="#F5F5DC")

    # Convert the main color of the pokemon into a hex string
    main_hex_color = matplotlib.colors.cnames[f"{pokemon_selected.color}"]

    # Getting the image from the link given by the image link
    im = Image.open(requests.get(
        f"{pokemon_selected.imageLink}", stream=True).raw)
    # Resizeing the image of the pokemon
    im = im.resize((200, 200))

    # Convert the image into a TkInter PhotoImage format
    tkPhoto = ImageTk.PhotoImage(im)

    # Creating a Frame object to place each of the Labels
    frame = Frame(window, bg="#e1f7f3")

    # Labels are an area that holds text/images within a window
    mainLabel = Label(frame,
                      text=f"No. {pokemon_selected.id} {pokemon_selected.name.capitalize()}\n",
                      font=('Arial', 40, 'bold'),
                      fg=main_hex_color,
                      bg='black',
                      relief=SUNKEN,
                      bd=10,
                      padx=20,
                      image=tkPhoto,
                      compound='right',)
    mainLabel.pack()
    # Place function to choose where to display the label
    # mainLabel.place(x=560, y=10)

    # Creating the label  for the basic attributes of the pokemon
    text = f"""{pokemon_selected.genus}\n
    Type(s): {" ".join(str(x) for x in pokemon_selected._types_list)}\n
    Height: {pokemon_selected.height/3.048:.2f} ft\tWeight: {pokemon_selected.weight/4.536:.2f} lbs
    """.ljust(
        20)
    attributesLabel = Label(frame,
                            text=text,
                            font=("Vani", 20),
                            bg="black",
                            fg=main_hex_color,
                            bd=6,
                            padx=20,
                            relief=RAISED)
    attributesLabel.pack()

    # Creating the label for the list of stats
    stats = pokemon_selected.stats
    statsText = f"""HP:    {stats[0]}\nATK:   {stats[1]}\nDEF:   {stats[2]}\nSPATK: {stats[3]}\nSPDEF: {stats[4]}\nSPD:   {stats[5]}"""

    statsLabel = Label(frame,
                       text=statsText,
                       font=("Vanisa", 20),
                       fg=main_hex_color,
                       bg="black")
    statsLabel.pack()

    # Creating the label for the description
    descLable = Label(frame,
                      text=f"{pokemon_selected._description}".ljust(120),
                      font=("Terminal", 15),
                      fg="black",
                      bg="white",
                      relief=RAISED,
                      bd=6,
                      padx=20
                      )

    descLable.pack()
    frame.pack()

    window.mainloop()  # Opens to the window

    # Continue: https://www.youtube.com/watch?v=lyoyTlltFVU
