integer1 = input("enter the first integer: \n")
print("integer1: "),id(integer1), type(integer1)
integer1 = int(integer1)
print ("integer1: "), id(integer1), type(integer1)

integer2 = input("enter the second integer: \n")
print("integer2: "), id(integer2), type(integer2)
integer2 = int(integer2)
print("integer2:") ,id(integer2),type(integer2)

sum = integer1 + integer2
print("sum is"), id(sum), type(sum), sum