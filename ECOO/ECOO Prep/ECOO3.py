N_C_Q = input()
new_Q = ""
new_N = ""
new_C = ""
lst_of_N = ""
count = 0
spacelst = []
for i in range(0,len(N_C_Q)):
    if N_C_Q[i] == " ":
        new_N += N_C_Q[:i+1]
        break
for i in range(0,len(N_C_Q)):
    if N_C_Q[i] == " ":
        count +=1
        spacelst.append(i)
    if count == 2:
        new_C += N_C_Q[spacelst[0]+1:spacelst[1]]
        break
for i in range(len(N_C_Q)-1,0,-1):
    if N_C_Q[i] == " ":
        new_Q += N_C_Q[i+1:]
        break   
for i in range(0,int(new_Q)):
    N_num = input()
    lst_of_N += N_num + " "

##print(new_N)
##print(new_C)
##print(new_Q)
##print(lst_of_N)

def machine(N,C,Q,strr):
    num = ""
    seperate = strr.split()
    for i in range(1,N+1):
        num += str(i) + " "
    nums = num.split()


    for i in seperate:
        if i % nums:
##    print(nums)
    

machine(int(new_N),int(new_C),int(new_Q),lst_of_N)
        
