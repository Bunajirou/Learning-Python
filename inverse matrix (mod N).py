print('(a,b)\n'
      '(c,d) (mod N)\n')

a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
d = int(input('d='))
n = int(input('N='))

print('\n')
print('({0},{1})\n'
      '({2},{3}) (mod {4})\n'.format(a,b,c,d,n))

det = a*d - b*c  #　　det = 行列式
det = det % n

print('|A| = {0} (mod {1})\n'.format(det,n))

ans = 0  #  ループを回すためにとりあえずの代入
x = 0

while(ans != 1):
    x += 1
    ans = (det * x) % n

indet = x  #  indet = 行列式の逆数

ans_a = (d * indet) % n
ans_b = (-b * indet) % n
ans_c = (-c * indet) % n
ans_d = (a * indet) % n

print('({0},{1})\n'
      '({2},{3}) (mod {4})\n'.format(ans_a,ans_b,ans_c,ans_d,n))