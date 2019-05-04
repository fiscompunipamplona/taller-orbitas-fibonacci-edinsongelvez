
import math as mt
r=float(input("digite el valor del radio"))
angulo=float(input("digite el valor del angulo"))
x=r*mt.cos(angulo/180*mt.pi)
y=r*mt.sin(angulo/180*mt.pi)
print("el resultado de x es ",x)
print("el resultado de y es ",y)

#Orbitas planetarias. A partir de la segunda ley de Kepler escriba un programa
#que calcule la posiciòn y velocidad en el afelio dada la posiciòn y velocidad 
#en al perihelio

G=6.67e-11
M=1.989e30
pi=3.1416

rp=float(input("digite el radio del perihelio"))
vp=float(input("digite la velocidad del perihelio"))

va=(((2*G*M)/(vp*rp))+(((2*G*M)/(vp*rp))**2+4*((vp**2-2*G*M)/rp))**1/2)/2
ra=(rp*vp)/va
a=(rp+ra)/2
b=(rp*ra)**(1/2)
T=(2*pi*a*b)/(rp*vp)
e=(ra-rp)/(ra+rp)

print("la velocidad del afelio es:" ,va)
print("el radio del afelio:" ,ra)
print("el semieje mayor es:" ,a)
print("el semieje menor es:" ,b)
print("el periodo orbital es:", T)
print("la excentricidad orbital es:" ,e)

#Escriba un còdigo que calcule la secuencia de Fibonacci

q=1
d=1

print(q)
while d <= 1000: 
    
    print(d)
    n=q+d
    q=d
    d=n
    

