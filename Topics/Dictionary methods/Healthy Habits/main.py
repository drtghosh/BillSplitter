# the list "walks" is already defined
# your code here
walk_distances = [walk['distance'] for walk in walks]
print(sum(walk_distances) // len(walk_distances))