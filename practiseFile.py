#  1. slicing
s =  'Arthur: three!' .lstrip('Arthur: ')
print(s)

s = 'Arthur: three!' .removeprefix('Arthur:')
print(s)
s = 'hellopython' . removesuffix('python')
print(s)
list_of_strings = ['string', 'method', 'in', 'python']
s = '-'.join(list_of_strings)
print(s)
s = 'python is awesome!'.isupper()
print(s)
s = 'python is awesome!'.islower()
print(s)
s = 'python is awesome!'.iscapitalize()
print(s)
