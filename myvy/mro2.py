'''#Example 1 
class A:
    def b(self):
        return "Function inside A"
class B:
    pass

class C: 
    def b(self):
        return "Fucntion inside C" 
class D(B,C,A) :
    pass
class D(C):
    pass
d = D=(C)
print(d.b())
'''
#Example 2
'''
class A:
    def c(self):
        return "Function inside A"

class B(A):
    def c(self):
        return "Funcrion inside B"

class C(A,B):
    pass

class D(C):
    pass

d=D()
print(d.a)
'''
#Example 3

class A:
    pass

class B(A):
    pass

class C(B):
    pass


c = C()
print(c.a())