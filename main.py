from email.errors import ObsoleteHeaderDefect
from http import client
from tkinter import *
from Objetos.Clientes import Cliente

##root = Tk()

def clienteAdd(clientAd[y]):
    for i in clienteAd:
        print('Cadastrando Cliente, adicione os dados respectivamente: \n')
        clientAd[i] = Cliente(input('Nome: '), input('CPF: '), input('Endereço completo: '))



y=10

clienteAd = [y]

def ArtMenu():{
    print("----------------------------------"),
    print("     1 : cadastro cliente         "),
    print("     2 : ver cardapio             "),
    print("     3 : fazer pedido             "),
    print("     4 : ver faturamento          "),
    print("     5 : finalizar                "),
    print("----------------------------------")
    
}
##root.mainloop()

def operacao(x):
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
        
        case _:
            return print('Valor inválido, retorne!'), operacao(input('Define '))
            
ArtMenu()

operacao(input('Define '))
