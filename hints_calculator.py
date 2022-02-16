from hint import Hint


class HintsCalculator():
    def __init__(self, input_word, target_word) -> None:
        self.input_word = input_word
        self.target_word = target_word
        self.hints = Hint(len(input_word))
        self.target_word_letter_count = {}

    def get_hints(self):
        self.calculate_hints()
        return self.hints.convert_hints_to_string()

    def calculate_hints(self):
        hints = [''] * len(self.input_word)
        self.calculate_target_word_letter_count()

        self.calculate_green_hints()
        self.calculate_yellow_hints()

    def calculate_target_word_letter_count(self):
        self.target_word_letter_count = {}
        for letter in self.target_word:
            if letter in self.target_word_letter_count:
                self.target_word_letter_count[letter] += 1
            else:
                self.target_word_letter_count[letter] = 1

    def calculate_green_hints(self):
        for letter_index, letter in enumerate(self.input_word):
            if self.should_be_green_hint(letter_index, letter):
                self.set_hint('green', letter_index, letter)

    def should_be_green_hint(self, letter_index, letter):
        return self.target_word[letter_index] == letter

    def set_hint(self, hint_colour, letter_index, letter):
        if hint_colour == 'green':
            self.hints.set_green_hint(letter_index)
        elif hint_colour == 'yellow':
            self.hints.set_yellow_hint(letter_index)
        self.target_word_letter_count[letter] -= 1

    def calculate_yellow_hints(self):
        for letter_index, letter in enumerate(self.input_word):
            if self.should_be_yellow_hint(letter_index, letter):
                self.set_hint('yellow', letter_index, letter)

    def should_be_yellow_hint(self, letter_index, letter):
        return not self.hints.is_green_hint(letter_index) \
                and letter in self.target_word_letter_count \
                and self.target_word_letter_count[letter] > 0
