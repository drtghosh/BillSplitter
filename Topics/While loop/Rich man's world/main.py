deposit = int(input())
year = 0
protected = 700000
interest_multiplier = 1.071
while deposit <= protected:
    year += 1
    deposit *= interest_multiplier

print(year)