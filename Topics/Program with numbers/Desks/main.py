# put your python code here
student_first = abs(int(input()))
student_second = abs(int(input()))
student_third = abs(int(input()))
desks_first = (student_first // 2) + (student_first % 2)
desks_second = (student_second // 2) + (student_second % 2)
desks_third = (student_third // 2) + (student_third % 2)
print(desks_first + desks_second + desks_third)