#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if(__name__ == '__main__'):
    print('* * * Máquina automática de venda * * *')
    print('* * * Carga de quantidade e preço do produto * * *')
    print('* * * Produtos disponíveis * * *')
    print('* * * Carregando a máquina * * *')
    
    #VARIABLES
    credits = 0
    soldProd = 0
    product_name = ''
    price = 0
    estoque = 0

    def setup():
        global estoque
        global price
        global product_name
        #product_name = input('Nome do produto disponível ')
        try:
            estoque = int(input('Quantidade de produtos disponíveis '))
        except ValueError as err:
            print('! ! ! Este campo aceita apenas valores numéricos ! ! ! ')
            return setup()
        try:
            price = float(input('Preço unitário '))
        except ValueError as err:
            print('! ! ! Este campo aceita apenas valores numéricos ! ! ! ')
            return setup()
        else:
            price = float("%0.2f" % (price))
            if(price*100 % 5 != 0):
                print('! ! ! Valor desejado não pode ser gerado por moedas em real ! ! !')
                return setup()

        print('* * * Existem {0} {1}s disponíveis. Cada uma por R${2} * * *'.format(estoque, product_name, price))
        print('* * * -------------------------------------------------- * * *')
        print ('* * * Digite 2 para visualizar creditos atuais * * * ')
        print ('* * * Digite 1 para adicionar creditos * * * ')
        print ('* * * Digite 0 para comprar novo produto * * * ')
        print ('* * * Digite -1 para receber troco * * * ')
        print ('* * * Digite -2 para vizualizar resumo de vendas * * * ')
        openOperations()

    

    def openOperations():
        try:
            operator = int(input('Digite o operador desejado: '))
        except ValueError as err:
            print('! ! ! Este campo aceita apenas valores numéricos. Tente novamente ! ! ! ')
            return openOperations()
        else: 
            if(operator < -2 or operator > 2):
                print('! ! ! Operador inesistente. Tente novamente ! ! !')
                return openOperations()
            if(operator == -2):
                actualProgress()
                openOperations()
            if(operator == -1):
                returnChange()
            if(operator == 0):
                buyProcuct()
            if(operator == 1):
                addCredit()
            if(operator == 2):
                print('Seu total de creditos é: ' + str(credits))
                openOperations()

    
    def actualProgress():
        global soldProd
        global price
        global estoque

        print('Produtos vendidos: ' + str(soldProd))
        print('Vendas em reais: '+ str(soldProd * price))
        print('Produtos em estoque: ' + str(estoque))

    def addCredit():
        try:
            amount = float("%0.2f" % float(input('Valor deseja creditar: ')))
        except ValueError as err:
            print('! ! ! Este campo aceita apenas valores numéricos ! ! ! ')
        else:
            if (amount < 0):
                print('! ! ! Esse operador apenas adiciona creditos. Para remoever utilize o operador -1 ! ! !')
            elif(amount*100 % 5 != 0):
                print('! ! ! Valor desejado não pode ser gerado por moedas em real ! ! !')
            else:
                global credits
                credits += amount
                print('Seu total de creditos é: ' + str(credits))
        openOperations()

    def returnChange():
        global credits
        splited = splitIntAndDecimal(credits)
        
        result = {}
        result['1'] = splited['integer']
        decimal = splited['decimal']
        result['50'] = int( decimal / 50)
        decimal = decimal % 50
        result['25'] = int(decimal / 25)
        decimal = decimal % 25
        result['10'] = int(decimal / 10)
        decimal = decimal % 10
        result['5'] = int(decimal / 5)
        decimal = decimal % 5

        print('Seu troco de ' + str(credits) + 'é composto de: ')
        print('\t'+str(result['1'])+ ' moeda(s) de 1 real')
        print('\t'+str(result['50'])+ ' moeda(s) de 50 centavos')
        print('\t'+str(result['25'])+ ' moeda(s) de 25 centavos')
        print('\t'+str(result['10'])+ ' moeda(s) de 10 centavos')
        print('\t'+str(result['5'])+ ' moeda(s) de 05 centavos')

        credits = 0
        print('Seus creditos atuais são de: ' + str(credits))

        openOperations()


    def buyProcuct():
        global soldProd
        global estoque
        global price
        global credits

        if(estoque < 1):
            print('! ! ! Os estoques dessa máquina acabaram. Finalizando processo por hoje. ! ! !')
            return endProcess()
        elif(credits < price):
            print('! ! ! Você não possui creditos suficienets para esta compra. Necessário adicionar mais para prosseguir ! ! !')
        else: 
            soldProd += 1
            estoque -= 1
            credits -= price
            print('* * * Você comprou um ' + product_name + ' com sucesso * * *')
            print('* * * Seus créditos atuáis são de: '+ str(credits) + ' * * * ')
        
        openOperations()

    def endProcess():
        actualProgress()
        return; #exit aplication

    def splitIntAndDecimal (number):
        string = str(number)
        string = string.split('.')
        integer = int(string[0])
        decimal = int(string[1])
        return {'integer': integer, 'decimal': decimal}
        
    setup()