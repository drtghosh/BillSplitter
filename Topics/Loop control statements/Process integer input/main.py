# put your python code here
a, b = 10, 100
while True:
    enter = int(input())
    if enter < a:
        continue
    elif enter > b:
        break
    else:
        print(enter)
