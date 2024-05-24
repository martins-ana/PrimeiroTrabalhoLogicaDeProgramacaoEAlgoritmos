print("Bem-vindo a Loja de Gelados da Ana Paula")
print("--------------------Cardápio--------------------")
print("------------------------------------------------")
print("---| Tamanho |  Cupuaçu (CP)  |  Açaí (AC)  |---")
print("---|    P    |    R$ 9.00     |   R$ 11.00  |---")
print("---|    M    |    R$ 14.00    |   R$ 16.00  |---")
print("---|    G    |    R$ 18.00    |   R$ 20.00  |---")
print("------------------------------------------------")

valorTotal = 0 #Variável acumuladora do valor do pedido
desejaContinuar = "S" #Enquanto for S, continuamos fazendo novos pedidos

while (desejaContinuar == "S"):
  sabor = "" #limpamos o sabor e tamanho para realizar novo pedido
  tamanho = ""
  while (sabor != "CP" and sabor != "AC"):
    sabor = input("Entre com o sabor desejado (CP/AC): ").upper() #transformamos o sabor em MAISUCULA para diminuir verificações
    if (sabor != "CP" and sabor != "AC"):
      print("Sabor inválido. Tente novamente. \n")
  
  while (tamanho != "P" and tamanho != "M" and tamanho != "G"):
    tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper() #transformamos o tamanho em MAISUCULA para diminuir verificações
    if (tamanho != "P" and tamanho != "M" and tamanho != "G"):
      print("Tamanho inválido. Tente novamente. \n")
    
  if (sabor == "CP" and tamanho == "P"):
    print("Você pediu um Cupuaçu no tamanho P: R$ 9.00")
    valorTotal = valorTotal + 9
  elif (sabor == "CP" and tamanho == "M"):
    print("Você pediu um Cupuaçu no tamanho M: R$ 14.00")
    valorTotal = valorTotal + 14
  elif (sabor == "CP" and tamanho == "G"):
    print("Você pediu um Cupuaçu no tamanho G: R$ 18.00")
    valorTotal = valorTotal + 18
  elif (sabor == "AC" and tamanho == "P"):
    print("Você pediu um Açaí no tamanho P: R$ 11.00")
    valorTotal = valorTotal + 11
  elif (sabor == "AC" and tamanho == "M"):
    print("Você pediu um Açaí no tamanho M: R$ 16.00")
    valorTotal = valorTotal + 16
  else:
    print("Você pediu um Açaí no tamanho G: R$ 20.00")
    valorTotal = valorTotal + 20
      
  desejaContinuar = input("\nDeseja mais alguma coisa? (S/N): ").upper()

print("\nO valor total a ser pago: R$ %.2f" % valorTotal)