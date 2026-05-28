#calculadora 

print("===================")
print("   CALCULADORA")
print("===================")

#escolher a operacao
operacao = input("Qual operacao sera feita: \n 1 - Soma. \n 2 - Subtracao \n 3 - Bhaskara \n 4 - Hipotenusa ")

#soma
if operacao == "1":
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero: "))
    soma = n1 + n2
    print("A soma entre", n1, " e", n2, "e: ", soma)

#subtracao
if operacao == "2":
    n1 = float(input("Digite o primeiro numero"))
    n2 = float(input("Digite o segundo numero"))
    subtracao = n1 - n2
    print("A subtracao entre", n1, " e", n2, "e: ", subtracao)

#bhaskara
if operacao == "3":
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c

    x1 = (-b + delta**(1/2))/(2*a)
    x2 = (-b - delta**(1/2))/(2*a)

    print("O valor de delta e: ", delta)
    print("O valor de x1: ", x1)
    print("O valor de x2: ", x2)

#hipotenusa
if operacao == "4":
    c1 = float(input("Digite o valor do primeiro cateto: "))
    c2 = float(input("Digite o valor do segundo cateto: "))

    h = ((c1)**2 + (c2)**2)**(1/2)

    print("O valor da hipotenusa e: ", h)