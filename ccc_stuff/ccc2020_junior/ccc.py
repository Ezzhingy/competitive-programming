###2020 junior ccc
###1.
def hapsad(small, medium, large):
    total = 1 * small + 2 * medium + 3 * large
    if total >= 10:
        return "happy"
    else:
        return "sad"




s = int(input())
m = int(input())
l = int(input())

print(hapsad(s,m,l))


