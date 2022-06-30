row = int(input())
col = int(input())
k = int(input())
choices = []

for i in range(0,k):
    orders = input()
    choices.append(orders)
remember = []
restart = []
gold = 0
black = row*col
for k in choices:
    if "R" in k and "R" in restart:
        gold, black = black, gold
        restart.remove("R")
##        print(black,gold, "switch")
    elif "R" in k:
        black, gold = gold, black
        restart.append("R")
##        print(black,gold, "switch2")
        
    if "C" in k:
        index = k[-3:]
        if "R" in restart:
            if index in remember:
                gold +=1
                black -=1
                remember.remove(index)
##                print(black,gold,"goldshouldgoup")
            
            else:
                black += 1
                gold -=1
                remember.append(k[-3:])
##                print(black,gold,"blackshouldgoup")
        else:
            if index in remember:
                black +=1
                gold -=1
                remember.remove(index)
##                print(black,gold,"blackshouldgoup")
            else:
                gold +=1
                black -=1
                remember.append(k[-3:])
##                print(black,gold,"goldshouldgoup")
print(gold)
        
    
    

    
