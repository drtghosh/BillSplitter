# put your python code here
first = int(input())
total = first
if first == 0:
    print(0)
else:
    sos = first ** 2
    while total != 0:
        enter = int(input())
        total += enter
        sos += enter ** 2
    print(sos)