#####################################################################################
#Nome completo:Luiza Del Negro Ciuffo Fernandes
#Matrícula PUC-Rio: 1721251
#Turma:33A
#Professor: Claudia Ferlin
#Declaração de autoria: Declaro que este documento foi produzido por mim em sua totalidade,
######################################################################################
import classeData
from datetime import date

class Pessoa():
    def __init__(self, nome, email, senha,dt='01/01/0000'):
        self.nome=nome
        self.email=email
        self.senha=senha
        [d,m,a]=dt.split('/')
        dia=int(d)
        mes=int(m)
        ano=int(a)
        self.dtNasc=classeData.Data(dia,mes,ano)
        self.filmesAssistidos=[]
        return
    def __str__(self):
        s='Nome: {:s}, email: {:s}, idade: {:d}, filmes assistidos:{}'.format(self.nome,self.email,self.calculaIdadePessoa(),self.filmesAssistidos)
        return s
    def __repr__(self):
        s='Nome: {:s}, email: {:s}, idade: {:d}, filmes assistidos:{}'.format(self.nome,self.email,self.calculaIdadePessoa(),self.filmesAssistidos)
        return s
    
    def exibePessoa(self):
        print(self.nome)
        print(self.email)
        print(self.senha)
        print(self.dtNasc)
        print(self.filmesAssistidos)
        return
    def exibeLista(self):
        for el in self.lista:
            print(self.el)
        return
    
    def setEmail(self,novo):
        self.email=novo
        return
    
    def setSenha(self,novo):
        self.senha=novo
        return
    
    def setAniversario(self,novo):
        [d,m,a]=novo.split('/')
        dia=int(d)
        mes=int(m)
        ano=int(a)
        self.dtNasc=classeData.Data(dia,mes,ano)
        return
    
    def getNome(self):
        return self.nome
    
    def getEmail(self):
        return self.email
    
    def getSenha(self):
        return self.senha
    
    def getAniversario(self):
        return self.dtNasc
        
    def calculaIdadePessoa(self):
        today=date.today()
        hoje=classeData.Data(today.day,today.month,today.year)
        idade=hoje.ano-self.dtNasc.ano-((hoje.mes, hoje.dia) < (self.dtNasc.mes,self.dtNasc.dia))
        return idade