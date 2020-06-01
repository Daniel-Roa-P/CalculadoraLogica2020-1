
"""
integrantes 

# Daniela Alexandra Martinez
# Mateo Yate Gonzalez
# Daniel Alejandro Roa Palacios

"""

"""

Ejemplos de nomenclatura

1) (((¬p)^(qvr))=((qvr)^q))
2) (((¬(¬(pv((¬q)>p)))v(¬(p=(¬q))>(q^(¬p))))))

"""

# se declara un metodo con el cual se podran almacenar los operadores logicos

def meter(lista,op):        
    lista.append(op)

# se declara un metodo que retornara los operadores logicos

def sacar(lista,indice):
    sacar=lista[indice]
    lista.pop(indice)
    return sacar

# se declara un metodo que evalua si la lista de operadores esta vacia o no

def vacia(lista):
    if lista:
        return True
    else:
        return False

# metodo que se encarga de negar los valores booleanos de la lista que recibe

def negar(lista):
    negada=[]
    for i in range (len(lista)):
        negada.append(not lista[i])
    return negada
    
# metodo que realiza el operador o (v) en donde se es falso si ambos valores son falsos

def disyuncion(p,q):
    result=[]
    cont=0
    while cont<len(p):
        result.append(p[cont] or q[cont])
        cont+=1
    return result

# metodo que realiza el operador y (^) en donde se es verdadero si ambos valores son verdaderos

def conjuncion(p,q):
    result=[]
    cont=0
    while cont<len(p):
        result.append(p[cont] and q[cont])
        cont+=1
    return result

# metodo que realiza el operador entonces (>) en donde se es falso si el primero es verdadero y el segundo es falso

def imp(p,q):
    result=[]
    cont=0
    while cont<len(p):
        if p[cont]==True and q[cont]==False:
            result.append(False)
            cont+=1
        else:
            result.append(True)
            cont+=1
    return result

# metodo que realiza el operador si solo si (=) en donde es verdadero si ambos valores poseen el mismo valor

def implicacion_doble(p,q):
    lista1 = imp(p,q)
    lista2 = imp(q,p)
    lista3 = conjuncion(lista1,lista2)
    return lista3

try:
    print("A continuación vera un ejemplo de como debe ingresar la operación para"+ 
          " obtener la solución acertadamente: (((¬p)^(qvr))=((qvr)^q))")
    
    
    
    aux=0
    op=input("ingrese operacion: ")
    operacion=[] # lista donde se almacenaran los operadores  
    polaca=[] # lista en la que se almacenaran las variables p, q y/o r
    
    p=[True, True, True, True, False, False, False, False] # variables
    q=[True, True, False, False, True, True, False, False]
    r=[True, False, True, False, True, False, True, False]
    
    for letra in op:    # ciclo for en el cual se crea la notacion polaca para la resolucion del problema
        if letra=="p":
            polaca.append(p)
        elif letra=="q":
            polaca.append(q)
        elif letra=="r":
            polaca.append(r)
        if letra==")":
            aux-=1
            polaca.append(sacar(operacion,aux))
        if (letra=="^" or letra=="v" or letra==">" or letra=="=" or letra=="¬"):
            meter(operacion,letra)
            aux+=1
    
    pila=[]    # pila donde se guardan las variables
    conta=0    # contador
    result=[]  # lista en la cual se va a almacenar el resultado temporal y final de la operacion
    
    for valor in polaca:    # ciclo en el que se opera la expresion polaca segun como esta este construida
        if valor==p or valor==q or valor==r:
            meter(pila,valor)
            conta+=1
        else:
            if valor=="^":
                result=conjuncion(sacar(pila,conta-1),sacar(pila,conta-2))
                conta-=1
            elif valor=="v":
                result=disyuncion(sacar(pila,conta-1),sacar(pila,conta-2))
                conta-=1
            elif valor==">":
                lista1=sacar(pila,conta-1)
                lista2=sacar(pila,conta-2)
                result=imp(lista2,lista1)
                conta-=1
            elif valor=="=":
                result=implicacion_doble(sacar(pila,conta-1),sacar(pila,conta-2))
                conta-=1
            elif valor=="¬":
                result=negar(sacar(pila,conta-1))
            meter(pila,result)
       
    print(polaca)
    print()
    print("solucion: ")
    print(pila[0])
except:
    print("Error: La proposicion está mal escrita")