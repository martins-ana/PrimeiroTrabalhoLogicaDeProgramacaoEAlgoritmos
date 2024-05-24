print("Bem-vindo a Loja da Ana Paula")

desconto = 0 #Refere à porcentagem
valor = float(input("Entre com o valor do produto: R$")) #Recebe o valor inserido pelo usuario e transforma em float
quantidade = int(input("Entre com a quantidade do produto: ")) #Recebe a quantidade inserida pelo usuario e transforma em int

valorSemDesconto = valor * quantidade

if (valorSemDesconto >= 10000): #Se o valor for maior ou igual a 10000, aplicamos 11% de desconto.
  desconto = 11
elif (valorSemDesconto >= 6000): #Se o valor for maior ou igual a 6000, aplicamos 7% de desconto.
  desconto = 7
elif (valorSemDesconto >= 2500): #Se o valor for maior ou igual a 2500, aplicamos 4% de desconto.
  desconto = 4
else: #Se não, aplicamos 0% de desconto.
  desconto = 0
  
valorDoDesconto = valorSemDesconto * (desconto / 100)
valorComDesconto = valorSemDesconto - valorDoDesconto
  
print("Porcentagem de desconto: " + str(desconto))
print("O valor SEM desconto: " + str(valorSemDesconto))
print("O valor DO desconto: " + str(valorDoDesconto))
print("O valor COM desconto: " + str(valorComDesconto))