#Funciones, ejemplo de como se ejecutan

"""
def mifuncion():
    print("nombre")
    print("Holi")

    for i in range(1, 5):
        print(i)


print("Antes")

mifuncion()

print("Despues")
"""

#Como funcionan las funciones
"""
def mifuncion(nombre):
    print("Hola", nombre)

def matematicas(a, b):
    
    def suma (a, b):
        print(a + b)

    def resta (a, b):
        print(a - b)

    suma(a, b)
    resta(a, b)

matematicas(10, 2)
"""

#Las variables fuera de una funcion si pueden ser usadas dentro de una funcion como por ejemplo
"""
temperatura = 20

def mifuncion(nombre):
    hoyhace = 15
    print("temperatura", temperatura)
    print("hola,", nombre, "la temperatura es de:", hoyhace)

mifuncion("Daniel")
"""

#si tengo una variable de ambito global con el mismo nombre que una de ambito local, es decir en la funcion, prevalece la de ambito local
#cuando se repitw se denomina Variable Shasowing
"""
hoyhace = 20

def mifuncion(nombre):
    hoyhace = 15
    print("hola,", nombre, "la temperatura es de:", hoyhace)

mifuncion("Daniel")
"""

#Si se pone a una variable antes la palabra global esta afectara a todas las que lleven el mismo nombre
"""
hoyhace = 20
print(hoyhace)

def mifuncion(nombre):
    global hoyhace 
    hoyhace = 15
    print("hola,", nombre, "la temperatura es de:", hoyhace)

mifuncion("Daniel")
print(hoyhace)
"""

#Parametros opcionales
#no puede haber un parametro en medio que sea opcional (a, b=5, c) NO SE PUEDE
"""
def mifuncion(nombre="Daniel"):
    print("Hola,", nombre)

mifuncion()
mifuncion("Felipe")
"""

#puedo cambiar solo una variable si asi lo deseo
"""
def suma (a=1, b=5, c=10):
    print(a + b + c)
    
suma(c=20)

#se pueden pasar en el orden que se desee pero de la siguiente manera
suma(b=1, c=3, a=2)
"""

#Parametros Variables - se puede llamar de cualquier manera con un * se crea una tupla
"""
def suma (*args):
    resultado = 0

    for i in args:
        resultado += i
    
    print(resultado)

suma(9, 9)
"""

#se crea un diccionario con dos **
"""
def suma (**kwargs):
    print(kwargs)

suma(vivienda="piso", coche= "rojo")


def suma (**kwargs):
    if "coche" not in kwargs:
        return
    
    if kwargs ["coche"] == "bonito":
        print("Tu coche es bonito")

suma(coche="bonito")
"""
#Funciones devuelven valores RETURN
"""
def suma (a, b):
    return a + b

resultado = suma (3, 4)
print(resultado)
"""

"""
def operaciones(a, b):
    return a + b, a - b, a * b, a / b

suma, resta, multi, divi = operaciones (2, 4)
print(suma)
print(resta)
print(multi)
print(divi)

print()

#otra manera de imprimir

res = operaciones (2, 4)
print(res[1]) 
"""

#funcion anonima debe tener lambda

sumar = lambda x: x + x
print(sumar(4))

