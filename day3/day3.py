from math import prod

tobb_path = open('input_day3', 'r').read().splitlines()
tobb_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
results = []
for i in range(len(tobb_slopes)):
    col, trees = 0, 0
    for j in range(0, len(tobb_path), tobb_slopes[i][1]):
        step = tobb_path[j]
        if step[col % len(step)] == '#':
            trees += 1
        col += tobb_slopes[i][0]
    results.append(trees)

print('Number of trees: {}'.format(results))
print('Product of trees: {}'.format(prod(results)))
