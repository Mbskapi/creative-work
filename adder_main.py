# list
#def my_fun(param):
 #   param = [1, 2, 3]
  #  param.append(4)
   # return param


#my_list = [1, 2, 3]
#new_list = my_fun(my_list)
#print(my_list, new_list)


def func(*args):
    total = 0
    for arg in args:
        total += arg
        print(total)
func(1, 2, 3, 4, 5, 6)

def func1(**kwargs):
    print(kwargs)

#func(a=1, b=2, c=3, d=4, e=5, f=6)

#print(module.a)
#print(f"name: {_name_}")
#print(module1.add(4,7))
#print(f"from module2 name: {_name_}")
