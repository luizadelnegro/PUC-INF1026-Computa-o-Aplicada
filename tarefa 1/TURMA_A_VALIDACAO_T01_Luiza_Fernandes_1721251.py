# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 17:53:54 2021

@author: Ferlin
@author: Luiza Del Negro Ciuffo Fernandes
Matrícula:1721251
Turma:33A
Professora: Claudia Ferlin
"""


""" QUESTAO 1"""

def agrupaEntradasPorVinhosEscolhidos (tupla_entrada_vinhos, lista_vinhos):
    dicionario_vinhos=dict()
    for vinho in lista_vinhos:
        dicionario_vinhos[vinho]=[]

    for el in tupla_entrada_vinhos:
        for vinho in el[1]:
            if vinho in dicionario_vinhos.keys():
                dicionario_vinhos[vinho].append(el[0])
    return dicionario_vinhos


""" QUESTAO 2"""
def montaDicionario(tupla_de_tuplas):
    dicionario=dict()
    for el in tupla_de_tuplas:
        for entrada in el[0]:
            dicionario[el[0]]=el[1]
    return dicionario
    
""" QUESTAO 3"""
def contabilizaPrimeiraOpcao(dVinhosEntrada, dVinhosPrato):
    dicionario=dict()
    for entrada in dVinhosEntrada:
        vinhos=dVinhosEntrada[entrada]
        for vinho in vinhos:  
            if vinho in dicionario:
                tuple=dicionario[vinho]
                value=tuple[0]+1
                dicionario[vinho]=(value,0)
            else:
                dicionario[vinho]=(1,0)
                tuple=dicionario[vinho] 
    for prato in dVinhosPrato:
        vinhos=dVinhosPrato[prato]
        for vinho in vinhos:
            if vinho in dicionario:
                tuple=dicionario[vinho] 
                value_prato=tuple[1]+1
                value_entrada=tuple[0]
                dicionario[vinho]=(value_entrada,value_prato)
            else:
                dicionario[vinho]=(0,1)

    return dicionario
    

""" QUESTAO 4"""
def possibilidadesVinho(dVinhosEntrada, dVinhosPrato, dIntTempVinho, prato, entrada):
    if prato not in dVinhosPrato:
        print("entrada:%s \n"%entrada)
        print("prato:%s \n"%prato)
        print("Prato não consta no consta no menu")
        return
    if entrada not in dVinhosEntrada:
        print("entrada:%s \n"%entrada)
        print("prato:%s \n"%prato)
        print("Entrada não consta no consta no menu")
        return
    vinhos_entrada=dVinhosEntrada[entrada]
    vinhos_prato=dVinhosPrato[prato]
    vinhos_comuns=[]
    for vinho in vinhos_entrada:
        if vinho in vinhos_prato:
            vinhos_comuns.append(vinho)
    print("entrada:%s \n"%entrada)
    print("prato:%s \n"%prato)
    if vinhos_comuns==[]:
        print("Não há vinhos comuns à entrada e ao prato")
        return
    else:
        for vinho in vinhos_comuns:
            dIntTempVinho[vinho]
            print("Vinho %s servido na temperatura entre %0.1f a %0.1f graus.\n"%(vinho, dIntTempVinho[vinho]['min'],dIntTempVinho[vinho]['max']))
        return
            
   
""" QUESTAO 5"""

def opcoesDaEstacao(dVinhosEntrada, dVinhosPrato,dVinhosEstacao, estacao):
    vinhos_estacao=dVinhosEstacao[estacao]
    dicionario=dict()
    for el in vinhos_estacao:
        dicionario[el]={'Entrada':[],'Prato':[]}
    for entrada in dVinhosEntrada:
        vinhos_entrada=dVinhosEntrada[entrada]
        for vinho in vinhos_entrada:
            if vinho in dicionario:
                dicionario[vinho]['Entrada'].append(entrada)
    for prato in dVinhosPrato:
        vinhos_prato=dVinhosPrato[prato]    
        for vinho in vinhos_prato:
            if vinho in dicionario:
                dicionario[vinho]['Prato'].append(prato)
    return dicionario


def printDicionario1(dicionario):
    for el in dicionario:
        print(el+":")
        
        for content in dicionario[el]:
            print("\t" +content)
    return

def printDicionario2(dicionario):
    for el in dicionario:
        print(el+":")
        print("\t Quantidade de entradas: %i"%dicionario[el][0])
        print("\t Quantidade de pratos: %i"%dicionario[el][1])
    return
  
def printDicionario3(dicionario):
    for el in dicionario:
        print(el+":")
        for item in dicionario[el]:
            print("\t"+item+":")
            for content in dicionario[el][item]:
                print("\t\t"+content)
 
    return

def validacao (dicionario, vinho1, vinho2):
    if vinho1 in dicionario and vinho2 in dicionario :
        v1=dicionario[vinho1][0]+dicionario[vinho1][1]
        v2=dicionario[vinho2][0]+dicionario[vinho2][1]
        if v1<v2:
            return ((vinho2,v2),(vinho1,v1))
        else:
            return ((vinho1,v1),(vinho2,v2))
    
    if vinho2 not in dicionario:
        return (vinho2)
    if vinho1 not in dicionario:
        return (vinho1)
    else:
        return (vinho1,vinho2)
    


dIntTempVinho={
   'espumante':{'min':6,'max':8},
   'rosé':{'min':6,'max':8},
   'branco leve':{'min':6,'max':8},
   'branco médio corpo':{'min':9,'max':11},
   'branco encorpado':{'min':10,'max':12},
   'tinto leve':{'min':10,'max':12},
   'tinto médio corpo':{'min':14,'max':15},
   'tinto encorpado':{'min':17,'max':18}
}

dVinhosEstacao={
   'primavera':('rosé','espumante','branco leve','tinto leve'),
   'verão':('rosé','espumante','branco leve'),
   'outono':('branco médio corpo','branco encorpado','tinto médio corpo'),
   'inverno':('tinto encorpado','tinto médio corpo','tinto leve','branco encorpado')
}

dEntradasVinho={
'rosé': ['Salada caprese',  'Brie empanado',  'Bruschetta',  'Falafel rosa',  'Iscas de tilápia',  'Lula dorê','Pipoca temperada',  'Tábua de queijos',  'Tapas de salmão defumado'],
 'espumante': ['Salada caprese', 'Falafel rosa', 'Iscas de tilápia', 'Lula à dorê', 'Pipoca temperada',  'Tapas de salmão defumado'],
 'branco leve': ['Salada caprese',  'Brie empanado',  'Bruschetta',  'Canapé Brandade de bacalhau',  'Falafel rosa',  'Iscas de tilápia',  'Lula à dorê',  'Pipoca temperada',  'Tábua de queijos',  'Tapas de salmão defumado'],
 'branco médio corpo': ['Brie empanado',  'Bruschetta',  'Iscas de filé-mignon',  'Iscas de tilápia',  'Lula à dorê',  'Tábua de queijos',  'Tapas de salmão defumado',  'Calabresa acebolada'],
 'tinto leve': ['Bruschetta',  'Canapé Brandade de bacalhau',  'Cheddar',  'Salaminho',  'Dadinho de tapioca',  'Empanadinho de provolone',  'Lula à dorê',  'Pipoca temperada',  'Tábua de queijos',  'Tapas de salmão defumado'],
 'tinto encorpado': ['Presunto Parma',  'Canapés de queijo coalho',  'Cheddar',  'Salaminho',  'Dadinho de tapioca',  'Empanadinho de provolone',  'Iscas de filé-mignon',  'Bacon',  'Tábua de queijos',  'Calabresa acebolada'],
 'tinto médio corpo': ['Presunto Parma',  'Cheddar',  'Salaminho',  'Iscas de filé-mignon',  'Bacon',  'Tábua de queijos',  'Calabresa acebolada'],
 'branco encorpado': ['Canapés de queijo coalho', 'Dadinho de tapioca','Iscas de filé-mignon','Bacon',  'Calabresa acebolada']
}
dPratosVinho={
'espumante': ['Massa em molho leve', 'Massa em molho branco','Massa em molho condimentado','Massa em molho vermelho','Carne vermelha grelhada','Carne vermelha em molho leve','Carne branca grelhada','Carne branca em molho leve','Sushi'],
 'rosé': ['Massa em molho leve', 'Carne vermelha grelhada', 'Sushi'],
 'branco leve': ['Massa em molho leve','Massa em molho branco','Carne branca grelhada','Carne branca em molho leve','Sushi'],
 'branco médio corpo': ['Massa em molho leve','Massa em molho branco','Carne branca grelhada','Carne branca em molho leve','Sushi'],
 'branco encorpado': ['Massa em molho leve','Massa em molho branco','Carne branca grelhada','Carne branca em molho leve','Peru'],
 'tinto leve': ['Massa em molho leve', 'Massa em molho branco','Carne vermelha grelhada','Carne vermelha em molho leve','Carne branca grelhada','Carne branca em molho leve','Peru'],
 'tinto médio corpo': ['Massa em molho leve','Massa em molho branco', 'Massa em molho condimentado', 'Massa em molho vermelho','Carne vermelha grelhada','Carne vermelha em molho leve', 'Carne vermelha em molho forte','Carne branca grelhada','Carne branca em molho leve',  'Carne branca em molho forte','Peru'],
 'tinto encorpado': ['Massa em molho condimentado', 'Massa em molho vermelho','Carne vermelha em molho forte','Caças de pêlo','Carne branca em molho forte']
}

tEntradaVinhos=(
        ('Salada caprese',('rosé','espumante','branco leve')),
        ('Brie empanado',('branco leve','branco médio corpo','rosé')),
        ('Bruschetta',('branco leve','branco médio corpo','rosé','tinto leve')),
        ('Presunto Parma',('tinto encorpado','tinto médio corpo')),
        ('Canapé Brandade de bacalhau',('branco leve','tinto leve')),
        ('Canapés de queijo coalho',('tinto encorpado','branco encorpado')),
        ('Cheddar',('tinto leve','tinto médio corpo','tinto encorpado')),
        ('Salaminho',('tinto médio corpo','tinto encorpado','tinto leve',)),
        ('Dadinho de tapioca',('tinto encorpado','tinto leve','branco encorpado')),
        ('Empanadinho de provolone',('tinto leve','tinto encorpado')),
        ('Falafel rosa',('espumante','branco leve','rosé')),
        ('Iscas de filé-mignon',('tinto encorpado','branco encorpado','tinto médio corpo','branco médio corpo')),
        ('Iscas de tilápia',('branco leve','espumante','branco médio corpo','rosé')),
        ('Lula à dorê',('branco leve','espumante','branco médio corpo','rosé','tinto leve')),
        ('Bacon',('tinto médio corpo','tinto encorpado','branco encorpado')),
        ('Pipoca temperada',('espumante','branco leve','tinto leve','rosé')),
        ('Tábua de queijos',('tinto médio corpo','tinto encorpado','branco médio corpo','rosé','tinto leve','branco leve')),
        ('Tapas de salmão defumado',('branco leve','branco médio corpo','rosé','espumante','tinto leve')),
        ('Calabresa acebolada',('tinto encorpado','branco encorpado','tinto médio corpo','branco médio corpo'))
)

tPratoPrincipalVinhos = (
    ('Massa em molho leve',('espumante','rosé','branco leve','branco médio corpo','branco encorpado','tinto leve','tinto médio corpo')),
    ('Massa em molho branco',('espumante','branco leve','branco médio corpo','branco encorpado','tinto leve','tinto médio corpo')),
    ('Massa em molho condimentado',('espumante','tinto médio corpo','tinto encorpado')),
    ('Massa em molho vermelho',('espumante','tinto médio corpo','tinto encorpado')),
    ('Carne vermelha grelhada',('espumante','rosé','tinto leve','tinto médio corpo')),
    ('Carne vermelha em molho leve',('espumante','tinto leve','tinto médio corpo')),
    ('Carne vermelha em molho forte',('tinto médio corpo','tinto encorpado')),
    ('Caças de pêlo',('tinto encorpado',)),
    ('Carne branca grelhada',('espumante','branco leve','branco médio corpo','branco encorpado','tinto leve','tinto médio corpo')),
    ('Carne branca em molho leve',('espumante','branco leve','branco médio corpo','branco encorpado','tinto leve','tinto médio corpo')),
    ('Carne branca em molho forte',('tinto médio corpo','tinto encorpado')),
    ('Peru',('tinto leve','tinto médio corpo','branco encorpado')),
    ('Sushi',('espumante','branco leve','branco médio corpo','rosé'))
   )


"""BLOCO PRINCIPAL"""


""" QUESTAO 1"""
print(" QUESTÃO 1 \n")
print(" Entradas que harmonizam com os vinhos escolhidos: \n")
dEntradaVinhoNovo=agrupaEntradasPorVinhosEscolhidos(tEntradaVinhos,
                                                    ('espumante', 'tinto encorpado'))
printDicionario1(dEntradaVinhoNovo)
print("\n ------------------------------------------------------------------- \n")


""" QUESTAO 2"""
print(" \n QUESTÃO 2 \n")
print(" ~ Dicionario dVinhosEntrada: \n")
dVinhosEntrada=montaDicionario(tEntradaVinhos)
printDicionario1(dVinhosEntrada)
print("\n ************************************ \n")
print(" \n ~ Dicionario dVinhosPrato: \n")
dVinhosPrato=montaDicionario(tPratoPrincipalVinhos)
printDicionario1(dVinhosPrato)
print("\n ------------------------------------------------------------------- \n")

""" QUESTAO 3"""
print("\n QUESTÃO 3 \n")
print(" Contabiliza Entradas e pratos para cada vinho: \n")
dicionarioval=contabilizaPrimeiraOpcao(dVinhosEntrada,dVinhosPrato)
printDicionario2(dicionarioval)
print("\n ------------------------------------------------------------------- \n")

""" QUESTAO 4 """
print("\n QUESTÃO 4 \n")
print(" Harmonizações de vinho para o conjunto de prato e entrada: \n")
possibilidadesVinho(dVinhosEntrada, dVinhosPrato, dIntTempVinho, "Massa em molho leve", "Salada caprese")
print("\n ************************************ \n")
possibilidadesVinho(dVinhosEntrada, dVinhosPrato, dIntTempVinho, "Caças de pêlo", "Salada caprese")
print("\n ************************************ \n")
possibilidadesVinho(dVinhosEntrada, dVinhosPrato, dIntTempVinho, "Caças de pêlo", "Salaprese")
print("\n ************************************ \n")
possibilidadesVinho(dVinhosEntrada, dVinhosPrato, dIntTempVinho, "Calo", "Salaprese")
print("\n ------------------------------------------------------------------- \n")



""" QUESTAO 5 """
print("\n QUESTÃO 5 \n")
print(" Harmonizações de vinhos da estação PRIMAVERA com os pratos e entradas do menu: \n")
dOpcoesEstacao=opcoesDaEstacao(dVinhosEntrada, dVinhosPrato,dVinhosEstacao,"primavera")
printDicionario3(dOpcoesEstacao)
print("\n ************************************ \n")
print(" Harmonizações de vinhos da estação VERÃO com os pratos e entradas do menu: \n")
dOpcoesEstacao=opcoesDaEstacao(dVinhosEntrada, dVinhosPrato,dVinhosEstacao,"verão")
printDicionario3(dOpcoesEstacao)
print("\n ************************************ \n")
print(" Harmonizações de vinhos da estação OUTONO com os pratos e entradas do menu: \n")
dOpcoesEstacao=opcoesDaEstacao(dVinhosEntrada, dVinhosPrato,dVinhosEstacao,"outono")
printDicionario3(dOpcoesEstacao)
print("\n ************************************ \n")
print(" Harmonizações de vinhos da estação INVERNO com os pratos e entradas do menu: \n")
dOpcoesEstacao=opcoesDaEstacao(dVinhosEntrada, dVinhosPrato,dVinhosEstacao,"inverno")
printDicionario3(dOpcoesEstacao)


""" VALIDACAO """
print(validacao(dicionarioval,"rosé","branco leve"))



