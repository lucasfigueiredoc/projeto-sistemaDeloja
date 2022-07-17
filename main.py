from http import client
from tkinter import *
from Objetos.Clientes import Cliente


root = Tk()

root.mainloop()

def ArtMenu():{
    print("----------------------------------"),
    print("     1 : cadastro cliente         "),
    print("     2 : ver cardapio             "),
    print("     3 : fazer pedido             "),
    print("     4 : ver faturamento          "),
    print("     5 : finalizar                "),
    print("----------------------------------")
    
}

def funCase(x):
    x = input("define:  ")
    case = switch.get(x, default)
    case()
    

def function1():

    Cliente.nome = (input('Insira nome: '))
    Clientes.Cliente.cpf (input('Insira CPF: '))
    Clientes.Cliente.endereco (input('Insira endereço: '))

    funCase(x)

def function2():
    print("Case 2 selected")
    funCase(x)
    
def function3():
    print("Case 3 selected")
    funCase(x)
    
def function4():
    print("Case 4 selected")
    funCase(x)

def function5():
    print("Case 5 selected")
    funCase(x)



def default():
    print("Valor inválido, digite novamente")
    funCase(x)

if __name__ == "__main__":
    switch = {
        "1" : function1,
        "2" : function2,
        "3" : function3,
        "4" : function4,
        "5" : function5
    }
else:{
    funCase()
}

ArtMenu()



x = input("define:  ")
funCase(x)