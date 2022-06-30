N = int(input())
observations = []
max_X = []
for i in range(N):
    observations.append(list(map(int, input().split())))
observations.sort()
for i in range(len(observations)):
    if i + 1 < len(observations):
        X = abs((observations[i+1][1] - observations[i][1])/(observations[i+1][0]-observations[i][0]))
        max_X.append(X)
print(max(max_X))