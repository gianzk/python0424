a=10
b=20

def sumav3(a,b):
    c=a+b
    return c

def sumav4(a,b):
    a+=10
    b+=5
    print(a,b)

def potencia2(d):
    print(d**2)

d=sumav3(15,25)
print(d) ## debuggeador
potencia2(d)
sumav4(17,26)
print(a,b)
a=15
b=21
print(a,b)

### errroes comunes
# las variables que se ponen en una funcion son variables temporales
# las variables internas de la funcion no persiten ,solo existen en el alcance de la funcion