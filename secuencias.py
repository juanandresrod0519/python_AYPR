from unittest import skip

def evaluarExpresion(e):
    n=0
    for l in e:
        if (l=='('):
            n+=1
        elif (l==')'):
            n-=1
        else:
            skip
    if (n==0):
        return True
    return False

def evaluarOcurrencias(c,e):
    n=0
    for l in e:
        if (l==c):
            n+=1
    return n

def main():
    print("Hello ¯\_(ツ)_/¯ Ejercicio-2-3")
    e= input("ingresa la expresion a evaluar (ej:(a + b) / 2): ")
    print(evaluarExpresion(e))
    c= input("ingresa el caracter al que se le evaluaran las ocurrencias (ej:a): ")
    e= input("ingresa la expresion a evaluar (ej:hola mundo): ")
    n= evaluarOcurrencias(c,e)
    print(f"Numero de ocurrencias: {n}")
    
if __name__ == '__main__':
    main()