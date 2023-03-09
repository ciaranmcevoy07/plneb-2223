import re
#EX1
line1 = "hello world"
line2 = "goodbye world"
line3 = "hi, hello there"
def ex11():
    a = re.match(r"^hello", line1)
    b = re.match(r"^hello", line2)
    c = re.match(r"^hello", line3)
    return a,b,c

def ex12():
    a = re.search(r"hello", line1)
    b = re.search(r"hello", line2)
    c = re.search(r"hello", line3)
    return a,b,c

def ex13():
    line = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
    a = re.findall(r"[Hh][Ee][Ll][Ll][Oo]", line)
    return a

#EX2
def palavra_magica(frase):
    a = re.search(r"$por favor?+", frase)
    return a

#EX3
def narcissismo(linha):
    a = re.search(r"\b[Ee]u\b", linha)
    return a

#EX4
def troca_de_curso(linha, novo_curso):
    a = re.sub("LEI", novo_curso, linha)
    return a

#EX5



print(ex11())
print(ex12())
print(ex13())
#print(palavra_magica("Posso ir à casa de banho, por favor?"))
#print(palavra_magica("Preciso de um favor."))
#print(narcissismo("Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou."))
a = input("Introduza um novo curso")
print(troca_de_curso("LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei.", a))
#print(soma_string("4,-6,2,3,8,-3,0,2,-5,1"))

