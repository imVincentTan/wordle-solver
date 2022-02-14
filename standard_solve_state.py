from solve_state import SolveState
from wordlist import wordlist_small


class StandardSolveState(SolveState):
    def __init__(self) -> None:
        self.possible_letters = self.get_english_alphabet()
        self.number_of_characters = 5
        self.valid_words = wordlist_small
