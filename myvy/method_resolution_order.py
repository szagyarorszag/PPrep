'''# Example 1
class A:
   def a(self):
       return "Function inside A"

class B:
    def a(self):
        return "Function inside B"

class C(B,A):
    pass

# Driver code
c = C()
print(c.a())
#Output Function inside B
'''
'''
#Example 2
class A:
    def b(self):
        return "Function inside A"

class B:
    def b(self):
        return "Function inside B"

class C(A, B):
    #def b(self):
    #    return "Function inside C"
    pass

class D(C):
    pass

d = D()
print(d.b())

#Output : Fucntion inside C
'''
'''
class A:
    def c(self):
        return "Function inside A"

class B:
    def c(self):
        return "Function inside B"

class C(A, B):
    def c(self):
        return "Function inside C"

class D(A, C):
    pass

d = D()
print(d.a)
'''
'''Output :Traceback (most recent call last):
  File "/Users/intropython/PycharmProjects/practicePython/inherit.py", line 10, in <module>
    class D(A, C):
TypeError: Cannot create a consistent method resolution
order (MRO) for bases A, C'''



#Example 4
class A:
    def d(self):
        return "Function inside A"

class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    def d(self):
        return "Function inside D"


class E(B, C):
    def d(self):
        return "Function inside E"


class F(E,D,C):
    pass

f = F()
print(f.d())
print(F.mro())
'''output : Function inside E
[<class '__main__.F'>, <class '__main__.E'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]'''