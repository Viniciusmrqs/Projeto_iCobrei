#Script enviar mensagem pronta para devedor

#print ('### INSIRA OS DADOS DO CLIENTE ABAIXO ###')

print ('INFORMAÇÕES PESSOAIS') #Formulário que coleta dados pessoais do devedor.
print ('Nome completo: ')
nome = input()
print ('CPF')
cpf_dev = input()
print ('RG', '(apenas numeros)')
rg_dev = input()

print ('INFORMAÇÕES DE ENDEREÇO') #Formulário que coleta dados de endereço do devedor.
print ('Rua')
end_rua = input()
print ('Número')
end_num = input()
print ('Bairro')
end_bairro = input()
print ('Cidade')
end_cid = input()
print ('CEP')
cep = input()

print ('INFORMAÇÕES DE CONTATO') #Formulário que coleta dados de contato do devedor
print ('Telefone fixo')
tel_fix_dev = input()
print ('Celular 1')
cel_1_dev = input()
print ('Celular 2')
cel_2_dev = input()
print ('Email')
email_dev = input()

print ('DADOS DA DÍVIDA') #Formulario que coleta informações da Dívida
print ('Nome do Credor')
nome_cred = input()
print ('CNPJ')
cnpj = input()
print ('Descrição da dívida')
desc = input()
print ('Valor', '(não é preciso inserir R$)')

valor = float #Converte tipo de entrada de str para float/int
parc = int

valor = input()
print ('Parcelas')
parc = input()

def


#msg = 'olá,',nome, somos, consta, valor, com, nome_cred, portadora, cnpj,referente, desc, oferecemos, parc,'X de R$', v_final


print (('https://api.whatsapp.com/send?phone=55{}&text=Ola%20{}!%20Somos%20aplataforma%20de%20cobranca%20iCobrei!'
        '%20Estamos%20aqui%20para%20lhe%20oferecer%20condicoes%20mais%20flexiveis%20para%20quitar%20sua%20divida.'
        'Voce%20tem%20um%20crediario%20em%20aberto%20no%20valor%20de%20R$%20{}.%20Referente%20a%20{}%20no%20estabelecimento:%20{}').format(cel_1_dev, nome,valor, desc,nome_cred ))


