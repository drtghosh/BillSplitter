initial = int(input())
final = int(input())
half_life = 12
period = 0
while initial > final:
    period += 1
    initial /= 2

print(period * half_life)