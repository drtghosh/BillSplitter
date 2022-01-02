list_float = []
while True:
    enter = input()
    if enter == '.':
        break
    else:
        list_float.append(float(enter))

print(min(list_float))