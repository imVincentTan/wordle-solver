from hints_calculator import HintsCalculator
from solve_state import SolveState
from wordlist import wordlist_small


class StandardSolveState(SolveState):
    def __init__(self) -> None:
        self.possible_letters = self.get_english_alphabet()
        self.number_of_characters = 5
        self.valid_words = wordlist_small
        self.possible_final_answers = wordlist_small

    def get_submission_hints(self, input_word, target_word):
        hints_calculator = HintsCalculator(input_word, target_word)
        return hints_calculator.get_hints()

