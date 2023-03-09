# figure02_01.py
""""comparing teo integer using if statement and using comparison operator"""

print("Enter two integer and i will tell you,"
       "the relationship they satisfy")

#read first integer number

number1 = int(input("Enter the first integer"))

    #read second integer number
number2 = int(input("Enter the second integer"))

if number1 == number2:
         print(number1, 'to equal to', number2)

if number1 != number2:
       print(number1,'is not equal to', number2)

if number1 < number2:
        print(number1,'is less than',number2)
if number1 > number2:
    print(number1,'great than',number2)

    if number1 <= number2:
      print(number1,'great than equal to',number2)

    if number1 >= number2:
     print(number1,'is great than equal less than equal',number2)


