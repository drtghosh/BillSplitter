start = 1
end = 101
for i in range(start, end):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    if i % 3 == 0 and i % 5 != 0:
        print('Fizz')
    if i % 3 != 0 and i % 5 == 0:
        print('Buzz')
    if i % 3 != 0 and i % 5 != 0:
        print(i)