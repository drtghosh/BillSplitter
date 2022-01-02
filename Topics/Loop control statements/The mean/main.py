total = 0
count = 0
while True:
    num = input()
    if num == '.':
        break
    else:
        to_add = int(num)
        count += 1
        total += to_add

print(total / count)