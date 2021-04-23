# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 16:15:55 2020

@author: lcam
@author: Luiza
"""
import math
import convDatas

def calculaCiclo(difDias,duracaoCiclo):
    a = math.sin ( 2*math.pi* difDias / duracaoCiclo) 
    return a

def mostraCicloeMensagem(nomeciclo,valor):
    print("Ciclo " + nomeciclo + " - valor: " + str(valor))
    if valor<=0:
        print("Cuidado, ciclo " + nomeciclo + " esta numa fase critica")
    
    
def MostraCiclos(fis,emoc,intel):
    mostraCicloeMensagem("Fisico",fis)
    
    mostraCicloeMensagem("Emocional",emoc)
    
    mostraCicloeMensagem("Intelectual",intel)

    return

def DiasEntreDatas(dt1,dt2):
    data1=convDatas.GregorianoParaJuliano(dt1)
    data2=convDatas.GregorianoParaJuliano(dt2)
    data=data1-data2
    return data
    
def PerguntaEResponde():
    ''') Faça um programa, utilizando as funções acima, que pergunte a data d
    e seu nascimento (string
‘dd/mm/aaaa’) e a data de uma de suas provas ( string: ‘dd/mm/aaaa’) e
 mostre o valor de cada um dos
ciclos. Caso alguns dos ciclos estejam em um período crítico
 ou negativo envie uma mensagem de alerta.
'''
    dtNasc=input("Por favor, insira sua data de nascimento:\n")
    dtProva=input("Agora, insira sua data de prova:\n")
    fisico=calculaCiclo(DiasEntreDatas(dtNasc,dtProva),23 )
    emocional=calculaCiclo(DiasEntreDatas(dtNasc,dtProva),28)
    intelectual=calculaCiclo(DiasEntreDatas(dtNasc,dtProva),33)
    MostraCiclos(fisico, emocional, intelectual)
    
     
dtNasc='01/12/2000'
dtProva='15/04/2021'
'''
1 - O ciclo Físico - 23 dias de duração
2 - O ciclo Emocional - 28 dias de duração
3 - O ciclo Intelectual - 33 dias de duração 
'''
PerguntaEResponde()

