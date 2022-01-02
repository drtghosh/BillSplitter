import math

input_int = int(input())
exponent = math.exp(input_int)
logistic = exponent / (exponent + 1)
print(round(logistic, 2))