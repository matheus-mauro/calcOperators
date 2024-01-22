import operator

continua = True

dict_operadores = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv

}

while continua:

    valor1 = int(input('Digite o primeiro valor: '))
    operacao = (input('Digite a operação: '))
    valor2 = int(input('Digite o segundo valor: '))


    resultado = dict_operadores[operacao](valor1,valor2)

    print('O Resultado é:', resultado)
    continua = (input('Deseja fazer outro calculo? '))
    if continua == 'Não':
        break