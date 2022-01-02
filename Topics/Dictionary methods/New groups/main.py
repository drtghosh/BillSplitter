# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
filled_groups = int(input())
filled_dict = dict.fromkeys(groups, None)
for i in range(filled_groups):
    group_kids = int(input())
    filled_dict[groups[i]] = group_kids
print(filled_dict)