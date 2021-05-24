print('ax + by = p\n'
      'cx + dy = q (mod N)\n')

a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
d = int(input('d='))
p = int(input('p='))
q = int(input('q='))
n = int(input('N='))

print('')
print('{0}x + {1}y = {2}\n'
      '{3}x + {4}y = {5} (mod {6})\n'.format(a,b,p,c,d,q,n))

det = a*d - b*c  #　　det = 行列式
det = det % n

ans = 0  #  ループを回すためにとりあえずの代入
x = 0

while(ans != 1):
    x += 1
    ans = (det * x) % n

indet = x  #  indet = 行列式の逆数

tmp = a
a = (d * indet) % n
b = (-b * indet) % n
c = (-c * indet) % n
d = (tmp * indet) % n

x = (a * p + b * q) % n
y = (c * p + d * q) % n

print('(x,y) = ({0},{1}) (mod {2})'.format(x,y,n))