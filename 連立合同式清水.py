print("( a b )(x) = (A1) (mod n )")
print("( c d )(y) - (A2)")

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=int(input("d="))
A1=int(input("A1="))
A2=int(input("A2="))
n=int(input("mod n="))

Mat=(a*d)-(b*c)

for i in range(1, n):
    X=(Mat*i)%n
    if X == 1:
        break

tmp=a
a=d
d=tmp
b=b*-1
c=c*-1

a=(a*i)%n
b=(b*i)%n
c=(c*i)%n
d=(d*i)%n

x=(a*A1+b*A2)%n
y=(c*A1+d*A2)%n

print("x=",x)
print("y=",y)
