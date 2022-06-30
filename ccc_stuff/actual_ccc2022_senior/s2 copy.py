X = int(input())
together = []
if X % 2 == 0:
    for i in range(int(X/2)):
        together.append(input().split())
        together.append(input().split())
else:
    for i in range(X):
        together.append(input().split())

Y = int(input())
seperate = []
if Y % 2 == 0:
    for i in range(int(Y/2)):
        seperate.append(input().split())
        seperate.append(input().split())
else:
    for i in range(Y):
        together.append(input().split())

G = int(input())
result = []
if G % 2 == 0:
    for i in range(int(G/2)):
        result.append(input().split())
        result.append(input().split())
else:
    for i in range(G):
        result.append(input().split())


contraints = 0

for i in range(len(result)):
    # X is together
    # Y is seperate
    if abs(i-X) < X:
        temp = abs(i-X)
        # print(i)
        # print(temp)
        
        while True:
            # print(together[temp], result[i])
            if together[temp][0] in result[i] and not together[temp][1] in result[i]:
                contraints += 1
                break
            elif together[temp][1] in result[i] and not together[temp][0] in result[i]:
                contraints += 1
                break
            elif together[temp][0] in result[i] and together[temp][1] in result[i]:
                break
                
            
            if i < len(result)-1:
                i += 1
            else:
                break
            
for i in range(len(result)):
    if abs(i-Y) < Y:
        temp = abs(i-Y)
        # print(i)
        # print(temp)
        
        while True:
            # print(together[temp], result[i])
            if seperate[temp][0] in result[i] and not seperate[temp][1] in result[i]:
                contraints += 1
                break
            elif seperate[temp][1] in result[i] and not seperate[temp][0] in result[i]:
                contraints += 1
                break
            elif seperate[temp][0] in result[i] and seperate[temp][1] in result[i]:
                break
                
            
            if i < len(result)-1:
                i += 1
            else:
                break

 


# for j in together:
#     for i in result:
#         if j[0] in i and not j[1] in i:
#             contraints += 1
#             break
            
#         elif j[1] in i and not j[0] in i:
#             contraints += 1
#             break 

# for k in seperate:
#     for i in result:
#         if k[0] in i and k[1] in i:
#             contraints += 1
#             break

print(contraints)

