X = int(input())
together = []
for i in range(X):
    together.append(input().split())
# print(together)

Y = int(input())
seperate = []
for i in range(Y):
    seperate.append(input().split())

G = int(input())
result = []
for i in range(G):
    result.append(input().split())
# print(result)

contraints = 0

for j in together:
    for i in result:
        # print(i, j)
        if j[0] in i and not j[1] in i:
            contraints += 1
            # print("not in same group")
            break
            
        elif j[1] in i and not j[0] in i:
            contraints += 1
            # print("not in same group")
            break 

for k in seperate:
    for i in result:
        # print(i,k)
        if k[0] in i and k[1] in i:
            # print("in same group")
            contraints += 1
            break
        elif k[1] in i and not k[0] in i:
            break
        elif k[0] in i and not k[1] in i:
            break
        # if k[0] in i and not k[1] in i:
        #     seperate.remove(k)
        #     break
        # elif not k[0] in i and k[1] in i:
        #     seperate.remove(k)
print(contraints)

