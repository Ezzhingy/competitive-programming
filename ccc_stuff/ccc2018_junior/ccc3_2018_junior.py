def plan(d1_2,d2_3,d3_4,d4_5):
    z = 0
    print(f'{z} {d1_2} {d1_2+d2_3} {d1_2+d2_3+d3_4} {d1_2+d2_3+d3_4+d4_5}')
    print(f'{d1_2} {z} {d2_3} {d2_3+d3_4} {d2_3+d3_4+d4_5}')
    print(f'{d1_2+d2_3} {d2_3} {z} {d3_4} {d3_4+d4_5}')
    print(f'{d1_2+d2_3+d3_4} {d2_3+d3_4} {d3_4} {z} {d4_5}')
    print(f'{d1_2+d2_3+d3_4+d4_5} {d2_3+d3_4+d4_5} {d3_4+d4_5} {d4_5} {z}')



somelst = []
limit = 0

d_cities = input()
for i in range(0,len(d_cities)):
    if d_cities[i] == " ":
        somelst.append(d_cities[limit:i])
        limit = i+1
somelst.append(d_cities[limit:])
        
d_one_two = int(somelst[0])
d_two_three = int(somelst[1])
d_three_four = int(somelst[2])
d_four_five = int(somelst[3])

plan(d_one_two,d_two_three,d_three_four,d_four_five)
