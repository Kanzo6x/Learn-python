# Example 1 multiple inhertance 
class A:
   a = 1
   
class B:
   b = 2
   
class C(A, B):
   pass

c = C()
print(c.a, c.b)
#=================================================================================
# EXample 2 Multi level inheritance 
class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a)

print(issubclass(A,B)) # issubclass a function that retruns true or false depends if there a relation between the classes
print(issubclass(B,A))

print(isinstance(c,C))# isinstance a function that returns true or false depends if there a relation between the obj and the class 
print(isinstance(c,C))

#=================================================================================
#Example 3 Super() 
class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()
