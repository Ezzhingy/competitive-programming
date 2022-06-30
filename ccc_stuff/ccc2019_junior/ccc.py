three_point_A = int(input())
two_point_A = int(input())
one_point_A = int(input())

three_point_B = int(input())
two_point_B = int(input())
one_point_B = int(input())

total_A = three_point_A*3 + two_point_A*2 + one_point_A*1
total_B = three_point_B*3 + two_point_B*2 + one_point_B*1

if total_A > total_B:
    print("A")
elif total_B > total_A:
    print("B")
else:
    print("T")
