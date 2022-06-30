import math

N = int(input())
readings = {}

for i in range(N):
    R = int(input())
    if R not in readings:
        readings[R] = 1
    else:
        readings[R] += 1

lst = []
absolute = max(readings, key=readings.get)
while True:
    if 
    max_key = max(readings, key=readings.get)
    readings.pop(max_key)
    lst.append(abs(max_key-absolute))
    if readings == {}:
        break
print(max(lst))

