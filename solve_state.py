from hints_calculator import HintsCalculator
from tools import Tools


class SolveState(Tools):
    def __init__(self, possible_letters, number_of_characters, valid_words) -> None:
        self.possible_letters = possible_letters
        self.number_of_characters = number_of_characters
        self.valid_words = valid_words
        self.possible_final_answers = valid_words

    def get_submission_hints(self, input_word, target_word):
        hints_calculator = HintsCalculator(input_word, target_word)
        return hints_calculator.get_hints()

    def get_hint_pattern_to_frequency_map(self, input_word):
        hint_pattern_to_frequency_map = {}
        for target_word in self.possible_final_answers:
            hint_pattern = self.get_submission_hints(input_word, target_word)
            if hint_pattern in hint_pattern_to_frequency_map:
                hint_pattern_to_frequency_map[hint_pattern] += 1
            else:
                hint_pattern_to_frequency_map[hint_pattern] = 1

        return hint_pattern_to_frequency_map