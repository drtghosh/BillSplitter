scores = input().split()
# put your python code here
incorrect = 0
correct = 0
for ans in scores:
    if ans == 'I':
        incorrect += 1
        if incorrect == 3:
            break
    else:
        correct += 1

if incorrect < 3:
    print('You won')
else:
    print('Game over')

print(correct)