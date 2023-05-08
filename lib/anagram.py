class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        match_list = []
        for item in word_list: 
            if sorted([letter for letter in self.word]) == sorted([letter for letter in item]):
                match_list.append(item)
        return match_list
        