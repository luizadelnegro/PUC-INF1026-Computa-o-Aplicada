# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:04:21 2021

@author: Ferlin
@author: Luiza
"""

'''
MODIFICAÇÃO 1:
    Alterar o programa para que a função corrige 
    exiba o enunciado das questões a cada aluno. 
    O enunciado das questões está no arquivo "questões.txt" 
    e tem como separador o caractere '#'. 
    O arquivo está disponível no EaD.
    Lembre-se que um arquivo só deve ser lido uma vez ( copiá-lo para uma lista )

'''
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

'''MODIFICAÇÃO 2:
    Alterar o programa para exibir, no final, 
    o número de alunos que acertaram cada uma das questões, 
    isto é, quantos alunos acertaram a questão 1, 
    quantos alunos acertaram a questão 2 e 
    assim sucessivamente (histograma por questão)
    DICA: crie uma lista com 10 zeros ( lHistograma)
          Esta lista deve ser atualizada pela função corrige
          Use o número da questão como indexador de lHistograma
'''
