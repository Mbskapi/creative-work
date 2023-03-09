lst = [1, 2, 3, 4, 5]

it = iter(lst)
print(next(it))
print(list(it))
print(next(it))

def custom_for(iterable, func):
    it = iter(iterable)

    while True:
        try:
            func(next(it))
        except StopIteration:
            print(("End of loop"))
            return

custom_for(lst, print)




#create another file
def custom_range(num):
    pass


def infinite_number_generator():
    num = 0
    while True:
        yield num
        num =+1

gen = infinite_number_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
for i in gen:
    print(i)