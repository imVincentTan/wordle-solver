from tools import Tools


class SolveState(Tools):
    def __init__(self, possible_letters, number_of_characters, valid_words) -> None:
        self.possible_letters = possible_letters
        self.number_of_characters = number_of_characters
        self.valid_words = valid_words
