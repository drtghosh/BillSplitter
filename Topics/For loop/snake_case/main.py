lower_camel = input()
snake = ''
for char in lower_camel:
    if char.islower():
        snake += char
    else:
        snake_add = f'_{char.lower()}'
        snake += snake_add
print(snake)