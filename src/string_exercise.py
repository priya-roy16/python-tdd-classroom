class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        return input_str[::-1]

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        if character in vowels:
            return True
        else:
            return False

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        words_list = sentence.split(' ')
        max_len = 0
        result = ""
        for word in words_list:
            if(len(word) > max_len):
                max_len = len(word)
                result=word
        return result

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        words_list = text.split(" ")
        result = []
        for word in words_list:
            result.append(len(word))

        return result