first = int(input ('Number'))
second = int(input ('Number'))
third = int(input ('Number'))


if first == second == third:
    print(3)
elif first == second or second == third or third == first :
    print (2)
else:
    print (0)
