N_X = input()
new_N = ""
new_X = ""
lst = ""
for i in range(0,len(N_X)):
    if N_X[i] == " ":
        new_N += N_X[:i+1]
        break
for i in range(len(N_X)-1,0,-1):
    if N_X[i] == " ":
        new_X += N_X[i+1:]
        break
for i in range(0,int(new_N)):
    A_V = input()
    lst += A_V + " "

def machine(N,X,strr):
    count = []
    seperate = strr.split()
    for i in range(0,len(seperate),2):
        if int(seperate[i]) > X:
            sums = X * int(seperate[i+1])
            count.append(sums)
        else:
            sums = int(seperate[i]) * int(seperate[i+1])
            count.append(sums)
    return count

result = machine(int(new_N),int(new_X),lst)

print(max(result))
            
                






