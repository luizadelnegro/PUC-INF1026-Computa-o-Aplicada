# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:30:05 2021
Object oriented programming class
@author: Luiza Del Negro
"""
import ponto

#crianod um objeto da classe ponto
p1=ponto.Ponto()
print(p1)#usa o metodo __str__
print("quadrante = ", p1.quadrante())

p2=ponto.Ponto(1,2)
print(p2)

if p1==p2:
    print("P1 iguual a p2")
else:
    print("p1 dif p2")
    
p3=p1+p2
print("P3=P1+P2=>",p3,"=",p1,"+",p2)

p4=p3+10
print("P4=P3+10=>",p4,"=",p3,"+ 10")
if p3>p4:
    print("p3 mais longe")
else:
    print("p4 mais longe")





p5=ponto.Ponto()
if p1==p5:
    print("P1 iguual a p5")
else:
    print("p1 dif p5")



p7=ponto.Ponto(yInicial=-5)
print("P4= ",p7.x,p7.y)
print("Distancia p1 e p7= ",p1.distancia(p7))


p8=ponto.Ponto(yInicial=-6,xInicial=-3)
p8.desloca(3,-7)
print("Desloca p8 em x=3 y=-7 , novo p1",p8.x,p8.y)






