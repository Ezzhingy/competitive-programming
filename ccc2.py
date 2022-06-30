namelst = []
bidlst = []
N = int(input())
for i in range(0,N):
    name = input()
    bid = int(input())
    namelst.append(name)
    bidlst.append(bid)

x = max(bidlst)
index = bidlst.index(x)
print(namelst[index])
