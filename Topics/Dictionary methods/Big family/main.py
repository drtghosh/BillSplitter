# The following lines create dictionaries from the input. Do not modify them, please
first_family = json.loads(input())
second_family = json.loads(input())

# Work with the 'first_family' and 'second_family' and create a new dictionary
all_family = first_family
for key, value in second_family.items():
    all_family.update({key: value})
print(all_family)