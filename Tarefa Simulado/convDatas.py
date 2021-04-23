# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

def GregorianoParaJuliano(dt):
    """
    A fórmula para conversão de qualquer data do Calendário Gregoriano(>=15/10/1582)
    em Dia Juliano 
    Se o Mês for menor do que 3, faça Ano=Ano-1 e Mês=Mês+12
    A = o inteiro de (Ano ÷ 100)
    B = o inteiro de (A ÷ 4)
    C = 2 - A + B
    Se a data for igual ou anterior a 04/10/1582 (Calendário Juliano), faça:
    C = 0
    
    Isso posto, faça:
    D = o inteiro de (365,25 x (Ano + 4716))
    E = o inteiro de (30,6001 x (Mês + 1))
    
    O DJ será = D + E + Dia +  C - 1524,5
    """
    [d,m,a]=dt.split('/')
    dia=int(d)
    mes=int(m)
    ano=int(a)
    
    if mes < 3:
        ano-=1
        mes+=12
    A=ano//100
    B=A//4
    if ano*10000 + mes*100 + dia < 15821004:
        C=0
    else:
        C=2-A+B
    D= int (365.25 * (ano + 4716))
    E =int (30.6001 * (mes + 1))
    dJul = (D + E+ dia + C  - 1524.5)
    
    return int(dJul)
    


def JulianoParaGregoriano(dJul):
    '''
    conversão de Dias Julianos em data - tem a seguinte fórmula:
    Faça:
    A = Dia Juliano (trabalharemos sempre com números inteiros, pelos mesmos motivos da observação logo acima)
    
    Se A for menor do que 2.299.161 faça:
    D = A
    
    Se A for maior do que 2.299.160 faça:
    E = o inteiro de ((A - 1.867.216,25) ÷ 36.524,25)
    D = A + 1 + E - o inteiro de (E ÷ 4)
    
    Isto posto, faça:
    F = D + 1.524
    G = o inteiro de ((F - 122,1) ÷ 365,25)
    H = o inteiro de (G x 365,25)
    I = o inteiro de ((F - H) ÷ 30,6001)
    J = F - H - o inteiro de (I x 30,6001)
    K = I - 1 (se I for menor do que 14) ou I - 13 (se I for maior do que 13)
    L = G - 4.716 (se K for maior do que 2) ou G - 4.715 (se K for menor do que 3)
    M = L (se L for maior do que 0) ou L x (-1) + 1 (se L for menor do que 1)
    
    J é o dia, K é o mês e M é o ano (d.C. se L for maior do que 0 ou a.C. se L for menor do que 1)
'''
    
    D=int(dJul)
    if D > 2299161:
        E = int((D - 1867216.25) / 36524.25)
        D = int(D + 1 + E - int(E / 4))
    F = D + 1524
    G = int ((F - 122.1) / 365.25)
    H = int(G * 365.25)
    I = int ((F - H) / 30.6001)
    J = F - H - int (I * 30.6001)

    K = I - 1 if I < 14 else I - 13 
    L = G - 4716 if  K > 2 else G - 4715 
    M = L if L>0  else -1*L + 1 
    dt= "{:0>2d}/{:0>2d}/{:0>4d}".format(J,K,M)
    if L > 0:
        return (dt,'d.C.')
    else:
        return (dt,'a.C.')
    
def diaDaSemana(dt):
    '''
    2.	Dados o  dia, mês e ano de uma data é possível calcular o dia da semana  
        desta data do seguinte modo: 
    1) a = (14 - Mes) / 12 
    2) y = Ano - a 
    3) m = Mes + 12a - 2 
    4) q = Dia + 31m/12 + y + y/4 - y/100 + y/400 
    5) d = q % 7 
    
    Sendo o dia da semana expresso do seguinte modo:
    d = 0 → domingo 
    d = 1 → segunda-feira 
    d = 2 → terça-feira 
    d = 3 → quarta-feira 
    d = 4 → quinta-feira 
    d = 5 → sexta-feira 
    d = 6 → sábado 

    '''    
    [D,M,A]=dt.split('/')
    dias=['Domingo','Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sábado']
    Dia=int(D)
    Mes=int(M)
    Ano=int(A)
   
    a = (14 - Mes) // 12 
    y = Ano - a 
    m = Mes + 12*a - 2 
    q = Dia + 31*m//12 + y + y//4 - y//100 + y//400 
    d = q % 7  
    return(dias[d])
