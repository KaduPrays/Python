# Exercicio 15                                  #
# https://wiki.python.org.br/ExerciciosListas   #
# Data: 01/03/2022                              #

import os
from distutils.command.clean import clean
from pickle import APPEND


texto = ""
array = 0
lista = []
total = 0

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def limpar():
    if(os.name == 'nt'):
        return os.system('cls')
    else:
        return os.system('clear')

while texto != "stop":
    texto = input();
    if(isfloat(texto)):
        limpar();
        lista.append(texto); 
        print(lista);
else:
    limpar();
    print(lista);


tamlista = len(lista);
print("Total: ", tamlista);

a = list(reversed(lista))
print("Reverso: ", a);

print("Item C - Reverso um de baixo do outro");

for i in range(tamlista) :
    print("%2d | %4.2f" % (i,float(lista[i])));


for i in lista:
   total = total + float(i)


print("Item D - Soma total", total);

media = total / tamlista

print("Item E - Média", media);

print("Item F - Itens a cima da média:");
li = [];
for a in lista:
    if(float(a) > float(media)):
       li.append(a);
       print(a);

print("Item F - Total: ", len(li))
print("Item G - Itens abaixo do valor 7:");

li2 = []
for c in lista:
    if(float(c) < 7):
        li2.append(c);
        print(c);

print("Item G - Total:", len(li2));
print("Encerando o programa");

exit;


