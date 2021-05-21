print('ax + by = m\n'
      'cx + dy = n (mod N)\n')

a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
d = int(input('d='))
m = int(input('m='))
n = int(input('n='))
N = int(input('N='))

print('\n')
print('{0}x + {1}y = {2}\n'
      '{3}x + {4}y = {5} (mod {6})\n'.format(a,b,m,c,d,n,N))

det = a*d - b*c  #　　det = 行列式
det = det % N

print('|A| = {0} (mod {1})\n'.format(det,N))

ans = 0  #  ループを回すためにとりあえずの代入
x = 0

while(ans != 1):
    x += 1
    ans = (det * x) % N

indet = x  #  indet = 行列式の逆数

tmp = a
a = (d * indet) % N
b = (-b * indet) % N
c = (-c * indet) % N
d = (tmp * indet) % N
print('({0},{1})\n'
      '({2},{3}) (mod {4})\n'.format(a,b,c,d,N))

x = (a*m + b*n) % N
y = (c*m + d*n) % N
print('x = %d, y = %d' % (x,y))
