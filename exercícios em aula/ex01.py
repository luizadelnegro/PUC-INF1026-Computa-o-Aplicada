# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 08:19:40 2021

@author: Luiza

The program creates a date(dd/mm) that should be guessed by the user.
First, the program generates a value for the day and for the month,
 then creates the string, representing the date that should be guessed.
 
"""
from random import randint

def geraData():
    mes=randint(1,12)
    if mes%2==0:
        if mes==2:
            dia=randint(1, 28)
        else:
            dia=randint(1, 30)
    else:
        dia=randint(1, 31)
        
    return '%02d/%02d'%(dia,mes)

def avaliaChute(chute,data):
    slice_chute=chute.split('/')#separa onde queremos criando uma lista com os elementos
    slice_data=data.split('/')
#acertou o mes  
    if slice_chute[1]==slice_data[1]:
        #dia dentro do intervalo
         if int(slice_data[0])-5<= int(slice_chute[0])<=int(slice_data[0])+5:
             return print('O mês ✔ data ∈ !\n')
         else:#dia fora do intervalo
             return print('O mês ✔ data ∉ !\n')
#mes dentro do intervalo
    if int(slice_data[1])-5<= int(slice_chute[1])<=int(slice_data[1])+5:
                #dia correto
        if slice_chute[0]==slice_data[0]:
             return print('O mês ∈ data ✔ !\n')
        #dia dentro do intervalo
        if int(slice_data[0])-5<= int(slice_chute[0])<=int(slice_data[0])+5:
             return print('O mês ∈ data ∈ !\n')
        else:#dia fora do intervalo
             return print('O mês ∈ data ∉ !\n')
#mes fora do intervalo
    else:
        #dia no intervalo
        if int(slice_data[0])-5<= int(slice_chute[0])<=int(slice_data[0])+5:
            return print('O mês ∉  data ∈ !\n')
        #dia certo
        if slice_chute[0]==slice_data[0]:
            return print('O mês ∉ data ✔ !\n')
        #dia fora do intervalo
        else: 
            return print('Mes e dia ∉  !\n')

    

def adivinhaData():
    data=geraData()
    print(data)
    contador=5
    found=False
    while(contador>0 & found==False):
        chute=input('Digite dd/mm:')
        if data==chute:
            print('Parabéns você acertou!')
            found=True
        else:
            avaliaChute(chute,data)
            contador=contador-1
            print('Você errou! Tente novamente! Tentativas restantes: %02d'%(contador))
    
    

data=adivinhaData()
