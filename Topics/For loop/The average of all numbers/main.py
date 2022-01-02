# put your python code here
start = int(input())
end = int(input()) + 1
summation = 0
count = 0
for i in range(start, end):
    if i % 3 == 0:
        summation += i
        count += 1
print(summation / count)