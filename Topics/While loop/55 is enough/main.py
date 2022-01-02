# put your code here
count = 0
flag = 55
summed = 0
number = int(input())
while number != flag:
    count += 1
    summed += number
    number = int(input())

print(count)
print(summed)
print(round(summed / count))