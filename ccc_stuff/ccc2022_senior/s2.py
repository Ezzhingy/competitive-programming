N = int(input())
swifts = list(map(int, input().split()))
semas = list(map(int, input().split()))

days = []
for i in range(N+1):
    if i == 0:
        score_swifts = i 
        score_semas = i
    else:
        score_swifts += swifts[i-1]
        score_semas += semas[i-1]
    
    if score_swifts == score_semas:
        days.append(i)
print(max(days))