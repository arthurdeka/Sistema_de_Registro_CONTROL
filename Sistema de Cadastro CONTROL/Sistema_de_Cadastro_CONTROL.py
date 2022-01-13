import os                  #importa biblioteca de limpeza do terminal
import random              #importa biblioteca para gerar números aleatórios

#Declaração da lista que vai armazenar os dados das pessoas registradas
ListaRegistros = []

#Definindo a classe para organização dos dados dos cadastrados
class Cadastro:
    #método construtor (forma de definir os parâmetros do objeto criado com a classe)
    def __init__(self, nome, idade, caracteristica, ID):  #self serve para indicar quais serão os parâmetros utilizados pelo objeto
        self.nome = nome
        self.idade = idade
        self.caracteristica = caracteristica
        self.ID = ID
        
    #definição de métodos SET (para inserir ou alterar valores nos parâmetros do objeto)
    def setNome(self, nome):
        self.nome = nome
    def setIdade(self, idade):
        self.idade = idade
    def setCaracteristia(self, caracteristica):
        self.caracteristica = caracteristica
    def setID(self, ID):
        self.ID = ID
        
    #definição de métodos GET (para ler os valores armazenados nos parâmetros do objeto)
    def getNome(self):
        return self.nome
    def getIdade(self):
        return self.idade
    def getCaracteristica(self):
        return self.caracteristica
    def getID (self):
        return self.ID
    
#definição do comando de limpar a tela
def limpar():
    os.system('cls')

#definição da variável para contagem de número de registros
RegistrosQuantidade = 0

#definição da variável para a escolha de opção:
escolha = 0

#definindo o Menu Principal
def menu():
    limpar()
    print("Bem-Vindo ao Sistema CONTROL")
    print()
    print()
    print("1 - Cadastrar uma pessoa")
    print("2 - Ver todos os cadastros")
    print("3 - Excluir um cadastro")
    print("4 - Ver a quantidade de cadastros")
    print("5 - EXTRAS")
    print()
    print("9 - Sair do SISTEMA CONTROL")
    escolha = int(input("Qual opção você deseja escolher? \n"))
    if escolha == 1:
        CadastrarPessoa()
    if escolha == 2:
        VerCadastros()
    if escolha == 3:
        ExcluirCadastro()
    if escolha == 4:
        QuantCadastros()
    if escolha == 5:
        extras()
    if escolha == 9:
        return 0
    
#definindo a função de cadastrar uma pessoa
def CadastrarPessoa():
    limpar()
    print("Bem vindo ao cadastro do sistema CONTROL")
    print()
    nome = input("Qual o nome da pessoa a ser cadastrada?\n")
    idade = input("Qual a idade da pessoa?\n")
    caracteristica = input("Cite uma caracteristica dessa pessoa\n")
    ID = random.randint(100,999)
    pessoa = Cadastro(nome, idade, caracteristica, ID) #Cria um objeto com as propriedades da classe Cadastro
    ListaRegistros.append(pessoa)   #manda o objeto criado para o fim da lista "ListaRegistros" 
    print()
    print("Cadastro realizado com sucesso!")
    input("pressione enter para voltar ao Menu CONTROL")
    menu()

#definindo a função de ver os cadastros
def VerCadastros():
    limpar()
    if len(ListaRegistros) == 0:
        print("Não existem cadastros ainda!")
        print()
        input("Pressione enter para voltar ao Menu CONTROL")
        menu()
    else:
        for i in range(len(ListaRegistros)):
            print("Nome:", ListaRegistros[i].nome,'| Idade:', ListaRegistros[i].idade,'| Caracteristica:', ListaRegistros[i].caracteristica,'| ID:',ListaRegistros[i].ID,"\n")
        print("\n Esses foram todos os atuais cadastros do sistema CONTROL!")
        input("Pressione Enter para voltar ao Menu")
        menu()

#definindo a função de excluir um cadastro
def ExcluirCadastro():
    limpar()
    ID = int(input("Digite o ID do cadastro que deseja excluir \n"))
    for i in range(len(ListaRegistros)):
        if ListaRegistros[i].ID == ID:
            ListaRegistros.pop(i)
            print("Pessoa excluída com sucesso!")
            break
    input("Pressione enter para voltar ao Menu CONTROL")
    menu() 
   
#definindo a função de ver a quantidade de cadastros
def QuantCadastros():
    limpar()
    print("No momento existem:", len(ListaRegistros), "Cadastros \n")
    input("Pressione enter para voltar ao Menu CONTROL")
    menu()

#definindo a função de ver conteúdo extra
def extras():
    limpar()
    print("SISTEMA DE REGISTRO CONTROL - v1.0 \n")
    print("Criado por Arthur DK")
    print("Com ajuda de Hugo Barbosa")
    print()
    print("valeu, hugo! :)")
    print()
    print()
    print()
    input("Pressione enter para voltar ao Menu CONTROL")
    menu()
    
menu()