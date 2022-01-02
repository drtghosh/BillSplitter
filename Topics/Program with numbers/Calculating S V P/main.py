# put your python code here
length = int(input())
width = int(input())
height = int(input())
sum_of_edges = 4 * (length + width + height)
surface_area = 2 * (length * width + length * height + height * width)
volume = length * width * height
print(sum_of_edges)
print(surface_area)
print(volume)