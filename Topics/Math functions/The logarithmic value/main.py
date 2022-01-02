import math

num_1 = int(input())
num_2 = int(input())
if num_2 <= 1:
    print(round(math.log(num_1), 2))
else:
    print(round(math.log(num_1, num_2), 2))