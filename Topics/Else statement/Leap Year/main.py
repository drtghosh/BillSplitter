# put your python code here
year = int(input())
unlucky_number = 100
lucky_number = 400
if year % 4 == 0:
    if year % unlucky_number == 0:
        if year % lucky_number == 0:
            print("Leap")
        else:
            print("Ordinary")
    else:
        print("Leap")
else:
    print("Ordinary")