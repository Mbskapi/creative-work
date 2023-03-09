def match_func():
    print("###################### match #####################")

    num = int(input("Enter a number: "))

    match num:
        case  _ as x if 1 < x < 10:

           print(x)

        case 30 | 40 | 50:

           print(2)

        case _ as x if 11 < x < 20:

            print("don't know you")


match_func()

lst = [20, 13, 16, "good"]

match lst:
     case[i1, i2, i3]:
         print(i1, i2, i3)
#     case _:

##        print("nothing matched")


d = {
    "name": "hadiza",
    "age": "18",
    "is_swit": True
}

match d:
    case {"name": str(name), "age": int(age)}:
        print(name, age)



def fizzbuzz(num):
    three = num % 3
    five = num % 5
    match (three, five):
        case (0, 0):
            return  "fizzbuzz"
        case (0, _):
            return "fizz"
        case(_, 0):
            return  "buzz"
        case _:
            return num
for i in range(1, 101):
    print(fizzbuzz(i))

    def summing_list(list_:list[int]) -> int:
        match list_:
            case []:
                return 0
            case [first_value, *another_list]:
                return first_value + summing_list(another_list)
            case _:
                print("can only accept an int")
                return None

    print(summing_list([1, 2, 3, 4, 5]))


import itertools
print(summing_list([1, 2, 3, 4, 5,]))
print(list(itertools.zip_longest([1, 2], [3, 4, 5], fillvalue=0)))


