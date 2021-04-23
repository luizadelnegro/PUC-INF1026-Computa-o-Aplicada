#####################################################################################
#Nome completo:Luiza Del Negro Ciuffo Fernandes
#Matrícula PUC-Rio: 1721251
#Turma:33A
#Professor: Claudia Ferlin
#Declaração de autoria: Declaro que este documento foi produzido por mim em sua totalidade,
######################################################################################

import pessoa
import filme
import cadastroDeFilmes
import assistirFilmes

print('Primeiro telespectador:')
luiza=pessoa.Pessoa("Luiza","luiza@email.com","abc123","07/06/1994")
luiza.exibePessoa()
luiza.setEmail("aziul@email.com")
luiza.setSenha("123abc")
print('Primeiro telespectador com alterações:')
luiza.exibePessoa()
print('Segundo telespectador:')
luiz=pessoa.Pessoa("Luiz","luiz@email.com","abc123")
luiz.exibePessoa()
luiz.setAniversario("02/02/2002")
print('Segundo telespectador com alterações:')
luiz.exibePessoa()
print(" ******************************************************* ")

cadFilmes=cadastroDeFilmes.CadastroDeFilmes()

dOscar2021= {
 'Mulan': {'Duracao': 115, 'Plataforma': 'Disney Plus'}, 
 "Pinóquio": {'Duracao': 125, 'Plataforma':'não disponível'},
 'Soul': {'Duracao': 107, 'Plataforma': 'Disney Plus'},
 'Meu pai': {'Duracao': 97, 'Plataforma': 'Now'},
 'Os 7 de Chicago': {'Duracao': 130, 'Plataforma': 'Netflix'},
 'O som do silêncio': {'Duracao': 130, 'Plataforma': 'Amazon Prime'},
 'Bela vingança': {'Duracao': 114, 'Plataforma': 'não disponível'},
 'Nomadland': {'Duracao': 110, 'Plataforma': 'não disponível'},
 'Minari': {'Duracao': 116, 'Plataforma': 'não disponível'},
 'Mank': {'Duracao': 131, 'Plataforma': 'Netflix'},
 'Judas e o messias negro': {'Duracao': 126, 'Plataforma': 'não disponível'}
}

for el in dOscar2021:
    movie=filme.Filme(el, dOscar2021[el]['Duracao'])
    cadFilmes.incluiNovoFilme(movie.getTitulo(), movie)
print("Cadastro de filmes criado")
cadFilmes.exibeTodosOsFilmes()

obj1=assistirFilmes.AssistirFilmes(luiza, cadFilmes.getFilme('Mulan'))
obj1.avaliaFilme(10,'Mulan')
obj1.like()
obj2=assistirFilmes.AssistirFilmes(luiza, cadFilmes.getFilme('Soul'))
obj2.avaliaFilme(7,'Soul')
obj2.like()
obj3=assistirFilmes.AssistirFilmes(luiza, cadFilmes.getFilme('Mank'))
obj3.avaliaFilme(6,'Mank')
obj3.like()
obj4=assistirFilmes.AssistirFilmes(luiz, cadFilmes.getFilme('Soul'))
obj4.avaliaFilme(5,'Soul')
obj4.unlike()
obj5=assistirFilmes.AssistirFilmes(luiz, cadFilmes.getFilme('Judas e o messias negro'))
obj6=assistirFilmes.AssistirFilmes(luiz, cadFilmes.getFilme('O som do silêncio'))
print(" ******************************************************* ")
print("Cadastro de filmes depois das mudanças")
cadFilmes.exibeTodosOsFilmes()
print(" ******************************************************* ")
print("Tarefa Validacao")
print(luiza)
print(luiz)
