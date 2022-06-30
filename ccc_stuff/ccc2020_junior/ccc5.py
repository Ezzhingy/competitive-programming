import random

def factors(x):
    factors_lst = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors_lst.append(i)
    return factors_lst

def loop(start,coords,n_lst):
    fac_start = factors(start)
##        print("hope this changes",fac_start)
    x = random.choice(fac_start)
    y = random.choice(fac_start)
    c = (x,y)
    while (x > num_row or y > num_column) or (x*y != start) or (c not in coords):
        x = random.choice(fac_start)
        y = random.choice(fac_start)
        c = (x,y)
   
    index = coords.index(c)
    start = num_list[index]
    return start
    
            
def escape(num_list,num_row,num_column,somelst):
    rip = 0
    end = num_list[-1]
    start_coords = (1,1)
    end_coords = num_row,num_column
    optimal_num = num_row*num_column
    coords = []
    for i in range(1,len(somelst)+1):
        for k in range(1,num_column+1):
            coor = (i,k)
            coords.append(coor)
        
    start = num_list[0]
    fac_start = factors(start)
    x = random.choice(fac_start)
    y = random.choice(fac_start)

    while (x > num_row or y > num_column) or x*y != start:
        x = random.choice(fac_start)
        y = random.choice(fac_start)

    c = (x,y)
    

##    while start != optimal_num:
##    the start here doesn't change - so it's always 3
    if start == start:
        
        start = loop(start,coords,num_list)
        if start == optimal_num:
            print("yes")
        else:
            start = loop(start,coords,num_list)
            if start == optimal_num:
                print("yes")
            else:
                start = loop(start,coords,num_list)
                if start == optimal_num:
                    print("yes")
                else:
                    print("no")
                            

        


##        print(index,start)

##        else:
##            rip +=1
##
##        if rip % 20 == 0:
##            start = num_list[0]
##        
##        if rip > 100:
##            print("no")
##            
##        print("still searching",start)
##        
##        
##        
##    print("yes")

        

    
    



        

        

    

somelst = []
num_list = []
limit = 0

num_row = int(input())
num_column = int(input())

for i in range(0,num_row):
    inputs = input()
    somelst.append(inputs)

for j in somelst:
    for k in range(0,len(j)):
        if j[k] == " ":
##            print("found space", j[k])
            num_list.append(int(j[limit:k]))
            limit = k + 1
        elif k == len(j)-1:
##            print("end of line", j[k])
            num_list.append(int(j[limit:]))
            limit = 0
##print(num_list)
escape(num_list,num_row,num_column,somelst)
