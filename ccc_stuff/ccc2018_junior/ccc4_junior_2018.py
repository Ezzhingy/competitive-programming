##def sorting(n_lst,t):
##    success = 0
##    sums = sum(n_lst[0:t])
##    newsums = 0
##    first = []
##    for a in range(t,len(n_lst)-t,t):
##        newsums = sum(n_lst[a:t])
##        if sums < newsums:
##            success +=1
##        elif sums > newsums:
##            for b in range(0,len(n_lst),t):
##                first.append(n_lst[b])
##            for c in range(t,len(n_lst),t):
##            last = n_lst[-t]
##            mid = n_lst[t]
##            n_lst = [last,mid.first,
##            
##            
##
##        if success == t:
##            print(f'{n_lst[0]} {n_lst[1]} {n_lst[2]')
##            print(f'{n_lst[3]} {n_lst[4]}
##
##
##
##
##somelst = []
##num_list = []
##limit = 0
##
##times = int(input())
##for i in range(0,times):
##    inputs = input()
##    somelst.append(inputs)
##
##for j in somelst:
##    for k in range(0,len(j)):
##        if j[k] == " ":
##            num_list.append(j[limit:k])
##            limit = k + 1
##        elif j[k] == j[-1]:
##            num_list.append(j[limit:])
##            limit = 0
##            
##
##
##print(num_list)
##
##sorting(num_lst,times)

trees = int(input())
matrix = []

while True:
    test = []
    for count in range(trees):
        string = raw_input()
        test = [int(s) for s in string.split(" ")]
        matrix.append(test)

    break


def rotate(array):
    ans = []
    for main_count in range(len(array)):
        temp = []
        for zero_count in range(len(array)):
            temp.append(0)

        ans.append(temp)

    for row in range(len(array)):
        col = len(array) - 1
        origin = 0
        while col>=0 and origin<len(array):
            ans[row][origin] = array[col][row]
            origin += 1
            col -= 1

    return ans


def check(matrix):
    outcome = False
    for g in range(len(matrix)):
        if matrix[g] != sorted(matrix[g]):
            outcome = True

    tempo = []
    for l in range(len(matrix)):
        tempo.append(matrix[l][0])

    if tempo != sorted(tempo):
        outcome = True

    if not outcome:
        return False
    elif outcome:
        return True


while True:
    if not check(matrix):
        x = matrix
        break
    else:
        matrix = rotate(matrix)

for i in x:
    string = ""
    for j in i:
        string += str(j) + " "
    print(string)
