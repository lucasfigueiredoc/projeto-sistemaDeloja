# from email.errors import ObsoleteHeaderDefect
# from http import client
# from tkinter import *
# Imports não necessários (pelo menos atualmente)


from bd.connectBD import connect
from os import system
from Objetos.Clientes import Cliente



# Criamos uma lista vazia
listaClientes = list()


def clienteAdd():
    print('Cadastrando Cliente, adicione os dados respectivamente: \n')

    # Adicionamos um item a nossa lista, neste caso, o objeto
    # cliente, através do método "append"

    listaClientes.append(
        Cliente(input('Nome: '), input('CPF: '), input('Endereço completo: ')))

    # Limpar a tela antes de concluir
    system("clear")
    print("Cliente cadastrado com sucesso!")

def ArtMenu():
    system("clear")
    print("----------------------------------")
    print("     1 : cadastro cliente         ")
    print("     2 : mostrar clientes         ")
    print("     3 : ver cardapio             ")
    print("     4 : fazer pedido             ")
    print("     5 : ver faturamento          ")
    print("     6 : finalizar                ")
    print("----------------------------------")
    

##root.mainloop()

def operacao(x):
    # Aqui, limpamos a tela antes de qualquer outra
    # operação
    system("clear")

    match x:
        case '1':
            return clienteAdd()

        case '2':
            return print("Case 2 selected")
    
        case '3':
            return print("Case 3 selected")
    
        case '4':
            return print("Case 4 selected")
    
        case '5':
            return print('Case 5')

        case '6':
            exit()
        
        case _:
            return print('Valor inválido, retorne!')

while True:   
    ArtMenu()
    operacao(input('Define: '))

    # Toda vez que uma "operação" terminar,
    # serão exibidos os textos abaixo

    print("----------------------------------")
    input("Pressione ENTER para continuar...")