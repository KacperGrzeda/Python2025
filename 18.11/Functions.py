def num_of_letters(text, num_of_letters):
    text = text.lower()
    letter_counts = { letter: text.count, { letter } for letter in letters}
    return letter_counts
text = ''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
'n', 'o', 'u', 'p', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z']
print(num_of_letters(text, letters))