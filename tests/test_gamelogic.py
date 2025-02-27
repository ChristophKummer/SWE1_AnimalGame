from AnimalGame.farm.animals import Cow
from AnimalGame.gamestructure import Player
from AnimalGame.wild.animals import Wolf

def test_cow(capsys):
    new_cow = Cow()   
    new_player = Player("John")
    new_player.feed(new_cow)
    captured = capsys.readouterr()
    assert captured.out == "John fed 1-Cow\nCow makes noise while eating:  Moo\n"
    
def test_wolf(capsys):
    new_cow = Cow()
    new_wolf = Wolf()
    new_wolf.hunt(new_cow)
    