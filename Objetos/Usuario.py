# uma função dentro de uma classe é metodo
# se tem uma variavel ela é um atributo


class Usuario:
    
    cargo = 'usuario'
    def __init__(self, nome, idade, altura) :
       # self.nome = nome
       # self.idade = idade
        self.altura = altura
        
        
def retorna_altura(self):
    print(self.altura)
    
    
    
def exibe_cargo(cls):
    print(cls.cargo)       
        
        
usuario1 = Usuario('Lucas','21','180')
usuario2 = Usuario('Cindy','32','173')


usuario1.retorna_altura()
usuario1.exibe_cargo