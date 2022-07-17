from email.errors import ObsoleteHeaderDefect
from http import client
from tkinter import *
from Objetos.Clientes import Cliente

##root = Tk()



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
            return Cliente.nome(input('test '))

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
