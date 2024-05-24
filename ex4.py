def menuPrincipal():
  global id_global
  opcao = 0
  while (opcao < 1 or opcao > 4): #enquanto o usuário não digitar uma das 4 opções, o menu persiste
    print("------------------------------------------------")
    print("---------------- MENU PRINCIPAL ----------------")
    print("Escolha a opção desejada: ")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro")
    print("3 - Remover Livro")
    print("4 - Encerrar Programa")
    opcao = int(input())
    
    if(opcao < 1 or opcao > 4):
      print("Opção inválida")
    elif(opcao == 1):
      id_global += 1
      cadastrar_livro(id_global)
    elif(opcao == 2):
      consultar_livro()
    elif(opcao == 3):
      remover_livro()
    else:
      print("Encerrando programa...") 

def cadastrar_livro(id):
    global lista_livro
    
    print("Id do livro: " + str(id))
    nome_livro = input("Por favor entre com o nome do livro: ")
    autor_livro = input("Por favor entre com o autor do livro: ")
    editora_livro = input("Por favor entre com a editora do livro: ")
    
    livro = {
      'id': id,
      'nome_livro': nome_livro,
      'autor_livro': autor_livro,
      'editora_livro': editora_livro,
    }
    
    lista_livro.append(livro)
    menuPrincipal()

def consultar_livro():  
  global lista_livro
  
  opcao = 0
  while (opcao < 1 or opcao > 4): #enquanto o usuário não digitar uma das 4 opções, o menu persiste
    print("------------------------------------------------")
    print("---------------- MENU CONSULTAR LIVRO ----------------")
    print("Escolha a opção desejada: ")
    print("1 - Consultar todos os Livros")
    print("2 - Consultar Livro por id")
    print("3 - Consultar Livro(s) por autor")
    print("4 - Retornar")
    opcao = int(input())
    
    if(opcao < 1 or opcao > 4):
      print("Opção inválida")
      
    elif(opcao == 1):
      if (len(lista_livro) == 0):
        print("Não há livros cadastrados")
      else:
        print("----------------------")
        for livro in lista_livro:
          exibeLivro(livro)
        print("----------------------")
      opcao = 0
        
    elif(opcao == 2):
      id = int(input("Digite o id do livro: "))
      livro = next((livro for livro in lista_livro if livro['id'] == id), None) #Procura na lista algum livro pelo ID informado, caso não encontra, retorna None
      if (livro == None):
        print("Livro não encontrado")
      else:
        print("----------------------")
        exibeLivro(livro)
        print("----------------------")
      opcao = 0
        
    elif(opcao == 3):
      autor = input("Digite o autor do livro: ")
      livros = [livro for livro in lista_livro if livro['autor_livro'] == autor] #Cria uma lista de livros baseada nos autores da lista original
      if (len(livros) == 0):
        print("Livro não encontrado")
      else:
        print("----------------------")
        for livro in livros:
          exibeLivro(livro)
        print("----------------------")
      opcao = 0
    else:
      menuPrincipal()

def remover_livro():
  global lista_livro
  
  print("------------------------------------------------")
  print("---------------- MENU REMOVER LIVRO ----------------")
  id = int(input("Digite o id do livro a ser removido: "))
  
  livro = next((livro for livro in lista_livro if livro['id'] == id), None)
  if (livro == None):
    print("Id inválido")
    remover_livro()
  else:
    lista_livro.remove(livro)
    print("Livro removido com sucesso")
    menuPrincipal()

def exibeLivro(livro):
  print("Id: " + str(livro['id']))
  print("Nome: " + livro['nome_livro'])
  print("Autor: " + livro['autor_livro'])
  print("Editora: " + livro['editora_livro'])
  print("\n")

id_global = 0 #ID que será usado para cadastrar livros
lista_livro = [] #Lista que serão adicionados os livros pelo usuário
def main():
  print("Bem-vindo a Livraria da Ana Paula")
  menuPrincipal()
  
main()