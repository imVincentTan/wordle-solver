from solve_state import SolveState
from wordlist import wordlist_small


class TinySolveState(SolveState):
    def __init__(self) -> None:
        self.possible_letters = {'a', 'b', 'c'}
        self.number_of_characters = 2
        self.valid_input_words = ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
        self.possible_final_answers = ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']

