from sympy import * 
from sympy.abc import x , y


print('|--------------------------------------------------------------------------------|')
print('| Punto 8. Podemos encontrar puntos criticos los evaluamos y nos dice si es P.e  |')
print('|--------------------------------------------------------------------------------|')
print('')

f = input('digite la funcion con respecto a "X" que deseas derivar: ')
derivada1=diff(f,x)#El primer argumento 'Y1' es la función a derivar y el segundo argumento 'X2' es la variable derivada
print(f'fx: {derivada1}')
f= input('digite la funcion con respecto a "Y" que desea derivar: ')
derivada2=diff(f,y)
print(f'fy: {derivada2}')
print('Ahora Vamos hallar los puntos criticos')
print('Para eso igualamos fx=0 y fy=0')
print('')
print('-------------------------------------')
print(f'| {derivada1} = 0   ,  {derivada2} =0  |')
print('-------------------------------------')
print('')

igualar1=solve(Eq(derivada1,0))
print(f'Puntos criticos en "X": {igualar1} ')
igualar2=solve(Eq(derivada2,0))
print(f'Puntos criticos en "Y": {igualar2} ')

#Dobles derivadas
fxx = diff(f,x,2) # Segunda derivada
print(f'fxx: {fxx}')
fyy = diff(f,y,2) # Segunda derivada
print(f'fyy: {fyy}')
fxy = diff(derivada1,y)
print(f'fxy: {fxy}')

print('Digite el punto critico en "X" y "Y" respectivamente')
a=int(input(' "X" --> '))
b=int(input(' "Y" --> '))
#En fxx, fyy,fxy evaluamos los puntos criticos
fxx_=fxx.evalf(subs={x:a,y:b})
fyy_=fyy.evalf(subs={x:a,y:b})
fxy_=fxy.evalf(subs={x:a,y:b})
#Discriminante
d=fxx_*fyy_-fxy**2
print('Formula de discriminante')
print(f'D = {fxx_:.2f} x {fyy_:.2f} - {fxy_}^2')
print(f'D = {d:.2f}')

if d<0:
    print('El punto que acabas de evaluar es de ensilladura')
else:
    pass

 