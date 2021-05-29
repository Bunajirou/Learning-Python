print('(a b)(x)   (p)\n'
      '(c d)(y) ≡ (q) (mod N)\n')

a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
d = int(input('d='))
p = int(input('p='))
q = int(input('q='))
n = int(input('N='))

print('')
print('({0} {1})(x)   ({2})\n'
      '({3} {4})(y) ≡ ({5}) (mod {6})\n'.format(a,b,p,c,d,q,n))

det = a*d - b*c  #　　det = 行列式
det = det % n
swap_flag = 0
A = det
B = n

R = 1  
i = 0  #  式の番号
Qlist = []

while( R != 0 ):  #  ユークリッドの互除法
    Q = A // B
    R = A % B
    
    print('({0}) {1} = {2} * {3} + {4}'.format(i, A, Q, B, R))
    Qlist.append(Q)
    A = B
    B = R
    i += 1

#  ユークリッドの互除法を遡る
i = i - 2
x1 = Qlist[i]
x2 = x1
x3 = 1

for j in range(i, 0, -1):
    x1 = x1 * Qlist[j-1] + x3
    tmp = x2
    x2 = x1
    x3 = tmp
indet = x3

if( n > det ): i -= i
if( i % 2 == 1 ): indet = -indet

print(indet)

tmp = a
a = (d * indet) % n
b = (-b * indet) % n
c = (-c * indet) % n
d = (tmp * indet) % n

x = (a * p + b * q) % n
y = (c * p + d * q) % n

print('( x, y ) = ({0},{1}) (mod {2})\n'.format(x,y,n))