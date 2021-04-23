#####################################################################################
#Nome completo:Luiza Del Negro Ciuffo Fernandes
#Matrícula PUC-Rio: 1721251
#Turma:33A
#Professor: Claudia Ferlin
#Declaração de autoria: Declaro que este documento foi produzido por mim em sua totalidade,
######################################################################################
import filme


class CadastroDeFilmes():
    def __init__(self):
        self.dicionario=dict()
        return
    def __eq__(self,outro):
        return(self.dicionario==outro.dicionario)
    
    def incluiNovoFilme(self,titulo,objFilme):
        self.dicionario[titulo]=objFilme
        return
    
    def exibeTodosOsFilmes(self):
        for el in self.dicionario:
            self.dicionario[el].exibeFilme()
        return
    
    def exibeFilmesComNotaMaior(self,nota):
        for el in self.dicionario:
            obj=self.dicionario[el]
            if obj.getAvaliacao()>nota:
                print(obj)
        return
    
    def encontraFilme(self, filme):
        if filme not in self.dicionario:
            print(" filme inexistente")
            return
        else:
            print(self.dicionario[filme])
            return
        
    def getFilme(self,nomeFilme):
        return self.dicionario[nomeFilme]
        