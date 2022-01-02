number = int(input())
word = input()

# write a condition for plurals
if number != 1:
    word = f'{word}s'

print(number, word)