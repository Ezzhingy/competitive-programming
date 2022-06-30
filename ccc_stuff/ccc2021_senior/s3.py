import math

def get_score(p):
    out = 0
    for i in instructions:
        walk = abs(p - i[0]) - i[2]
        if walk > 0:
            out += walk*i[1]
    return out

N = int(input())
instructions = []
for i in range(N):
    instructions.append(list(map(int, input().split())))

low = -1000000000
high = 1000000000
mid = 0
s = 0

while low <= high:
    mid = round((low + high)/2)
    s = get_score(mid)
    s_left = get_score(mid-1)
    s_right = get_score(mid+1)
    if s < s_right and s < s_left:
        break
    elif s == s_right and s == s_left:
        break
    elif s < s_right:
        high = mid - 1
    elif s < s_left:
        low = mid + 1

print(round(s))



