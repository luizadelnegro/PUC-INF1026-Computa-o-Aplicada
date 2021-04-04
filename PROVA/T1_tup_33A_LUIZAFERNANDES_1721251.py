# -*- coding: latin-1 -*-
# Tupla
#A########################################################################################
# Turma:33A
# Professor:Claudia Ferlin
# Nome completo:Luiza Del Negro Ciuffo Fernandes
# Matr�cula PUC-Rio:1721251
# Declara��o de autoria: declaro que este documento foi produzido por mim em sua totalidade,
#                        sem consultas a outros alunos, professores ou qualquer outra pessoa.
###########################################################################################
import math
#escreva aqui as 2 funcoes pedidas

#letra A

def calculoArrecada(t1,t2,t3):
    aDia=t1[1]*t1[2]+t2[1]*t2[2]+t3[1]*t3[2]
    aMax=t1[1]*t1[0]+t2[1]*t2[0]+t3[1]*t3[0]
    return math.floor(aDia/aMax*100)
    
def criaDicHotelArrecadacao(tHoteis):
    dicionario=dict()
    for el in tHoteis:
        arrecada=calculoArrecada(el[2],el[3],el[4])
        print(arrecada)
        if arrecada>=75:
            dicionario[el[0]]=(el[1], "Muito Bom")
        elif arrecada<75 and arrecada>=40:
            dicionario[el[0]]=(el[1], "Normal")
        else:
            dicionario[el[0]]=(el[1], "Ruim")
        
    return dicionario
#letra B
def criaDicCID_MuitoBom(dicionario):
    new=dict()
    #inicializa
    for el in dicionario:
        if dicionario[el][1]=="Muito Bom":
            new[dicionario[el][0]]=0
        
    for el in dicionario:
        if dicionario[el][1]=="Muito Bom":
            new[dicionario[el][0]]=new[dicionario[el][0]]+1
    return new


'''
Um hotel com seus dados cadastrais e a ocupa��o de um determinado dia est�
representado como uma tupla no formato abaixo:

(NomeHotel, cidade,
(totQuartosSimples,valorDiariaSimples,numQuartosSimpleOcupadosNoDia), 
(totQuartosDuplos, valorDiariaDuplo,numQuartosDuplosOcupadosNoDia),
(totQuartosCasal, valorDiariaCasal, numQuartosCasalOcupadosNoDia) )

NomeHotel-> nome do hotel, 
cidade -> cidade onde o hotel est� localizado,
(totQuartosSimples,valorDiariaSimples,numQuartosSimpleOcupadosNoDia)
-->tupla de 3 elementos com o total de quartos simples do hotel,
                    o valor da di�ria do quarto simples e
                    a quantidade de quartos simples ocupados neste dia
totQuartosDuplos, valorDiariaDuplo,numQuartosDuplosOcupadosNoDia)
->tupla de 3 elementos com o total de quartos duplos do hotel,
                    o valor da di�ria do quarto duplo e
                    a quantidade de quartos duplos ocupados neste dia
(totQuartosCasal, valorDiariaCasal, numQuartosCasalOcupadosNoDia)
->tupla de 3 elementos com o total de quartos de casal do hotel,
                    o valor da di�ria do quarto de casal e
                    a quantidade de quartos de casal ocupados neste dia

O grupo de hoteis de uma rede hoteleira � representado como uma tupla de hoteis,
ou seja, uma tupla de tuplas como descritas acima.
'''
#exemplo de tupla de hoteis
tHoteis= (('SUZUKI','RJ',(20,250.50,15),(25,350.50,22),(12,320.50,10)),
        ('MAZZAR','RJ',(40,410.50,25),(20,650.50,8),(20,620.50,10)),
        ('TUNNEL','SP',(30,150.50,15),(30,250.50,12),(5,280.50,2)),
        ('SANSAO','SP',(20,230.50,18),(20,320.50,19),(15,320.50,13)),
        ('MEUMAR','RJ',(32,550.50,12),(30,850.50,16),(20,920.50,10)),
        ('TAMBOR','BH',(18,230.50,15),(15,330.50,12),(10,330.50,10)),
        ('PETECA','RJ',(15,450.50,10),(15,650.50,10),(15,720.50,9)),
        ('CAUCAU','BH',(30,290.50,7),(20,350.50,4),(12,350.50,6)),
        ('TACAPE','SP',(40,250.50,38),(25,380.50,24),(5,320.50,5)),
        ('ZEZZEI','MP',(22,220.50,15),(10,310.50,7),(10,300.50,7)),
        ('TRAPPO','RJ',(14,750.50,3),(10,950.50,2),(12,990.50,4)))
# escreva aqui o teste para suas funcoes
dicionario1=criaDicHotelArrecadacao(tHoteis)
print(dicionario1)

dicionario2=criaDicCID_MuitoBom(dicionario1)
print(dicionario2)