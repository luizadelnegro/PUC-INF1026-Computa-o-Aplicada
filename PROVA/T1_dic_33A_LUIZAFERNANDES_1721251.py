# -*- coding: latin-1 -*-
# Dicionario
#A########################################################################################
# Turma:33A
# Professor:Claudia Ferlin
# Nome completo:Luiza Del Negro Ciuffo Fernandes
# Matr�cula PUC-Rio:1721251
# Declara��o de autoria: declaro que este documento foi produzido por mim em sua totalidade,
#                        sem consultas a outros alunos, professores ou qualquer outra pessoa.
###########################################################################################

#escreva aqui a funcao alturaDeFilho



'''
Considere as seguintes informa��es referentes a pessoas: nome de seus filhos,
e sua altura, organizadas em 2 dicion�rios como descritos abaixo. 
Nesses dicion�rios o nome de uma pessoa identifica unicamente a pessoa.
=> dicion�rio de pais e filhos onde cada item tem:
    - chave: nome de pessoa
    - valor: lista com o nome de seus filhos.
    O dicion�rio dicPaisFilhos, disponibilizado no template, � apenas um exemplo do dicion�rio
    de pais e filhos.
=> dicion�rio de alturas onde cada item tem:
    - chave: nome de pessoa
    - valor: altura
    O dicion�rio dicAltura, disponibilizado no template, � apenas um exemplo do dicion�rio
    de alturas.
Todo nome existente em dicPaisFilhos tamb�m existe em dicAltura.
'''


def alturaDeFilho(dicPaisFilhos,dicAltura,nome):
    if nome not in dicPaisFilhos:
        return "Essa pessoa nao consta no banco"
    if dicPaisFilhos[nome]==[]:
        return 0
    maior=0.0
    for el in dicPaisFilhos[nome]:
        if el in dicAltura and dicAltura[el]>maior:
            maior=dicAltura[el]
        
    
    return maior
# dicionario de pais e filhos
dicPaisFilhos = { 'Severina':['Elzira','Ernesto'],
               'Oto':['Elzira','Ernesto','Carla'],
               'Marta':['Carla'],
               'Elzira':['Marcia','Alvaro'],
               'Carlos':['Marcia','Alvaro'],
               'Marcia':['Rosinha','Lia'],
               'Markio':['Rosinha','Lia'],
               'Alvaro':['Luis'],
               'Rita':['Luis','Sandro'],
               'Wilson':['Sandro'],
               'Rosinha':['Joana'],
               'Hor�cio':['Joana'],
               'Lia':[],
               'Joana':[],
               'Carla':[],
               'Ernesto':['Karlos','Jorge','Ana'],
               'Miram':['Karlos','Jorge','Ana'],
               'Karlos':['Ricardo','Joice'],
               'Hanna':['Ricardo'],
               'Mara':['Joice'],
               'Joice':[],
               'Jorge':['Marco','Francisca'],
               'Petra':['Marco','Francisca'],
               'Ana':[],
               'Ricardo':['Sara'],
               'Moira':['Sara'],
               'Sara':[],
               'Marco':[],
               'Francisca':[],
               'Luis':[],
               'Sandro':[]
               }
# dicionario de alturas
dicAltura = { 'Severina':1.63,
               'Oto':1.82,
               'Marta':1.54,
               'Elzira':1.72,
               'Carlos':1.78,
               'Marcia':1.64,
               'Markio':1.87,
               'Alvaro':1.69,
               'Rita':1.56,
               'Wilson':1.77,
               'Rosinha':1.83,
               'Hor�cio':1.79,
               'Lia':1.61,
               'Joana':1.57,
               'Carla':1.78,
               'Ernesto':1.75,
               'Miram':1.84,
               'Karlos':1.89,
               'Hanna':1.65,
               'Mara':1.69,
               'Joice':1.57,
               'Jorge':1.91,
               'Petra':1.73,
               'Ana':1.56,
               'Ricardo':1.61,
               'Moira':1.65,
               'Sara':1.76,
               'Marco':1.76,
               'Luis':1.87,
               'Sandro':1.73
               }

# escreva aqui os testes para sua funcao
print(alturaDeFilho(dicPaisFilhos,dicAltura,"Jorge"))
print(alturaDeFilho(dicPaisFilhos,dicAltura,"Sandro"))
print(alturaDeFilho(dicPaisFilhos,dicAltura,"BABABA"))
print(alturaDeFilho(dicPaisFilhos,dicAltura,"Ernesto"))