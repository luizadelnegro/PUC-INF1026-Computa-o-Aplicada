# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:26:34 2021
Object oriented programming class
@author: Luiza Del Negro
"""
import math
class Ponto():
    #atributos:
    x=0 
    y=0
    #construtor:
    def __init__(self,xInicial=0, yInicial=0):
        self.x=xInicial
        self.y=yInicial
        return 
    
    def __str__(self):
        s="(%f,%f)"%(self.x,self.y)
        return s
    
    def __repr__(self): # representacao interna do objeto, no console
        s="[{:4.2f},{:4.2f}]".format(self.x,self.y)
        return s
    
    def __add__(self,toBeAdd):
        if isinstance(toBeAdd,Ponto):
            new=Ponto(self.x+toBeAdd.x, self.y+toBeAdd.y)
        elif isinstance(toBeAdd,int) or isinstance(toBeAdd,float):
            new=Ponto(self.x+toBeAdd,self.y+toBeAdd)
        else:
            new=Ponto(self.x,self.y)
        return new
    def __eq__(self, o):
        if self.x==o.y and self.y==o.y:
            return True
        else:
            return False
    def __gt__(self,o):
        origem=Ponto()
        if self.distancia(origem) > o.distancia(origem):
            return True
        else:
            return False
    
    
    def quadrante(self):
        if self.x>=0:
            if self.y>0:
                return 1
            else:
                return 4
        else:
            if self.y>0:
                return 2
            else:
                return 3
    #dentro da classe ponto:
        #self.distancia()=metodo
        #distancia=variavel
    #fora da classe ponto:
        #ponto.distancia()=metodo
        #distancia=nao existe
    def distancia(self, outroPonto):
        deltaX=self.x-outroPonto.x
        deltaY=self.y-outroPonto.y
        distancia=math.sqrt(deltaX**2+deltaY**2)
        return distancia
    
    def desloca(self, deltaX=0,deltaY=0):
        self.x+=deltaX
        self.y+=deltaY
        return
        