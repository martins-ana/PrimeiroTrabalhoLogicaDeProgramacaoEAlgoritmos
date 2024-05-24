print("Bem-vindo a Copiadora da Ana Paula")
servico = ""
paginas = 0
servico_extra = 3

def escolha_servico(): #Recebe o tipo do serviço desejado pelo cliente e retorna seu valor
  global servico
  while (servico != "DIG" and servico != "ICO" and servico != "IPB" and servico != "FOT"):  
    print("\nEntre com o tipo de serviço desejado:")
    print("DIG - Digitalização")
    print("ICO - Impressão Colorida")
    print("IPB - Impressão Preto e Branco")
    print("FOT - Fotocópia")
    servico = input().upper() #Transformamos a string em MAIUSCULA para diminuir verificações
    
    if (servico == "DIG"):
      return 1.10
    elif (servico == "ICO"):
      return 1
    elif (servico == "IPB"):
      return 0.40
    elif (servico == "FOT"):
      return 0.20
    else:
      print("Escolha inválida, entre com o tipo do serviço novamente.")
      
def num_pagina(): #Recebe o numero de paginas e retorna a porcentagem de desconto
  global paginas
  while (paginas <= 0 or paginas >= 20000):  
    paginas = int(input("Entre com o número de páginas: "))
    
    if (paginas >= 20000):
      print("Não aceitamos tantas páginas de uma vez.")
      print("Por favor, entre com o número de páginas novamente.\n")
    elif (paginas >= 2000):
      return calcula_desconto(paginas, 25)
    elif (paginas >= 200):
      return calcula_desconto(paginas, 20)
    elif (paginas >= 20):
      return calcula_desconto(paginas, 15)
    elif (paginas > 0):
      return paginas
    else:
      print("Por favor, selecione pelo menos uma página.")

      
def servico_extra(): #Recebe o tipo do serviço extra desejado pelo cliente e retorna seu valor
  global servico_extra
  while (servico_extra != 0 and servico_extra != 1 and servico_extra != 2):  
    print("\nDeseja adicionar algum serviço? ")
    print("1 - Encadernação Simples - R$ 15.00")
    print("2 - Encadernação Capa Dura - R$ 40.00")
    print("0 - Não desejo mais nada")
    servico_extra = int(input())
    
    if (servico_extra == 0):
      return 0
    elif (servico_extra == 1):
      return 15
    elif (servico_extra == 2):
      return 40
    else:
      print("Escolha inválida, entre com o serviço extra novamente.")

def calcula_desconto(paginas, porcentagem):
  return paginas - (paginas * (porcentagem / 100))     

def main():
  valorServico = escolha_servico()
  numPagina = num_pagina()
  valorServicoExtra = servico_extra()
  
  valorTotal = (valorServico * numPagina) + valorServicoExtra
  
  print("Total: R$ %.2f (serviço: R$ %.2f * páginas: %i + extra: R$ R$ %.2f)" % (valorTotal, valorServico, numPagina, valorServicoExtra))

main()