from random import choice
import string


def text_generator(frase_length):
	letters = string.ascii_lowercase + ' '
	monkey_guess = ''
	for _ in range(frase_length):
		monkey_guess += choice(letters)
	return monkey_guess


def text_comparison(frase, guess):
	count = 0
	matches = 0
	for _ in range(len(frase)):
		if frase[count] == guess[count]:
			matches += 1
		count += 1
	return matches


def monkey_guess(frase):
	frase_length = len(frase)
	count = 0
	best_match = [0, '']
	guess = False
	while not guess:
		count += 1
		monkey_prints = text_generator(frase_length)
		if monkey_prints == frase:
			print('Match found!')
			guess = True
		match = text_comparison(frase, monkey_prints)
		if match >= best_match[0]:
		#if match > best_match[0]:
			best_match = [match, monkey_prints]
		if count % 1000 == 0:
			print(f'On count {str(count)} best match is "{best_match[1]}".')
	return print(f'It took {str(count)} attempts to generate "{frase}".')


if __name__ == "__main__":
	monkey_guess('meth')