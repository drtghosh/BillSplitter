int_1 = int(input())
int_2 = int(input())
last_one = int_2
if int_1 >= int_2:
    print(int_1)
else:
    print(int_2)
    last_one = int_1
print(last_one)