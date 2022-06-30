code = []
num = []
char = []
count = int(input())
for i in range(0,count):
    x = input()
    code.append(x)
    
for thing in code:
    num.append(int(thing[0:2]))
    char.append(thing[-1])
    
for i in range(0,len(num)):
    print(char[i]*num[i])


    
