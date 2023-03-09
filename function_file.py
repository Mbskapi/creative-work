# with open('temp_file_txt', mode='w', encoding='utf-8') as file_object:
#  print(file_object.tell())
# file_object.write("life is good with banke")
# file_object.seek(10)
# print(file_object.tell())
# file_object.write("life is good with banke"

class Human:
    legs = 2
    count = 1

    def __init__(self, name="", age=0):
        self._name = name
        self._age = age
        Human.count += 1

        @classmethod
        def get_count(cls):
            return cls._count

        @staticmethod
        def is_minor(age):
            return age < 16


            #@staticmethod
            #def do_nothing():
            #reture "nothing"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name.islower():
            raise ValueError("Name cannot be all lower case")
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age Cannot be less than 0")
        self._age = age

    @age.deleter
    def age(self):
        print("deleting age......")


human_instance = Human()
human_instance.name = "Kapi Emmanuel"
human_instance.age = 30
print(f"Name is: {human_instance.name} and age is: {human_instance.age} years old")

h2.name = "Rachael"
h2.age = 44
new_name = h1.name
print(h2.is_minor(h2.age))
print(f"this is the second name setter {new_name} and age is {h1.age}")

h3.name ="Lakes"
h3.age = 1
print(f"this is the second name setter{h1.name}and age is {h1.age} ")
print(Human.get_count())
