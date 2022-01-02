word = input()
answer = 'Palindrome'
word_size = len(word)
half_size = word_size // 2
for i in range(half_size):
    if word[i] != word[word_size - i - 1]:
        answer = 'Not palindrome'
        break
print(answer)