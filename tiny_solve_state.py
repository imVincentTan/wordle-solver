from solve_state import SolveState
from wordlist import wordlist_small


class TinySolveState(SolveState):
    def __init__(self) -> None:
        self.possible_letters = self.get_english_alphabet()
        self.number_of_characters = 5
        self.valid_words = self.get_tiny_wordlist()

    def get_tiny_wordlist(self):
        self.get_smaller_wordlist(wordlist_small, 10)