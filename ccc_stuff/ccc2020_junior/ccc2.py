###2020 junior ccc
###2.
def disease(p_max, n_infected, r_infects):
    count = 0
    total = n_infected
    replace = n_infected
    while total <= p_max:
        special = replace * r_infects
        replace = special
        total += special
        count += 1
    return count

p = int(input())
n = int(input())
r = int(input())
print(disease(p,n,r))


