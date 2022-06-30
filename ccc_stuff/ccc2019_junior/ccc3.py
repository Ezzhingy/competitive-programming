def coder(i):
    pass


x = int(input())
lst = []
code = []
finale = []
grandfinale = []
count = 0
final = ""

for i in range(0,x):
    y = input()
    lst.append(y)
    
newlst = f'{lst[0][0]}'

##for i in range(0,len(lst)):
##    strr = lst[i]
##    print(strr)

for i in lst:
    
    for m in i:
  
        if m != newlst:
            final += f'{count} {newlst}'
            print(final)
##            finale.append(final)
            newlst = f'{m}'
            count = 1


        else:
            count += 1
        
    
        
  

            
##print(grandfinale)
##for i in finale:
##    print(i)

