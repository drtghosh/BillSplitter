# put your python code here
import math

side_1 = int(input())
side_2 = int(input())
side_3 = int(input())
half_p = (side_1 + side_2 + side_3) / 2

area_sq = half_p * (half_p - side_1) * (half_p - side_2) * (half_p - side_3)
area = math.sqrt(area_sq)
print(area)