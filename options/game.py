from enum import Enum
from utils import clear_screen

from options.menu import ExitGameException, MenuOption

ABANDON_GAME_OPT = "0"
ASK_CLUE_OPT = "1"
BUY_CLUE_OPT = "2"
ASK_HELP_OPT = "3"
BUY_CLUE_OPT = "4"

class GameOpt(Enum):
    ABANDON_GAME_OPT = 1
    ASK_CLUE = 2
    BUY_CLUE = 3
    ASK_HELP = 4
    BUY_HELP = 5

    @classmethod
    def from_input(cls, inp):
        if inp == ABANDON_GAME_OPT:
            return GameOpt.ABANDON_GAME_OPT
        elif inp == ASK_CLUE_OPT:
            return GameOpt.ASK_CLUE
        elif inp == BUY_CLUE_OPT:
            return GameOpt.BUY_CLUE
        elif inp == ASK_HELP_OPT:
            return GameOpt.ASK_HELP
        elif inp == BUY_HELP_OPT:
            return GameOpt.BUY_HELP
        else:
            return None
            
    def execute(self, juego):
        match self:
            case GameOpt.ABANDON_GAME_OPT:
                if self.ask_abandon_confirmation():
                    raise ExitGameException
            case GameOpt.ASK_CLUE:
                juego.use_basic_clue()
            case GameOpt.BUY_CLUE:
                juego.buy_basic_clue()
            case GameOpt.ASK_HELP:
                juego.use_hint_clue()
            case GameOpt.BUY_HELP:
                juego.buy_hint_clue()

    def ask_abandon_confirmation(self):
        if self == GameOpt.ABANDON_GAME_OPT:
            print("\n")
            while True:
                print("¿Estas seguro de que deseas abandonar la partida?")
                print("0. Si")
                print("1. No\n")
                inp = input("- ").strip()
                clear_screen()
                if inp == "0":
                    return True
                if inp == "1":
                    return False
                MenuOption.show_incorrect_option_message()
