#validador de CPF. verifica se contem os 11 digitos, e faz a analise matematica para validar os dois ultimos digitos. 
#Se preencher com menos digitos, ele solicita um novo preenchimento, se estiver correto, ele retorna que está valido.

#Você pode adaptar esse código a sua necessidade. Resolvi criar esse codigo dessa forma para meu projeto, mas, construi ele dessa forma para evitar problemas recorrentes que já enfrentei tentando importar módulos prontos. 


def recebe_cpf():
    cpf = str(input('\033[1;33;1mDigite o CPF: '))  # recebe o cpf
    while int(cpf[0]) == 0:
        return print('CPF em branco')
    while len(cpf)!=11: #verifica se o CPF contem 11 digitos
        return print('\033[1;031;1mO CPF é composto por 11 digitos'),recebe_cpf()#solicita novamente o CPF em caso de preenchimento errado


    cpf1 = (cpf[0:3])#fatia a str CPF em grupos
    cpf2 = (cpf[3:6])#fatia a str o CPF em grupos
    cpf3 = (cpf[6:9])#fatia a str o CPF em grupos
    cpf4 = (cpf[9:11])#fatia a str o CPF em grupos
    cpf_format=('{}.{}.{}-{}'.format(cpf1,cpf2,cpf3,cpf4)) #Formata o CPF com a pontuação usual
    p1 = int (cpf[0])#Relaciona a posição da srt com o seu equivalente inteiro
    p2 = int(cpf[1])
    p3 = int(cpf[2])
    p4 = int(cpf[3])
    p5 = int(cpf[4])
    p6 = int(cpf[5])
    p7 = int(cpf[6])
    p8 = int(cpf[7])
    p9 = int(cpf[8])
    p10 = int(cpf[9])
    p11 = int(cpf[10])#Relaciona a posição da srt com o seu equivalente inteiro
    vp1 = ( p1*10+p2*9+p3*8+p4*7+p5*6+p6*5+p7*4+p8*3+p9*2)  # Expressão numerica que valida primeiro o digito verificador do cpf
    vp2 = (p1*11+p2*10+p3*9+p4*8+p5*7+p6*6+p7*5+p8*4+p9*3+p10*2)  # Expressão numerica que valida o segundo digito verificador do cpf
    r1 = (vp1 * 10)
    r2 = (vp2 * 10)
    div = (11)
    v1 = (r1 % div) #Registra o valor do resto da divisão
    v2 = (r2 % div) #Registra o valor do resto da divisão

    while v1 != p10:
        return print('\033[1;031;1mCPF inválido'), recebe_cpf()
    while v2 != p11:
        return print('\033[1;031;1mCPF inválido'), recebe_cpf()
