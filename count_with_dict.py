from pprint import pprint

letter_counts = {}

with open('DATA/words.txt') as words_in:
    for line in words_in:
        letter = line[0]
        if letter not in letter_counts:
            letter_counts[letter] = 0

        letter_counts[letter] += 1

pprint(letter_counts)