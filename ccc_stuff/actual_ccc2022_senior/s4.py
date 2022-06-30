CN = input().split()
N = CN[0]
C = CN[1]
point_list = input().split()
num_dict = {}
for num in point_list:
    if num not in num_dict:
        num_dict[num] = 1
    else:
        num_dict[num] += 1
sorted(num_dict)
for i in range(len(num_dict)):
    if i + 1 < len(num_dict):
        key = list(num_dict.keys())
        next_key = key[i+1]
        next_key2 = key[i+2]
    if next_key-key == C/2:
       break
    elif next_key2 - key == C/2:
        break
    elif next_key2 - next_key ==C/2:
        break
    elif next_key2 - next_key == 4 and max(next_key2,next_key,key) <= 5:
        break
    elif 



