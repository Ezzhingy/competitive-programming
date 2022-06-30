import sys

def rotate(grid_value):
    way = []
    way_lst = []
    for i in range(len(grid_value)):
        for j in range(-1,-len(grid_value)-1,-1):
            way_lst.append(grid_value[j][i])
        way.append(way_lst)
        way_lst = []
    return way

def checker(grid_value):
    count = 0
    for i in range(len(grid_value)):
        for j in range(len(grid_value)):
            if grid_value[i][j] < count:
                return False
            count = grid_value[i][j]
            if i + 1 < len(grid_value) and j + 1 < len(grid_value):
                if grid_value[i][j] > grid_value[i+1][j]:
                    return False
        count = 0
    return True


N = int(input())
grid = []
for i in range(N):
    grid.append(list(map(int, input().split())))

# way1
way1 = grid
if checker(way1) == True:
    for i in range(len(way1)):
        for j in range(len(way1)):
            print(way1[i][j], end=" ")
        print("")
    sys.exit()

# way2
way2 = rotate(grid)
if checker(way2) == True:
    for i in range(len(way2)):
        for j in range(len(way2)):
            print(way2[i][j], end=" ")
        print("")  
    sys.exit() 

# way3
way3 = rotate(way2)
if checker(way3) == True:
    for i in range(len(way3)):
        for j in range(len(way3)):
            print(way3[i][j], end=" ")
        print("")
    sys.exit()

# way4
way4 = rotate(way3)
if checker(way4) == True:
    for i in range(len(way4)):
        for j in range(len(way4)):
            print(way4[i][j], end=" ")
        print("")
    sys.exit()




    