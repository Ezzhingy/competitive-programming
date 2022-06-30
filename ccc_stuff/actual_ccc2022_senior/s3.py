import random

def num_good_samples():
    pass

lst = list(map(int,input().split()))
num_notes = lst[0]
max_pitch = lst[1]
max_good_samples = lst[2]

possible_combos = []
for i in range(num_notes):
    possible_combos.append(random.randint(1,max_pitch))
