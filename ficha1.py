import re

def numerosPares(array):
    listapares =[]
    for i in array:
        if i % 2 == 0:
            listapares.append(i)
    return listapares


def nomeFicheiroInverso(nf):
    inverso = nf[::-1]
    print(inverso)


def occurrenciasf(b):
    file = open(b, 'r')
    content = file.read()
    lista = content.split(" ")
    dict={}
    counter = 0
    for i in lista:
        for keys in dict.keys():
            if i == keys:
                dict[i] += 1
                counter += 1
                break
        if counter == 0:
            dict.update({i:1})
    maioresvalores = sorted(dict.items(), key=lambda x:x[1], reverse=True,)[:10]
    return maioresvalores

def removepontuacao(arg):
    str = arg.lower()
    new1 = re.sub("[áàãâ]", "a",str)
    new2 = re.sub("[õô]", "o", new1)
    new3 = re.sub("ç", "c", new2)
    lista = re.split(", |,|:| |\n", new3)
    string = ' '.join(lista)
    return string

def reverse(a):
    inverso = a[::-1]
    return inverso

def numerodeA(a):
    lista = []
    contador = 0
    for i in a:
        lista.append(i)
    for o in lista:
        if o == "a" or o =="A":
            contador += 1
    return contador

def numerodevogais(a):
    b= a.lower()
    lista = []
    contador = 0
    for i in b:
        lista.append(i)
    for o in lista:
        if o == "a" or o == "e" or o == "i" or o == "o" or o == "u":
            contador += 1
    return contador

def upper(a):
    b = a.upper()
    return b

def lower(a):
    b = a.lower()
    return b
                
nome = input("Introduz Nome:")
print(nome.upper())
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = input("Nome de Ficheiro:")
print(numerosPares(a))
nomeFicheiroInverso(b)
print(occurrenciasf(b))
texto = input("Introduza uma texto:")
print(removepontuacao(texto))
print(reverse(texto))
print(numerodeA(texto))
print(numerodevogais(texto))
print(upper(texto))
print(lower(texto))