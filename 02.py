nome = str(input('Digite seu nome: '))
saldo = int(input('Agora digite seu saldo médio: R$'))

saldo20 = saldo * 0.20
saldo30 = saldo * 0.30
saldo40 = saldo * 0.40

if (saldo >= 0) and (saldo <= 200):
    print('{}, Saldo médio R${}, Cédito disponibilizado: Nenhum crédito.'.format(nome, saldo))
else:
    if (saldo >= 201) and (saldo <= 400):
        print('{}, Saldo médio R${}, Cédito disponibilizado: R${} (20% do valor do saldo médio)'.format(nome, saldo, saldo20))
    elif (saldo >= 401) and (saldo <= 600):
        print('{}, Saldo médio R${}, Cédito disponibilizado: R${} (30% do valor do saldo médio)'.format(nome, saldo, saldo30))
    else:
        print('{}, Saldo médio R${}, Cédito disponibilizado: R${} (40% do valor do saldo médio)'.format(nome, saldo, saldo40))
