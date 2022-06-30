import sys
import math
# 2N = A + B
# N = (A + B)/2

def is_prime(num):
    short_num = math.floor(math.sqrt(num))
    # print(short_num)

    for i in range(2, short_num+1):
        if num % i == 0:
            return False
    return True

N = int(input())
to_be_primed = []
for i in range(N):
    T = int(input())
    to_be_primed.append(T*2)
# print(to_be_primed)

for i in to_be_primed:
    for j in range(2,i):
        first_num = i - j
        second_num = j
        if first_num == 5 and second_num == 3 or first_num == 3 and second_num == 5:
            print(first_num, second_num)
            break
        
        if is_prime(first_num) == True and is_prime(second_num) == True:
            print(first_num, second_num)
            break
