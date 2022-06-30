import math

N = int(input())
hood = []
for i in range(N):
    V = int(input())
    hood.append(V)
hood.sort()

distance = []
for i in range(len(hood)):
    if hood[i] == min(hood):
        distance.append(math.inf)
    elif hood[i] == max(hood):
        distance.append(math.inf)
    else:
        left_distance = (hood[i] - hood[i-1]) / 2
        right_distance = (hood[i+1] - hood[i]) / 2
        distance.append(round(left_distance+right_distance, 1))
print(min(distance))
