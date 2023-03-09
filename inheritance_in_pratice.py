# class pratice:
#     count = 0
#     def __init__(self, first):
#         self.first = first
#
#         def play(self):
#             return f"playing with {self.first}"
#
#         @classmethod
#         def create(cls, name):
#             return cls(name)
#
#         @staticmethod
#         def just_here():
#             return "just hanging out here!!!"
#
#         pi = pratice("Banke")
#         p2 = pratice.create("hadiza")
#         pratice.just_here()
#         pi = just_here()
#

class A:
    def do_this(self):
        print("from A")

class B(A):
     pass

class C(A):
    def do_this(self):
        print("from C")

class D(B, C):
     pass

d = D()
d.do_this()
print(D.mro())
print(D.__mro__)
help(D)




