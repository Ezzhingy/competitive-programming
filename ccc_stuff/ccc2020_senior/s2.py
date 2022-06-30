         
import sys

def already_in_list(lst, size, number):
    for i in range(size):
        if lst[i] == number:
            return True
    return False

table = []
M = int(input())
N = int(input())
for i in range(M):
    row = list(map(int, input().split()))
    table.append(row)

size = M * N

pathways = []

for i in range(size):
    pathways.append(-1)

empty_spot = 0
current_exploration = 0

pathways[empty_spot] = table[0][0]
empty_spot += 1

if pathways[current_exploration] == size:
    print("yes")
    sys.exit()

while pathways[current_exploration] != -1:
    for i in range(1,M+1):
        for j in range(1,N+1):
            if i*j == pathways[current_exploration]:
                if table[i-1][j-1] == size:
                    print("yes")
                    sys.exit()

                if already_in_list(pathways, size, table[i-1][j-1]) == False:
                    pathways[empty_spot] = table[i-1][j-1]
                    empty_spot += 1
    current_exploration += 1

print("no")


        