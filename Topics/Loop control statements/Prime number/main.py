number = int(input())
prime = True
if number < 2:
    print("This number is not prime")
else:
    for i in range(2, number // 2):
        if number % i == 0:
            prime = False
            print("This number is not prime")
            break
    if prime:
        print("This number is prime")