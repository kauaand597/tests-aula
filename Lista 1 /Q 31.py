from math import sqrt

a= int(input('Valor de a: '))
b=int(input('Valor de b: '))
c=int(input('Valor de c: '))

x1= (-b + sqrt(b*2-4*a*c))/(2*a)

x2= (-b - sqrt(b*2-4*a*c))/(2*a)

print(f"As raízes são {x1} e {x2}")