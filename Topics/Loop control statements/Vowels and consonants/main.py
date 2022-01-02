vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
text = input()
for char in text:
    if char in vowels:
        print('vowel')
    elif char in consonants:
        print('consonant')
    else:
        break