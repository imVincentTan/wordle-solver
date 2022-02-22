from math import log2
from hints_calculator import HintsCalculator
from tools import Tools


class SolveState(Tools):
    def __init__(self, possible_letters, number_of_characters, valid_words) -> None:
        self.possible_letters = possible_letters
        self.number_of_characters = number_of_characters
        self.valid_input_words = valid_words
        self.possible_final_answers = valid_words

    def get_submission_hints(self, input_word, target_word):
        hints_calculator = HintsCalculator(input_word, target_word)
        return hints_calculator.get_hints()

    def get_sorted_word_to_expected_score(self):
        # TODO: improve algorithm to be faster
        word_score_pairs = []
        for input_word in self.valid_input_words:
            word_score_pairs.append([input_word, self.get_expected_score(input_word)])
        word_score_pairs.sort(key=lambda x: x[1], reverse=True)
        return word_score_pairs

    def get_expected_score(self, input_word):
        hint_pattern_to_frequency_map = self.get_hint_pattern_to_frequency_map(input_word)
        score = 0
        for key in hint_pattern_to_frequency_map:
            score += self.get_score_gained_by_occurrences(hint_pattern_to_frequency_map[key])
        return score

    def get_score_gained_by_occurrences(self, occurrences):
        probability_of_hint = occurrences / self.get_number_of_valid_inputs()
        weight = log2(1/probability_of_hint)
        return probability_of_hint * weight

    def get_number_of_valid_inputs(self):
        return len(self.valid_input_words)

    def get_hint_pattern_to_frequency_map(self, input_word):
        hint_pattern_to_frequency_map = {}
        for target_word in self.valid_input_words:
            hint_pattern = self.get_submission_hints(input_word, target_word)
            if hint_pattern in hint_pattern_to_frequency_map:
                hint_pattern_to_frequency_map[hint_pattern] += 1
            else:
                hint_pattern_to_frequency_map[hint_pattern] = 1

        return hint_pattern_to_frequency_map
