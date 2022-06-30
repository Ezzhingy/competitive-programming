first = int(input())
second = int(input())
third = int(input())

check_one = first + second
check_two = check_one + second
check_three = check_two + second
if third <= check_one:
    print(check_one)
elif third <= check_two:
    print(check_two)
elif third <= check_three:
    print(check_three)
else:
    print("Who knows...")
    
