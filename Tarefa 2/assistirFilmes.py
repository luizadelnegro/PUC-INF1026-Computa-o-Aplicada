#####################################################################################
#Nome completo:Luiza Del Negro Ciuffo Fernandes
#Matrícula PUC-Rio: 1721251
#Turma:33A
#Professor: Claudia Ferlin
#Declaração de autoria: Declaro que este documento foi produzido por mim em sua totalidade,
######################################################################################
import pessoa
import filme

class AssistirFilmes():
    def __init__(self, pessoa, filme):
        self.pessoa=pessoa
        self.filme=filme
        self.filme.visualizado()
        return
    
    def __str__(self):
        s='Espectador: {}'.format(self.pessoa,self.filme)
        return s
    def __repr__(self):
        s='Espectador: {}'.format(self.pessoa,self.filme)
        return s
    def getPessoa(self):
        return self.pessoa
    
    def getFilme(self):
        return self.filme
    
    def avaliaFilme(self,nota,nomeFilme):
        self.filme.avaliacao(nota)
        
        self.pessoa.filmesAssistidos.append(nomeFilme)
        return
    
    def like(self):
        self.filme.curtir()
        return
    
    def unlike(self):
        self.filme.naoCurtir()
        return