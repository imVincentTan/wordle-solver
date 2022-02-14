class Tools():
    def get_english_alphabet(self):
        alphabet = set()
        for char_ascii in range(ord('a'), ord('z') + 1):
            alphabet.add(chr(char_ascii))
        return alphabet

    def get_smaller_wordlist(self, starting_wordlist, max_per_letter_start):
        temp_wordlist = starting_wordlist
        temp_wordlist.sort()

        start_letter = temp_wordlist[0][0]
        current_letter_start_count = 0
        smaller_list = []

        for word in temp_wordlist:
            if current_letter_start_count < max_per_letter_start and word.startswith(start_letter):
                smaller_list.append(word)
                current_letter_start_count += 1
            else:
                if not word.startswith(start_letter):
                    start_letter = word[0]
                    current_letter_start_count = 0
                    if current_letter_start_count < max_per_letter_start:
                        smaller_list.append(word)
                        current_letter_start_count += 1

        return smaller_list
