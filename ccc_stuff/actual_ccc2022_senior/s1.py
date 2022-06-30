N = input()
count = 0
if int(N) % 5 == 0:
    count += 1
    # print("divis by 5")
if int(N) % 4 == 0:
    count += 1
    # print("divis by 4")
# if N % 5 == 0 and N % 4 == 0:
#     count += 1
    # print("divis by both")
# if int(N[-1]) == 0 and int(N) > 20:
#     for i in range(5,int(N)+1,5):
#         # print(i)
#         fours = 4*i
#         fives = int(N) - fours
#         if fives <= 0:
#             break
#         else:
#             count += 1
if int(N[-1]) % 2 != 0:
    temp = int(N)
    while temp > 0:
        temp -= 4
        if temp % 5 == 0:
            count += 1
elif int(N[-1]) % 2 == 0:
    for i in range(2, int(N) + 1, 2):
        fives = 5 * i
        temp = int(N) - fives
        if temp <= 0:
            break
        elif temp % 4 == 0:
            count += 1
        
# else:
#     remainder5  = int(N) % 5
#     remainder4 = int(N) % 4
#     if remainder5 % 4 == 0:
#         count += 1
#     elif remainder4 % 5 == 0:
#         count += 1


# else:
#     remainder5  = N % 5
#     remainder4 = N % 4

#     if remainder5 % 4 == 0:
#         count += 1
#     elif remainder4 % 5 == 0:
#         count += 1
#     else:
#         total = 0
#         while total < N:
#             total += 4
#             if total < N:
#                 total += 5
#             if total == N:
#                 count += 1
#                 # print("more fours than fives")
#                 break
#         total = 0
#         while total < N:
#             total += 5
#             if total < N:
#                 total += 4
#             if total == N:
#                 count += 1
#                 # print("more fives than fours")
#                 break
            
print(count)