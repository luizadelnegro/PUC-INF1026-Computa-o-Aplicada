# -*- coding: utf-8 -*-
#########################################################################################
# Nome completo: Luiza Del Negro Ciuffo Fernandes
# Declaração de autoria: declaro que este documento foi produzido por mim em sua totalidade,
#                        sem consultas a outros alunos, professores ou qualquer outra pessoa.
###########################################################################################
'''
ATENÇÃO: não pode haver criação de dicionários por enumeração, com exceção dos 
já disponibilizados.
'''
'''
Escreva uma função, denominada criaDicStatusNotasFinais, que:
    - receba um dicionário de candidatos, um dicionário de áreas e o nome de um 
    candidato. Considere que sempre será um nome de candidato existente no dicionario.
    Ambos dicionarios contém os mesmos quesitos. 
    - crie e retorne um dicionário com o STATUS e as 
    notas finais do candidato por AREA, 
    em  que cada elemento e´
    
        AREA: Tupla com (STATUS, NotaFinal do candidato), considerando a nota mínima e os 
               pesos dessa área         
    OBS1:              
      CHAVE => Área
      VALOR => Tupla com ('Eliminado' ou 'Aprovado', NotaFinal na área)   
    OBS2: Uma candidato está Eliminado em uma área se a nota de algum quesito for menor 
    do que a mínima especificada para o quesito na área    
 
Exemplo: Para os dicionários apresentados e a área ATENDIMENTO o dicionário construído 
e retornado pela função seria:
    {'ATENDIMENTO': ('Eliminado', 65.0), 'ADMINISTRACAO': ('Eliminado', 68.0), 'RECURSOSHUMANOS': ('Aprovado', 60.0),
     'TECNOLOGIA': ('Aprovado', 79.0)}
'''
#escreva a funcao pedida


def criaDicStatusNotasFinais(dicionarioCandidatos,dicionarioAreas,nomeCandidato):
    candidato=dicionarioCandidatos[nomeCandidato]
    novoDicCandidato=dict()
    for area in dicionarioAreas:
        soma=0
        for topic in dicionarioAreas[area]:
            soma+=candidato[topic]*dicionarioAreas[area][topic][1]
        media=soma/10
        if media>=dicionarioAreas[area][topic][0]:
            novoDicCandidato[area]=('Aprovado',media)
        else:
            novoDicCandidato[area]=('Eliminado',media)
    return novoDicCandidato



            
dicCandidatos= {
           'Brian': {'comunicacao':65, 'trabEquipe':60, 'autonomia':50, 'tecnologia':40, 'conhecimentoEmp':75},
           'Ellen': {'comunicacao':80, 'trabEquipe':40, 'autonomia':30, 'tecnologia':70, 'conhecimentoEmp':80},
           'Nikki': {'comunicacao':35, 'trabEquipe':60, 'autonomia':80, 'tecnologia':80, 'conhecimentoEmp':40},   
           'David': {'comunicacao':70, 'trabEquipe':55, 'autonomia':50, 'tecnologia':65, 'conhecimentoEmp':50}, 
           'Lasse': {'comunicacao':60, 'trabEquipe':60, 'autonomia':90, 'tecnologia':90, 'conhecimentoEmp':40},
           'Katie': {'comunicacao':45, 'trabEquipe':60, 'autonomia':50, 'tecnologia':40, 'conhecimentoEmp':60},
           'Tommy': {'comunicacao':90, 'trabEquipe':90, 'autonomia':50, 'tecnologia':40, 'conhecimentoEmp':50}
           }

dicAreas= {
      'ATENDIMENTO': {'comunicacao':( 70,4), 'trabEquipe':(30,1), 'autonomia':(30,2), 'tecnologia':(30,1), 'conhecimentoEmp':(65,2)},
      'ADMINISTRACAO': {'comunicacao':(40,2), 'trabEquipe':(60,2), 'autonomia':(50,2), 'tecnologia':(40,2), 'conhecimentoEmp':(55,2)},
      'RECURSOSHUMANOS':{'comunicacao':(60,3), 'trabEquipe':(60,2), 'autonomia':(40 ,1), 'tecnologia':(30,1), 'conhecimentoEmp':(40,3)},
      'TECNOLOGIA': {'comunicacao':(40,1), 'trabEquipe':(50,1), 'autonomia':(70,3), 'tecnologia':(70,4), 'conhecimentoEmp':(30,1)}
     }    

#teste sua funcao exibindo o dicionario retornado
print("Candidato Brian")
print(criaDicStatusNotasFinais(dicCandidatos,dicAreas,'Brian'))
print("Candidata Ellen")
print(criaDicStatusNotasFinais(dicCandidatos,dicAreas,'Ellen'))
print("Candidata Nikki")
print(criaDicStatusNotasFinais(dicCandidatos,dicAreas,'Nikki'))
print("Candidata David")
print(criaDicStatusNotasFinais(dicCandidatos,dicAreas,'David'))
