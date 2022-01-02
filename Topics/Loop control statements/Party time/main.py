guests = 0
guest_names = []
while True:
    name = input()
    if name == '.':
        break
    else:
        guest_names.append(name)
        guests += 1
print(guest_names)
print(guests)