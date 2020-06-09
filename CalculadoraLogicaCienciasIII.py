
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
    
aux=0
op=input("ingrese operacion: ")
operacion=[] # lista donde se almacenaran los operadores  
polaca=[] # lista en la que se almacenaran las variables p, q y/o r
arrayOperadores=[] #v,^,>,=,¬
arrayVariables=[] #p,q,r
arraySimbolos=[] #(,)


p='p' # variables
q='q'
r='r'

auxP = 0
auxQ = 0
auxR = 0

numParentesisAbiertos = 0
numParentesisCerrados = 0

contErrores = 0
anterior = ''

try:
    for letra in op:    # ciclo for en el cual se crea la notacion polaca para la resolucion del problema
        if letra=="p":
            polaca.append(p)
            if (auxP==0):
                arrayVariables.append(p)
                auxP+=1
            if (anterior is p or anterior is q or anterior is r):
                contErrores+=1
                print('Se encontró un error en las variables')
                print('Variable conectadas sin operador')
                    
        elif letra=="q":
            polaca.append(q)
            if auxQ==0:
                arrayVariables.append(q)
                auxQ+=1
            if (anterior is p or anterior is q or anterior is r):
                contErrores+=1
                print('Se encontró un error en las variables')
                print('Variable conectadas sin operador')
                    
        elif letra=="r":
            polaca.append(r)
            if auxR==0:
                arrayVariables.append(r)
                auxR+=1
            if (anterior is p or anterior is q or anterior is r):
                contErrores+=1
                print('Se encontró un error en las variables')
                print('Variable conectadas sin operador')
                    
        if letra==")":
            aux-=1
            polaca.append(sacar(operacion,aux))
            arraySimbolos.append(letra)
            numParentesisCerrados+=1
            if (anterior=="^" or anterior=="v" or anterior==">" or anterior=="=" or anterior=="¬"):
                contErrores+=1
                print('Se encontró un error relacionado los parentesis')
                print('Parentesis con operacion sin operandos')
            
        if (letra=="^" or letra=="v" or letra==">" or letra=="=" or letra=="¬"):
            meter(operacion,letra)
            arrayOperadores.append(letra)
            aux+=1
            if (anterior=="^" or anterior=="v" or anterior==">" or anterior=="=" or anterior=="¬"):
                contErrores+=1
                print('Se encontró un error relacionado con los operadores')
                print('Operando antecedido de otro operando')
                
        if letra=="(":
            arraySimbolos.append(letra)
            numParentesisAbiertos+=1
        anterior=letra
    
    
    pila=[]    # pila donde se guardan las variables
    conta=0    # contador
    result=[]  # lista en la cual se va a almacenar el resultado temporal y final de la operacion
       
    if (numParentesisAbiertos != numParentesisCerrados):
        contErrores+=1
        print('Se encontró un error en la cantidad de parentesis')
        print('Parentesis abiertos no coinciden con parentesis cerrados')
    
    if (contErrores > 0):
        print('Se detectaron ' + str(contErrores) + " Errores")
    else:
        print('Escritura en notacion polaca: ' +str(polaca))
        print('Operadores: ' + str(arrayOperadores))
        print('Variables: ' + str(arrayVariables))
        print('Simbolos: ' + str(arraySimbolos))
    
except:
    print('Se encontró un error en los parentesis')
    print('Un parentesis esta vacio o un parentesis tiene una letra sin ningun operando')
    print('Nota: La negacion (¬) es considerada un operando')
    print('Ejecucion detenida')