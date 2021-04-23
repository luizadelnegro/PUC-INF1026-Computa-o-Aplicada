# -*- coding: utf-8 -*-
#########################################################################################
# Nome completo: Luiza Del Negro Ciuffo Fernandes
# Declaração de autoria: declaro que este documento foi produzido por mim em sua totalidade,
#                        sem consultas a outros alunos, professores ou qualquer outra pessoa.
###########################################################################################

class Horario:
    def __init__(self, hhmm):
        self.hora = int(hhmm[:2])
        self.min = int(hhmm[3:])     
        self.tempo = self.hora*60+self.min 
        return
    
    def __str__(self): 
        return "{:0>2d}:{:0>2d}".format(self.hora, self.min)
    def __repr__(self): 
        return "{:0>2d}:{:0>2d}".format(self.hora, self.min)
    def getTempo(self):
        return self.tempo
    def __sub__(self,outro):
       tempo=abs(self.tempo-outro.tempo)
       return tempo
    def __lt__(self,outro):
       return self.tempo<outro.tempo

class Competicao:
    def __init__(self,modalidade,listaPaises,horarioInicio,horarioFim):
        self.modalidade=modalidade
        self.horInic=horarioInicio
        self.horFinal=horarioFim
        self.listaPaises=listaPaises
        return
    def __str__(self): 
        return "Modalidade:{} Duração:{} Países:{:s}".format(self.modalidade,self.getDuracao(),','.join(self.listaPaises))
    def __repr__(self): 
        return "Modalidade:{} Duração:{} Países:{:s}".format(self.modalidade,self.getDuracao(),','.join(self.listaPaises))
    def getDuracao(self):
        return self.horFinal - self.horInic
    def participante(self,pais):
        return pais in self.listaPaises
#------------------------------------------------------------------
#Bloco Principal
tCompeticoes =(  ('basquete',['Brasil', 'Argentina'],'09:00','10:50'),
            ('natação',[ 'Japão', 'USA', 'Alemanha', 'Brasil', 'Chile', 'China', 'Canadá'],'08:00','12:30'),
            ('Corrida',[ 'Jamaica', 'USA', 'Nigéria', 'Brasil', 'Alemanha', 'Cuba'],'14:00','16:30'),
            ('basquete',['Uruguai', 'USA'],'18:00','18:50'),
            ('natação',[ 'Suécia', 'Argentina', 'Áustria', 'Japão', 'Rússia', 'Polonia'],'14:00','16:30'),
            ('voleibol',['Brasil', 'Cuba'],'18:00','21:00'),
            ('Corrida',[ 'Egito', 'Índia', 'Polônia', 'Grécia', 'Equador', 'Colombia'],'17:00','20:00'),
            ('voleibol',['Itália', 'USA'],'18:00','20:00'),
            ('basquete',['França', 'Inglaterra'],'15:00','16:10'),
            ('futebol',['França', 'Espanha'],'10:00','12:10'),
            ('natação',[ 'USA', 'Alemanha', 'Brasil', 'Canadá'],'15:00','15:30'),
            ('basquete',['França', 'Brasil'],'18:00','19:30')
        )    
# Escreva abaixo sua solução

contadorJogoSemBrasil=0
for el in tCompeticoes:
    horarioInicio=Horario(el[2])
    if horarioInicio.hora<12:
        horarioFim=Horario(el[3])
        comp=Competicao(el[0],el[1],horarioInicio,horarioFim)
        print(comp)
        if not comp.participante("Brasil"):
            contadorJogoSemBrasil+=1
print("O Brasil não participou de "+ str(contadorJogoSemBrasil) +" jogos no periodo da manha")
        
        