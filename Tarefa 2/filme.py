#####################################################################################
#Nome completo:Luiza Del Negro Ciuffo Fernandes
#Matrícula PUC-Rio: 1721251
#Turma:33A
#Professor: Claudia Ferlin
#Declaração de autoria: Declaro que este documento foi produzido por mim em sua totalidade,
######################################################################################
import classeHorario

class Filme():
    def __init__(self, titulo, duracao):
        self.titulo=titulo
        #######
        self.duracao=classeHorario.geraHorario(duracao)
        ###
        self.qtdVisualizacoes=0
        self.qtdCurtidas=0
        self.qtdNaoCurtidas=0
        self.dictAvaliacao=dict()
        self.dictAvaliacao['somaNotas']=0
        self.dictAvaliacao['qtNotas']=0
        return
    
    def __str__(self):
        s= 'Titulo: {:s} - Duracao:{} - Quantidade de Visualizacoes: {} - Quantidade de Curtidas: {} - Quantidade nao curtidas:{} - Avaliacao:{}'.format(self.titulo,self.duracao,self.qtdVisualizacoes,self.qtdCurtidas,self.qtdNaoCurtidas,self.calculaMediaAvaliacao())
        return s
        
    def __repr__(self):
        s= 'Titulo: {:s} - Duracao:{} - Quantidade de Visualizacoes: {} - Quantidade de Curtidas: {} - Quantidade nao curtidas:{} - Avaliacao:{}'.format(self.titulo,self.duracao,self.qtdVisualizacoes,self.qtdCurtidas,self.qtdNaoCurtidas,self.calculaMediaAvaliacao())
        return s
        
    def calculaMediaAvaliacao(self):
        media=0
        if self.dictAvaliacao['qtNotas']==0:
            media=0
        else:
            media=self.dictAvaliacao['somaNotas']//self.dictAvaliacao['qtNotas']
        return media
    
    def exibeFilme(self):
        print("Titulo: ",self.titulo)
        print("duracao: ",self.duracao)
        print("Quantidade Visualizacoes: ",self.qtdVisualizacoes)
        print("Quandidade Curtidas: ",self.qtdCurtidas)
        print("Quandidade Nao Curtidas: ",self.qtdNaoCurtidas)
        print("Avaliacao: ",self.calculaMediaAvaliacao())
        print(" ---------")
        return
    
    def setTituloFilme(self,novo):
        self.titulo=novo
        return
    
    def setDuracaoFilme(self,novo):
        [h,m,s]=novo.split(':')
        horas=int(h)
        minutos=int(m)
        segundos=int(s)
        self.duracao.setHora(horas)
        self.duracao.setMin(minutos)
        self.duracao.setSeg(segundos)
        return
    
    def getTitulo(self):
        return self.titulo
    
    def getDuracao(self):
        return self.duracao
    
    def getQtdVisualizacao(self):
        return self.qtdVisualizacoes
    
    def getQtdCurtidas(self):
        return self.qtdCurtidas
    
    def getQtdNaoCurtidas(self):
        return self.qtdNaoCurtidas
    
    def getAvaliacao(self):
        return self.calculaMediaAvaliacao()
    
    def curtir(self):
        self.qtdCurtidas+=1
        return
    
    def naoCurtir(self):
        self.qtdNaoCurtidas+=1
        return
    
    def visualizado(self):
        self.qtdVisualizacoes+=1
        return
    
    def avaliacao(self,nota):
        self.dictAvaliacao['somaNotas']=self.dictAvaliacao['somaNotas']+nota
        self.dictAvaliacao['qtNotas']=self.dictAvaliacao['qtNotas']+1
        return