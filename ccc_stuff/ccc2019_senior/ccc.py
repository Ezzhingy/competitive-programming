def machine(xs):
    num = [[1,2],[3,4]]
    for i in xs:
        if i == "H":
            num[0][0], num[1][0] = num[1][0], num[0][0]
            num[0][1], num[1][1] = num[1][1], num[0][1]
        elif i == "V":
            num[0][0], num[0][1] = num[0][1], num[0][0]
            num[1][0], num[1][1] = num[1][1], num[1][0]
            
    print(f'{num[0][0]} {num[0][1]}\n{num[1][0]} {num[1][1]}')






x = input()
(machine(x))
