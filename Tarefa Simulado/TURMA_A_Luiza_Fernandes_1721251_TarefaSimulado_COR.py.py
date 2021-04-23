# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:04:21 2021
Luiza Del Negro Ciuffo Fernandes
Turma A
matricula 1721251
prof Claudia
"""


def corrige(gabarito, lista, endhistograma):
    nota = 0
    q=1
    f = open("questoes.txt", "r")
    content=f.read()
    content_list = content.split("#")
    f.close()
    for el in gabarito:
        print(content_list[q-1])
        resp = input("Digite a resposta da questão %02d: "%(q))
        if resp == el:
            nota+=1
            lista.append(True)
        else:
            endhistograma[q-1]=endhistograma[q-1]+1
            lista.append(False)
        q+=1
    return nota

def exibeCorrecao(matr,nota,Lista):
    print("\n%d- Sua nota é: %d\n"%(matr,nota))
    for (i,el) in enumerate(Lista):
        if el:
            sit ='certo'
        else:
            sit ='errado'
        print('Questão %02i: %s'%((i+1),sit))
     
    return


gab = ['d','d','a','d','b','e','c','c','c','c']
lHistograma= [0,0,0,0,0,0,0,0,0,0]
LMenosAcertos= [0,0,0,0,0,0,0,0,0,0]

matr = int(input("Sua matrícula? "))
while matr != 0:
    lCorrecao = []
    nota = corrige(gab, lCorrecao,LMenosAcertos)
    exibeCorrecao(matr,nota,lCorrecao)
    print(LMenosAcertos)
    matr = int(input("Sua matrícula? "))
