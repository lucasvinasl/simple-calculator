import os

print("\n******************* Calculadora em Python *******************")

def calSOMA(num1,num2):
    return num1 + num2

def calSUB(num1,num2):
    return num1 - num2

def calPROD(num1,num2):
    return num1 * num2

def calDIV(num1,num2): 
    return num1/num2

parada = 0
while parada == 0:
    
    print("Operações possíveis: ")
    print("1 - SOMA")
    print("2 - SUBTRAÇÃO")
    print("3 - PRODUTO")
    print("4 - DIVISÃO")
    
    operacao = int(input("Selecione a operação desejada 1/2/3/4: "))
           
    
    if operacao == 1:
        x = float(input("Informe o primeiro número: "))
        y = float(input("Informe o segundo número: "))
        print("%.2f + %.2f = %.2f" %(x,y,calSOMA(x,y)))
        
    elif operacao == 2:
        x = float(input("Informe o primeiro número: "))
        y = float(input("Informe o segundo número: "))
        print("%.2f - %.2f = %.2f" %(x,y,calSUB(x,y)))
        
    elif operacao == 3:
        x = float(input("Informe o primeiro número: "))
        y = float(input("Informe o segundo número: "))
        print("%.2f * %.2f = %.2f" %(x,y,calPROD(x,y)))
                                                  
    elif operacao == 4:
        while True:
            try:
                x = float(input("Informe o primeiro número: "))
                y = float(input("Informe o segundo número: "))
                
                if y == 0:
                    raise ZeroDivisionError("Erro: Denominador não pode ser ZERO. Tente novamente! \n")
                    
                print("%.2f / %.2f = %.2f" %(x,y,calDIV(x,y)))
                break
                
            except ZeroDivisionError as error:
                print(error)
                continue
                    
    else:
        print("informe uma operação válida")
    
    parada += int(input("Deseja fazer outra operação? 0 - SIM / 1 - NÃO: \n"))
    
    os.system("cls")

print("Obrigado e volte sempre \n")