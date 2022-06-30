N = int(input())
height = list(map(int, input().split()))
width = list(map(int, input().split()))
area = 0
for j in range(N):
    area += width[j] * (height[j] + height[j+1])/2.0

print(area)

    