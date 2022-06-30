M = int(input())
N = int(input())
K = int(input())
choices = []
grid = ["B"]*(M*N)
for i in range(K):
    choice = list(input().split())
    choices.append(choice)
# for x in range(M):
#     for y in range(N):
#         grid.append("B")

count = 0
for option in choices:
    if option == choices[0]:
        if option[0] == "R":
            row_num = int(option[1])
            if grid[row_num*N-N] == "B":
                grid[grid_num:row_num*N-N+N] = "G"*N
                count += 1
        
        else:
            column_num = int(option[1])
            if grid[column_num-1] == "B":
                grid[grid_num:M*N,N] = "G"*M
                count += 1

    if option[0] == "R":
        row_num = int(option[1])
        for grid_num in range(row_num*N-N,row_num*N-N+N):
            if grid[grid_num] == "B":
                grid[grid_num] = "G"
                count += 1
            else:
                grid[grid_num] = "B"
                count -= 1
    
    else:
        column_num = int(option[1])
        for grid_num in range(column_num-1,M*N,N):
            if grid[grid_num] == "B":
                grid[grid_num] = "G"
                count += 1
            else:
                grid[grid_num] = "B"
                count -= 1

print(count)