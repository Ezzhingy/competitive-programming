def even_rule(sets, t):
    one = int(sets[0])
    two = int(sets[1])

    if (one + two) % 2 == 0:
        t = 0
        return t
    else:
        t = 1
        return t    

def even_odd(sets, t):
    one = int(sets[0])
    two = int(sets[1])
    rest = sets[2:]
    if (one + two) % 2 == 0 and one+two != 0:
        print(f'right {rest}')
    elif one + two == 0 and t == 0:
        print(f'right {rest}')
    elif one + two == 0 and t == 1:
        print(f'left {rest}')
    else:
        print(f'left {rest}')

    
    



num = []
test = 0
x = input()
num.append(x)
while x != "99999":
    x = input()
    num.append(x)
num.remove(num[-1])


for i in num:
    even_odd(i, test)
    test = even_rule(i, test)
    
        
    
