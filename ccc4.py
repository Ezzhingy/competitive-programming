L_lst = []
M_lst = []
char = input()

for k in char:
    if k == "L":
        L_lst.append(k)
    elif k == "M":
        M_lst.append(k)

limit_L = len(L_lst)
limit_M = len(M_lst)

swap = 0

for m in range(0,len(char)):
    if char[m] == "S" and m < limit_L:
        swap +=1
        
    elif char[m] == "S" and m > limit_L and m < limit_L + limit_M:
        swap +=1

    elif char[m] == "M" and m < limit_L:
        swap +=1
        
##    elif "M" == char[-1]:
##        swap +=1
if "M" == char[-1]:
    swap +=1


print(swap)

