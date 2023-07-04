import random

def generate_word(length):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    word = ''
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(consonants)
        else:
            word += random.choice(vowels)
    return word

# Generate 10 random words of length 5
for _ in range(10):
    word = generate_word(2)
    print(word)
