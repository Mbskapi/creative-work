#new list = [expression for number in iterable]

list1 = []
for i in range(5):
    list1.append(i*i)
    #print(list1)

    list2 = [i*i for i in range(5)]
    #print(list2)

    def cube(i):
        return i*i*i
    cubes = [cube(i) for i in range(5)]
    #print(cubes)
    #if the conditional statement
    evens = [i for i in range(20)if i %2==0]
    #print(evens)

    a = [1,2,3,4,5,6,7,8]
    b = [0 if i < 4 else i for i in a]
    #print(b)

    #list with of dict/ set

    quote = "hello everybody"
    unique_vowels = { i for i in quote if i}
   # print(quote)

    square = {i: i*i for i in range(5)}
   # print(square)

    matrix2d = [[i*j for i in range(5) for j in range(5)]]
    print(matrix2d)


    s = sum[(i*i for i in range (1000))]
    print(5)

    #from timeit import default_timer as timer
    a = []
    for i in range(1_000_000):
        end = ()
        a.append(i*i)
        print()

