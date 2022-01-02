# put your python code here
three_digit = int(input())
first_digit = three_digit % 10
second_digit = (three_digit // 10) % 10
third_digit = three_digit // 100
print(first_digit + second_digit + third_digit)