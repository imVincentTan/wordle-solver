class Hint():
    def __init__(self, word_length):
        self.hints = ['-'] * word_length

    def get_hints_key(self):
        return self.convert_hints_to_string()

    def is_unset_hint(self, index):
        return self.hints[index] == '-'

    def is_green_hint(self, index):
        return self.hints[index] == 'g'

    def is_yellow_hint(self, index):
        return self.hints[index] == 'y'

    def is_grey_hint(self, index):
        return self.hints[index] == 'x'

    def convert_hints_to_string(self):
        return ''.join(self.hints)

    def set_green_hint(self, index):
        self.hints[index] = 'g'

    def set_yellow_hint(self, index):
        self.hints[index] = 'y'
    
    def set_grey_hint(self, index):
        self.hints[index] = 'x'
