max_cats = 0
cafe_to_go = None
while True:
    cafe = input()
    if cafe == 'MEOW':
        break
    else:
        try:
            name, cats = cafe.split()
        except ValueError:
            print('Get name and cats both!')
        if int(cats) > max_cats:
            max_cats = int(cats)
            cafe_to_go = name

print(cafe_to_go)