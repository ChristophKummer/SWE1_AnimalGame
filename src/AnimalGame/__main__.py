import tomllib
from pathlib import Path
from .gamestructure import Player, Animal
from .farm.animals import Chicken, Cow, Parrot
from typeguard import TypeCheckError
from .wild.animals import Wolf

# Main game loop
def do_main_loop(player: Player, animals: list[Animal]):
    for animal in animals:
        player.feed(animal)
        animal.display_info()

    
if __name__ == "__main__":
    p = Path(__file__).parent / Path("config.toml")
    with open(p, mode="rb") as fp:
        config = tomllib.load(fp)

    # Setup game
    animal_classes = {"chicken": Chicken, "cows": Cow, "parrots": Parrot}
    animals = [animal_classes[name]() for name, count in config["Animals"].items() for _ in range(count)]

    # Create a player with name
    player = Player(config["PlayerInfo"]["name"])

    # Exception handling
    wolf = Wolf()
    try:
        wolf.hunt(player) #type: ignore
    except TypeCheckError:
        print("\nEin wilder Wolf kann keinen Spieler angreifen\n")

    wolf.hunt(animals[0])

    do_main_loop(player, animals)
    
