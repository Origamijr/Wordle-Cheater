import keyboard
from wordfreq import word_frequency
import sys

with open('wordle-answers-alphabetical.txt') as f:
    dictionary = f.readlines()

wordfreqs = dict()
for word in dictionary:
    word = word.strip()
    wordfreqs[word] = word_frequency(word, lang='en')

while True:
    # Handle one puzzle
    correct_letters = []
    letter_positions = [[], [], [], [], []]
    incorrect_letters = []
    while True:
        # Handle one word attempt
        guess = list("_____")
        pos = 0

        # Capture word input
        while True:
            sys.stdout.write('\rCapturing input: ' + ''.join(guess))
            sys.stdout.flush()
            event = keyboard.read_event()
            if event.event_type == 'down':
                key = event.name
                if len(key) == 1 and key.isalpha() and pos < 5:
                    guess[pos] = key
                    pos += 1
                elif key == 'backspace' and pos > 0:
                    pos -= 1
                    response[pos] = '_'
                elif key == 'enter' and pos == 5:
                    sys.stdout.write('\n')
                    break
                elif key == 'esc':
                    exit()
        guess = ''.join(guess)
        
        # Record response
        response = list("_____")
        pos = 0
        solved = False
        while True:
            sys.stdout.write('\rInput response: ' + ''.join(response))
            sys.stdout.flush()
            event = keyboard.read_event()
            if event.event_type == 'down':
                key = event.name
                if key == '1' and pos < 5:
                    response[pos] = '!'
                    pos += 1
                elif key == '2' and pos < 5:
                    response[pos] = '?'
                    pos += 1
                elif key == 'space' and pos < 5:
                    response[pos] = '-'
                    pos += 1
                elif key == 'backspace' and pos > 0:
                    pos -= 1
                    response[pos] = '_'
                elif key == '3' and pos < 5:
                    solved = True
                    sys.stdout.write('\n')
                    break
                elif key == '3' and pos == 5:
                    sys.stdout.write('\n')
                    break
                elif key == 'esc':
                    exit()
        if solved:
            print(f'Congrats. Word was {guess}. Restarting...')
            break

        # update known information
        for i, r in enumerate(response):
            if r == '!':
                correct_letters.append(guess[i])
                letter_positions[i] = guess[i]
            elif r == '?' and isinstance(letter_positions[i], list):
                correct_letters.append(guess[i])
                letter_positions[i].append(guess[i])
            else:
                incorrect_letters.append(guess[i])
        incorrect_letters = [letter for letter in incorrect_letters if letter not in correct_letters]

        # find valid words
        valid_words = []
        for word in wordfreqs:
            if any(letter in word for letter in incorrect_letters): continue
            if not all(letter in word for letter in correct_letters): continue
            valid = True
            for ref, info in zip(word, letter_positions):
                if (isinstance(info, str) and ref != info or
                    isinstance(info, list) and ref in info):
                    valid = False
                    break
            if valid:
                valid_words.append((wordfreqs[word], word))
        
        # display top valid words
        valid_words.sort()
        if len(valid_words) == 0:
            print('mistakes were made. Restarting...')
            break
        else:
            print(f'{len(valid_words)} solutions found. Try {valid_words[:-4:-1]}')