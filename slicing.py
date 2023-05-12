# is to do just thing and one thing alonge
# def my_function(child1, child2, child3, child4, child5, child6):
#     print("the youngest child" + child4, child1)
#
# #  my_function(child1="james", child2="johnson",child3="peace",
# #                 child4="mark",child5="victor",child6="lucky")
# my_list = ["banana", "mango", "grape", "pawpaw", "pinapple", "water_melon", "orange", "cumcumber"]
# index = my_list.index("pawpaw")
# print(my_list, index)


# calculating food percentage
# food_amount = float(input('Enter food amount $:'))
# tip_percentage = float(input('Enter your tip_percentage:'))/100
# tip_amount = food_amount * tip_percentage
# total_amount = food_amount + tip_percentage
# print(f'food amount: ${food_amount}')
# print('$' + str(total_amount))


# boolean
# if withdraw amount > balance, withdraw
#
#
# weather = input('how is the weather? ')
#
# if weather == 'rain':
#  print('it is raining')
#
# elif weather == 'cloud':
#     print(weather)
#
# elif weather == 'bright':
#     print("clear skies")
# else:
#        print("glass")
#  #comparison operator
# import grade as grade
# #
# import grade
#
# passing_student = input("what is your grade?")
# score = 90
# if grade >= 90 and grade <= 100:
#     print(" A")
# elif grade >= 80 and grade <= 90:
#     print('B')
# elif grade >= 70  and grade <=80:
#     print('C')
# elif grade >= 60 and grade <=70:
#     print('D')
# else:
#     print('f')
#
#     a = 5
#     b = 10
#     total = 5*10
#     print(total)
#     # if a > b:
    #     print("a is less than 10")
    #     return a
    # else:
    #     print("true")
    #     return b
#
#
#
# def sum(a, b):
#     return a + b
# sum2 = lambda a, b: a+b
# print(sum2(5, 10))
# greet = lambda greet, name: f"{greet} {name}"
# print(greet('aloha', 'kapi'))
#
#
# def calculatefoodamount():
#     food_amount = 200
#     tip_percentage = 20 * 100
#     total_sum = food_amount + tip_percentage
#     print(total_sum)


#comparing integer using if statement and comparison operator
#
# print('enter two integer, and i will tell you the relationship')
# number1 = int( input('enter first integer'))
# number2 = int(input('enter second integer'))
#
# if number1 == number2:
#     print(number1,'is not equal',number2)
#
# if number1 != number2:
#     print(number1, 'not equal', number2)
#
# if number1 > number2:
#     print(number1,'greater than', number2)
#
# if number1 < number2:
#     print(number1,'is less than', number2)
#
# if number1 >= number2:
#     print(number1,'greater or equal', number2)
#
# if number1 <= number2:
#     print(number1,'less or equal', number2)

#the numeber that reteurn sum of strings.


#let learn about lists
supplies =["tents", "sleeping bags", "water",
           "raspberry pi", "coffee", "knife",
           "ethernet cable", "flash drive", "beard oil"]


camp_site =["crystal lake", 404, 95, 5, 10, ]

#supplies.extend("toilet paper,   bidet")
supplies.insert(0,"toilet paper")
supplies.insert(1, "bidet")
supplies.insert(-1, "fish_bread")

print(supplies)
