# write your code here
import random

print("Enter the number of friends joining (including you):")
people_joining = int(input())
names_joining = []
if people_joining <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(people_joining):
        name = input()
        names_joining.append(name)
    print("Enter the total bill value:")
    total_bill = int(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky = input()
    if lucky == 'Yes':
        lucky_one = random.choice(names_joining)
        print(f'{lucky_one} is the lucky one!')
        bill_each = round(total_bill / (people_joining - 1), 2)
        bill_dict = dict.fromkeys(names_joining, bill_each)
        bill_dict[lucky_one] = 0
    else:
        print('No one is going to be lucky')
        bill_each = round(total_bill / people_joining, 2)
        bill_dict = dict.fromkeys(names_joining, bill_each)
    print(bill_dict)
