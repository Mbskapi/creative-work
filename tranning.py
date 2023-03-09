def counter(iterable: list | str | tuple) -> dict:
    item_dict = {}
    #for item in iterable:
     #   if item in item_dict:

    #        item_dict[item] = item_dict[item] + 1
   #     else:

  #          item_dict[item] = 1
        # item_dict[item] = item_dict.get[item, 0] + 1
 #   return item_dict


# print(word_letters("hello"))

#def square_list_comprehension():
#    cont = [num ** 2 for num in range(1, 11)]
 #   return cont


#print(square_list_comprehension())
range (1, 11)
for i in range(1, 11):
 cont = [num for num in range(1, 11)]
print(cont)
names =['bimpe:', 'banke', 'abimbola:' ,'james:','olalekan:', 'Recheal']
my_names = []
for name in names:
    if name.istitle():
        my_names.append(name)
print(names)

name =['bimpe', 'kelechi', 'james', 'olalekan', 'banke', 'Racheal']
my_names = [name for name in name if names.istitle()]
upper_name =[input(f"{i + 1} name")]
even = [even for even in range(1, 11)if even %2 == 0]
print()
# int z
#users = [
   # {'name': 'hadiza',
    # 'age': 21,
     #'gender': 'female',
    # 'username': 'daezah',
     #'is_verified': 'true',
     #'tweets': [
        # {'content': 'po for president', ' likes': '450', 'retweets': 233}
        # {'content': 'atiku is our man', 'likes': 4, 'retweets': 2}

