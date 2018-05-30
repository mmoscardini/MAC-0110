#!/usr/bin/env python3

'''
    Define python3 as interpreter
    To run this script from terminal run in Unix OS: chmod +x /path/to/script 
'''

#import libraries
import math           
if (__name__ == '__main__'):
    def integralRetangle(a,b,M,fn):
        #Get the lenth of each interval to determine the factor of increase in x value
        interval_range = (b - a)/M

        #total area, wich will be the integral result
        total_area = 0
        for i in range(M):
            total_area += (fn(a + i*interval_range))*interval_range

        return total_area

    def IntegralTrapeze(a,b,M, fn):
        #Get the lenth of each interval to determine the factor of increase in x value
        interval_range = (b - a)/M

        #total area, wich will be the integral result
        total_area = 0
        for i in range(M):
            total_area += ((fn(a+i*interval_range)+fn(a+interval_range+i*interval_range)))*interval_range/2

        return total_area

    #calculate the intrisic value for the intefral of fn
    def integralIntrisic(a,b,fnName):
        return {
            'sin': math.cos(a) - math.cos(b),
            'cos': math.sin(b) - math.sin(a),
            'e': math.pow(math.e, b) - math.pow(math.e, a),
            'pol': ((3*((b**4) - (a**4))/4) + (2*((b**3) - (a**3))/3) + (((b**2) - (a**2))/2) + ((b - a)))
        }[fnName]

    def fnExponential(x):
        return math.pow(math.e, x)

    def fnPolinomial(x):
        return 3*(x**3) + 2*(x**2) + x + 1

    #funciton used to calculate the error the calculated functions had
    def calculateError(intrisic, calculated):
        return module((intrisic - calculated)*100/calculated)

    def module(x):
        if(x >= 0): return x
        else: return -1*x


    def printResults(fnName, method, result, err):
        '''
            function created to print results sistematicly 
            Expects as params: 
                the name of the function
                the method user to calculate the result
                the result
                difference between intrisic funciton and the calculated resultd
        '''
        print('{:<50} {:.10f}'.format(('Integral do %s pelo método %s:'%(fnName, method)), result))
        if(err):
            if(err < 0):
                print('{:<49} {:.10f}%'.format(('Erro %s pelo método %s:'%(fnName, method)), err))
            else:
                print('{:<50} {:.10f}%'.format(('Erro %s pelo método %s:'%(fnName, method)), err))

    def main():
        try:
            a = int(input('Entre com o limite inferior do intervalo: '))
            b = int(input('Entre com o limite superior do intervalo: '))
            m = int(input('Entre com a quantidade de sub-intervalos: '))
        except ValueError:
            print('! ! ! Ops! Você deve digitar apenas números inteiros. Tente novamente...  \n')
            return main()

        #Handle wrong inputs
        if(a > b):
            print('! ! ! Você entrou um intervalo superior menor que o inferior. Tente novamente... \n')
            return main()
        if(m < 0):
            print('! ! ! A quantidade de subintervalos deve ser maior do que zero. Tente novamente... \n')
            return main() 

        
        print() #print empty line
        intrinsic_sin = integralIntrisic(a,b, 'sin')
        ret_sin = integralRetangle(a,b,m, math.sin)
        trap_sin = IntegralTrapeze(a,b,m,math.sin)
        ret_sin_err = calculateError(intrinsic_sin, ret_sin)
        trap_sin_err = calculateError(intrinsic_sin, trap_sin)
        printResults('Seno', 'Intrinsico', intrinsic_sin, None)
        printResults('Seno', 'Retangulos', ret_sin, ret_sin_err)
        printResults('Seno', 'Trapézio', trap_sin, trap_sin_err)
        print('------------------------------------------------------------------')
        intrinsic_cos = integralIntrisic(a,b, 'cos')
        ret_cos = integralRetangle(a,b,m, math.cos)
        trap_cos = IntegralTrapeze(a,b,m, math.cos)
        ret_cos_err = calculateError(intrinsic_cos, ret_cos)
        trap_cos_err = calculateError(intrinsic_cos, trap_cos)
        printResults('Cosseno', 'Intrinsico', intrinsic_cos, None)
        printResults('Cosseno', 'Retangulos', ret_cos, ret_cos_err)
        printResults('Cosseno', 'Trapézio', trap_cos, trap_cos_err)
        print('------------------------------------------------------------------')
        intrinsic_e = integralIntrisic(a,b, 'e')
        ret_e = integralRetangle(a,b,m, fnExponential)
        trap_e = IntegralTrapeze(a,b,m, fnExponential)
        ret_e_err = calculateError(intrinsic_e, ret_e)
        trap_e_err = calculateError(intrinsic_e, trap_e)
        printResults('Exponencial', 'Intrinsico', intrinsic_e, None)
        printResults('Exponencial', 'Retangulos', ret_e, ret_e_err)
        printResults('Exponencial', 'Trapézio', trap_e, trap_e_err)
        print('------------------------------------------------------------------')
        intrinsic_pol = integralIntrisic(a,b, 'pol')
        ret_pol = integralRetangle(a,b,m, fnPolinomial)
        trap_pol = IntegralTrapeze(a,b,m, fnPolinomial)
        ret_pol_err = calculateError(intrinsic_pol, ret_pol)
        trap_pol_err = calculateError(intrinsic_pol, trap_pol)
        printResults('Polinômio', 'Intrinsico', intrinsic_pol, None)
        printResults('Polinômio', 'Retangulos', ret_pol, ret_pol_err)
        printResults('Polinômio', 'Trapézio', trap_pol, trap_pol_err)
        print() #print empty line

        #loop to keep asking if user want to continue or not
        i = True
        while(i):
            repeat = (input('Deseja calcular novamente? (s/n)'))
            if(repeat == 's'):
                print() #print empty line
                main() #call function recursivly, so it can keep running in loop
            elif(repeat == 'n'):
                print('*** Finalizando programa *** \n')
                i = False
                return #exit function and finish program
            else:
                print('! ! ! Comando não aceito. Tente novamente')
    
    #Start the program
    main()