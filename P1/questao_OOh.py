# -*- coding: utf-8 -*-
#########################################################################################
# Nome completo: Luiza Del Negro Ciuffo Fernandes
# Declaração de autoria: declaro que este documento foi produzido por mim em sua totalidade,
#                        sem consultas a outros alunos, professores ou qualquer outra pessoa.
###########################################################################################

class Entrega:
    def __init__(self,nome,bairro): 
        self.nome=nome          
        self.bairro = bairro         
        self.pesoPorItem=[]
        self.pesoTotal = 0
        return
    
    def __str__(self): 
        s='Nome: {} – Bairro: {} – Peso por item: {} – Peso total: {:.1f} – Valor da Entrega: R$ {:.2f}'.format(self.nome,self.bairro,self.pesoPorItem,self.getPesoTotal(),self.calcValorEntrega()) 
        return s 
    def __repr__(self): 
        s='Nome: {} – Bairro: {} – Peso por item: {} – Peso total: {:.1f} – Valor da Entrega: R$ {:.2f}'.format(self.nome,self.bairro,self.pesoPorItem,self.getPesoTotal(),self.calcValorEntrega()) 
        return s  
   
    def getPesoTotal(self):
          return self.pesoTotal
    def novoItem(self,peso):  
        self.pesoPorItem.append(peso)
        self.pesoTotal+=peso
        return
    def calcValorEntrega(self):
        qt=len(self.pesoPorItem)
        if self.getPesoTotal() <=3:
            return 1.5*qt
        return 2*qt     
    
# Escreva abaixo a classe pedida   
class EntregaRefrigerada(Entrega):
    def __init__(self,nome,bairro,temperatura):
        super().__init__(nome,bairro)
        self.temperatura=temperatura
    def __str__(self): 
        s=super().__str__()
        return s + " - Temperatura : {}".format(self.temperatura)
    def __repr__(self): 
        s=super().__repr__()
        return s + " - Temperatura : {}".format(self.temperatura)
        
    def calcValorEntrega(self):
        valor=super().calcValorEntrega()
        multiplicador=0
        if self.temperatura>0:
            multiplicador=5
        elif self.temperatura<=0 and self.temperatura>-10:
            multiplicador=12
        else:
            multiplicador=20
        qtdItens=0
        for peso in self.pesoPorItem:
            if peso>2:
                qtdItens+=1
        
        return valor+multiplicador*qtdItens
        
    
    



# Retire as aspas abaixo para testar sua classe

entrega = Entrega('Antonio','Copacabana')
print('Entrega')
print(entrega)
entregRef = EntregaRefrigerada('Carla','Ipanema',5)
print('Entrega refrigerada')
print(entregRef)
entrega.novoItem(0.300)
entrega.novoItem(2.300)
entrega.novoItem(4.70)
entregRef.novoItem(0.300)
entregRef.novoItem(2.300)
entregRef.novoItem(4.70)
print('Entrega')
print(entrega)
print('Entrega refrigerada')
print(entregRef)
