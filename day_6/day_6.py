from collections import defaultdict

points = []
with open('input.txt') as f:
    for line in f:
        x, y = [int(s.strip()) for s in line.split(',')]
        points.append((x, y))
        print(x, y)

print(len(points))

x_left = min([p[0] for p in points])
x_right = max([p[0] for p in points])
y_top = min([p[1] for p in points])
y_bottom = max([p[1] for p in points])

print((x_left, x_right))
print((y_top, y_bottom))

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def closest(x, y):
    distances = [(manhattan_distance(x, y, *p), p) for p in points]
    distances.sort(key=lambda x: x[0])
    if distances[0][0] < distances[1][0]:
        return distances[0][1]
    else:
        return (-1, -1)
# print('part 1')
# scores = defaultdict(int)
# for x in range(x_left, x_right):
#     for y in range(y_top, y_bottom):
#         scores[closest(x, y)] += 1
#
#
# # create a bounding box 100 units away from points and calculate closest points to get points for which areas are
# # infinite. remove them from results and get max area
# scores_inf = defaultdict(int)
# for x in range(x_left - 100, x_right + 100):
#     for y in (y_top - 100, y_bottom+100):
#         scores_inf[closest(x, y)] += 1
#
# for x in (x_left - 100, x_right + 100):
#     for y in range(y_top - 100, y_bottom+100):
#         scores_inf[closest(x, y)] += 1
#
# inner_scores = {k: v for k, v in scores.items() if k not in scores_inf}
#
# print(max(inner_scores.values()))

print('Part 2:')

safe_points = []
for x in range(x_left - 100, x_right + 100):
    for y in range(y_top - 100, y_bottom+100):
        cum_dist = 0
        for p in points:
            cum_dist += manhattan_distance(x, y, *p)

            if cum_dist >10000:
                break

        if cum_dist < 10000:
            safe_points.append((x, y))

print(len(safe_points))

