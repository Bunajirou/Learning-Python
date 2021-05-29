import sympy

print('--------------------------------------------------')
print('# [[a,b],[c,d]]*[x,y]≡[e,f] mod(?)となる[x,y]を求める')
print('--------------------------------------------------')

a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
d = int(input('d:'))
e = int(input('e:'))
f = int(input('f:'))
mod = int(input('mod:'))
print()

A = sympy.Matrix([[a,b],[c,d]])
A_det = A.det()
A_inv = A.inv()

A_goudou = A_det % mod
A_inv2 = A_det * A_inv

x,y,t = sympy.gcdex(A_goudou,mod)
A5 = x * A_inv2

a,b,c,d = A5
a %= mod
b %= mod
c %= mod
d %= mod

# A6:求める逆行列
A6 = sympy.Matrix([[a,b],[c,d]])
# a,b,c,d = A6

print('求めるx,yは、')
B1 = sympy.Matrix([e,f])
B2 = A6 * B1
# print(B2)
print('[ x ]')
print('[ y ]')
print('≡')
print('[',a,',',b,']')
print('[',c,',',d,']')
print('*')
print('[',e,']')
print('[',f,']')

a,b = B2
a %= mod
b %= mod
# B3 = sympy.Matrix([a,b])
# print(B3)

print('≡')
print('[',a,']')
print('[',b,'] mod(',mod,')')