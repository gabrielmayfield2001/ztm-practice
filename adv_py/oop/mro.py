# class A:
#     num = 10

# class B(A):
#     pass

# class C(A):
#     num = 1

# class D(B, C):
#     pass

# print(D.num)


# print(D.mro())
# D.__str__


class X:pass
class Y: pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass