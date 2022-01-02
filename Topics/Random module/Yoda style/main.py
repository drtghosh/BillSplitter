import random
seed = 43

# your sentence is assigned to the variable
sentence = input().split()

# write your python code below
random.seed(seed)
random.shuffle(sentence)

# shows the message
print(' '.join(sentence))