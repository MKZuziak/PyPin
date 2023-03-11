import re

class string_transformer():
    def __init__(self) -> None:
        # Defining all possible ends of a syllab - by punctuation mark or a letter.
        self.syllab_beginning = ['b', 'p', 'm', 'f', 'd', 't', 'l',\
        'k', 'j', 'q', 'x', 'z', 'c', 's', 'y', 'w']
        self.syllab_end = ['a', 'e', 'i', 'o', 'u', 'ü', 'g', 'n', 'r']
        self.punctuation_mark = ['.', '?', '!', ':', ';', '-', '[', ']',\
             '{', '}', '(', ')', '‘', '“', ' ', '\n', ',']

        # Defining all the possible tones
        self.tones = ['ā', 'ē', 'ī', 'ō', 'ū', \
            'ǖ', 'á', 'é', 'í', 'ó', 'ú', 'ǘ', 'ǎ',\
                'ě', 'ǐ', 'ǒ', 'ǔ', 'ǚ', 'à', 'è', 'ì', 'ò', 'ù', 'ǜ']
        self.vowel = ['a', 'e', 'i', 'o', 'u']
        self.i_tones = ['ī', 'ǐ', 'ì', 'í']
        
        # Initializing regex object.
        self.tones_regex = re.compile('ā|ē|ī|ō|ū|ǖ|á|é|í|ó|ú|ǘ|ǎ|ě|ǐ|ǒ|ǔ|ǚ|à|è|ì|ò|ù|ǜ')
        self.number_regex = re.compile('(?<=[a-zA-Z])1|2|3|4')

        # Declaring a mapping of each tone to corresponding letter that should be inserted.
        self.tone_letter_mapping = {
            tone_letter : letter 
            for tone_letter, letter in zip(self.tones, ['a', 'e', 'i', 'o', 'u', 'ü']*4)}
        
        # Each number is 
        self.number_tone_mapping = {
            "1": {letter: tone_letter for tone_letter, letter in zip(self.tones[:6], ['a', 'e', 'i', 'o', 'u', 'ü'])},
            "2": {letter: tone_letter for tone_letter, letter in zip(self.tones[6:13], ['a', 'e', 'i', 'o', 'u', 'ü'])},
            "3": {letter: tone_letter for tone_letter, letter in zip(self.tones[12:19], ['a', 'e', 'i', 'o', 'u', 'ü'])},
            "4": {letter: tone_letter for tone_letter, letter in zip(self.tones[18:], ['a', 'e', 'i', 'o', 'u', 'ü'])}
        }
        
        # Declaring each tone to corresponding number that should be inserted at the
        # end of the syllab.
        tone_numbers = []
        for number in range(1, 5):
            tone_numbers.extend([str(number)]*6)        
        self.tones_to_numbers = {tone : number 
            for tone, number in zip(self.tones, tone_numbers)
        }
        
    def to_numbers(self, text: str):
        assert isinstance(text, str), "Wrong argument passed to the class constructor."
        self.text = text
        
        while True:
            match = re.search(self.tones_regex, self.text)
            if match:
                shifting_index = match.start()
                security_counter = 0
                while self.text[shifting_index] \
                    not in self.syllab_end and \
                        self.text[shifting_index]\
                    not in self.punctuation_mark and\
                        self.text[shifting_index]\
                    not in self.syllab_beginning:
                        shifting_index += 1
                        security_counter += 1
                if self.text[shifting_index] in self.syllab_end:
                    if self.text[shifting_index] == "n" and self.text[shifting_index + 1] == "g":
                        self.text = self.text[:shifting_index + 2] + \
                            self.tones_to_numbers[self.text[match.start()]] + \
                                self.text[shifting_index + 2:]
                    if self.text[shifting_index] == "g" and self.text[shifting_index - 1] == "i":
                        pass # TODO
                    else:
                        self.text = self.text[:shifting_index + 1] + \
                            self.tones_to_numbers[self.text[match.start()]] + \
                                self.text[shifting_index + 1:]
                elif self.text[shifting_index] in self.punctuation_mark\
                    or self.text[shifting_index] in self.syllab_beginning:
                    self.text = self.text[:shifting_index] + \
                         self.tones_to_numbers[self.text[match.start()]] + \
                            self.text[shifting_index:]
                elif security_counter > 10:
                    print("An error occued - program terminated to avoid entering into endless loop.")
                    return
                self.text = self.text[:match.start()] + self.tone_letter_mapping[self.text[match.start()]] + \
                    self.text[match.start() + 1:]
            else:
                break
    
        return self.text
    
    def to_marks(self, text: str):
        assert isinstance(text, str), "Wrong argument passed to the class constructor."
        self.text = text
        while True:
            match = re.search(self.number_regex, self.text)
            if match:
                tone = self.text[match.start()]
                shifting_index = match.start() - 1
                security_counter = 0
                while self.text[shifting_index] not in self.vowel:
                    shifting_index -= 1
                    security_counter += 1
                if self.text[shifting_index] == 'i' and self.text[shifting_index-1] in self.vowel:
                    # We want to replace vowel preceeding i, not i itself.
                    shifting_index -= 1
                    self.text = self.text[:shifting_index] + self.number_tone_mapping[tone][self.text[shifting_index]] + \
                        self.text[shifting_index + 1:]
                    # Removes the tone number
                    self.text = self.text[:match.start()] + self.text[match.start()+1:]
                elif self.text[shifting_index] == 'o' and self.text[shifting_index-1] == 'a':
                    # We want to replace vowel preceeding i, not i itself.
                    shifting_index -= 1
                    self.text = self.text[:shifting_index] + self.number_tone_mapping[tone][self.text[shifting_index]] + \
                        self.text[shifting_index + 1:]
                    # Removes the tone number
                    self.text = self.text[:match.start()] + self.text[match.start()+1:]
                elif self.text[shifting_index] == 'u' and self.text[shifting_index-1] == 'o':
                    # We want to replace vowel preceeding i, not i itself.
                    shifting_index -= 1
                    self.text = self.text[:shifting_index] + self.number_tone_mapping[tone][self.text[shifting_index]] + \
                        self.text[shifting_index + 1:]
                    # Removes the tone number
                    self.text = self.text[:match.start()] + self.text[match.start()+1:]

                elif self.text[shifting_index] in self.vowel:
                    # Replaces the tone
                    self.text = self.text[:shifting_index] + self.number_tone_mapping[tone][self.text[shifting_index]] + \
                        self.text[shifting_index + 1:]
                    # Removes the tone number
                    self.text = self.text[:match.start()] + self.text[match.start()+1:]
                elif security_counter > 10:
                    print("An error occued - program terminated to avoid entering into endless loop.")
                    return
            else:
                # BREAK
                break
        
        return self.text