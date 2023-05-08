matri = input('Matrícula: ')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
me_ex = float(input('Média Exercícios Escolares: '))

me_apr = ((nota1 + (nota2 * 2) + (nota3 * 3) + me_ex) / 7)

if (me_apr >= 9.0):
    print('Média de Aproveitamento = {}, Conceito: A, APROVADO.'.format(me_apr))
elif (me_apr >= 7.5) and (me_apr < 9.0):
        print('Média de Aproveitamento = {}, Conceito: B, APROVADO.'.format(me_apr))
else:
    if (me_apr >= 6.0) and (me_apr < 7.5):
            print('Média de Aproveitamento = {}, Conceito: C, APROVADO.'.format(me_apr))
    elif (me_apr >= 4.0) and (me_apr < 6.0):
            print('Média de Aproveitamento = {}, Conceito: D, REPROVADO.'.format(me_apr))
    else:
        print('Média de Aproveitamento = {}, Conceito: E, REPROVADO.'.format(me_apr))


        
