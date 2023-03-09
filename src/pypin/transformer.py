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
        
        
    def to_numbers(self, text: str):
        assert isinstance(text, str), "Wrong argument passed to the class constructor."
        self.text = text
        # Initializing regex object.
        self.tones_regex = re.compile('ā|ē|ī|ō|ū|ǖ|á|é|í|ó|ú|ǘ|ǎ|ě|ǐ|ǒ|ǔ|ǚ|à|è|ì|ò|ù|ǜ')
        
        # Declaring a mapping of each tone to corresponding letter that should be inserted.
        self.tone_letter_mapping = {
            tone_letter : letter 
            for tone_letter, letter in zip(self.tones, ['a', 'e', 'i', 'o', 'u', 'u']*4)}
        
        # Declaring each tone to corresponding number that should be inserted at the
        # end of the syllab.
        tone_numbers = []
        for number in range(1, 5):
            tone_numbers.extend([str(number)]*6)        
        self.tones_to_numbers = {tone : number 
            for tone, number in zip(self.tones, tone_numbers)
        }
        print(self.tones_to_numbers)

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
                    break
                self.text = self.text[:match.start()] + self.tone_letter_mapping[self.text[match.start()]] + \
                    self.text[match.start() + 1:]
            else:
                break
    
        return self.text
            




#test = initialize_transformer("""Xǔduō zài zhōngguó yìnshuā de shūjí shǐyòng hùnhé zìtǐ, 
                                #yuán yīn hé shēngdiào biāojì yǐ yǔ zhōuwéi wénběn bùtóng de zìtǐ chéngxiàn, 
                                #wǎngwǎng shǐ cǐ lèi pīnyīn wénběn zài yìnshuā shàng xiǎndé bènzhuō.""")
#new_text = test.to_numbers()
#print(new_text)