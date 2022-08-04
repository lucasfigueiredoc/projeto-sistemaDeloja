class Usuario:
    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        

    def retornaNomeeIdade(self):
        print(f'{self.nome} e sua idade é: {self.idade} ')
        
        
        
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} esta comendo, não pode falar')
            return
        print(f'{self.nome} esta conversando sobre {assunto}')
    
    def comer(self, alimento):
        
        if self.comendo:
            print(f'{self.nome} já esta comendo.')
            return
        
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
        
    def parar_comer(self):
        if not self.comer:
            print(f'{self.nome} não está comendo')
            return
        
        print(f'{self.nome} parou de comer. ')
        self.comendo =  False         