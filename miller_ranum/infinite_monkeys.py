from random import choice
import string


class Infinite_Monkey:
    def __init__(self, frase):
        self.frase = frase
        self._frase_length = len(frase)
        self._count = 0
        self._result = self.monkey_guess(self.frase)

    @property
    def result(self):
        return self._result

    def monkey_prints(self, frase_length):
        letters = string.ascii_lowercase + ' '
        monkey_guess = ''
        for _ in range(frase_length):
            monkey_guess += choice(letters)
        return monkey_guess

    def monkey_compares(self, guess):
        letter_count = 0
        letters_matched = 0
        for _ in range(self._frase_length):
            if self.frase[letter_count] == guess[letter_count]:
                letters_matched += 1
            letter_count += 1
        return letters_matched

    def monkey_guess(self, frase):
        best_match = [0, '']
        found = False
        while not found:
            self._count += 1
            attempt = self.monkey_prints(self._frase_length)
            if attempt == frase:
                print('Match found!')
                found = True
            letters_matched_in_attempt = self.monkey_compares(attempt)
            if letters_matched_in_attempt >= best_match[0]:
                best_match = [letters_matched_in_attempt, attempt]
            if self._count % 1000 == 0:
                print(f'On count {str(self._count)} best match is "{best_match[1]}".')
        return f'It took {str(self._count)} attempts to generate "{self.frase}".'


if __name__ == "__main__":
    first_try = Infinite_Monkey('meth')
    second_try = Infinite_Monkey('meth')
    third_try = Infinite_Monkey('meth')
    print(f'\nFirst try:\n{first_try.result}')
    print(f'\nSecond try:\n{second_try.result}')
    print(f'\nThird try:\n{third_try.result}\n')