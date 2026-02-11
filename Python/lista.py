frutas = ["laranja", "maca", "uva"]
print(frutas)
frutas = []
print(frutas)
letras = list("python")
print(letras)
numeros = list(range(10))
print(numeros)
carro = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True]
print(carro)

#o primeiro elemento é o indice 0
#de tras pra frente o primeiro numero é -1
frutas = ["laranja", "maca", "uva"]
frutas[0] #laranja
frutas[2] #uva
frutas[-1] #uva
frutas[-3] #laranja


#LISTA ANINHADA MATRIZ

matriz = [
    [1,"a",2 ]
    ["b",3,4 ]
    [6,5,"c" ]
]

matriz[0] # [1, "a", 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"


#FATIAMENTO

lista = ["p", "y", "t", "h","o","n"]

lista[2:] #["t", "h", "o", "n"]
lista[:2] #["p", "y"]
lista[1:3] #["y", "t"]
lista[0:3:2] #["p", "t"]
lista[::] #["p", "y", "t", "h", "o", "n"]
lista[::-1] #["n","o","h","t","y","p"]

#FILTRO

numeros = [1, 30, 21, 2, 9, 65, 34]
pares =[]

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

#mais simplificada versão2
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

# de outro jeito 
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

#mais simplificada versão2
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero ** 2 for numero in numeros]




