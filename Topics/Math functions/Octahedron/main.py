import math

edge_len = int(input())
area = round(2 * math.sqrt(3) * edge_len ** 2, 2)
volume = round(math.sqrt(2) * edge_len ** 3 / 3, 2)
print(area, volume)