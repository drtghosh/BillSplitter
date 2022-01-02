angle_1 = int(input())
angle_2 = int(input())
angle_3 = int(input())
summed_angle = angle_1 + angle_2 + angle_3
desired_sum = 180
if summed_angle == desired_sum:
    print("The triangle is valid!")
else:
    print("The triangle is not valid!")