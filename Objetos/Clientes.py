

class Cliente():
    def __init__(self, nome: str, cpf: str, endereco: str) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        
    @property
    def nome(self):
            return self.__nome
    def cpf(self):
            return self.__cpf
    def endereco(self):
            return self.__endereco
    
    @nome.setter
    def nome(self, value):
        self._nome = value
    
    @cpf.setter
    def cpf(self, value):
        self._cpf = value
    
    @endereco.setter
    def endereco(self, value):
        self._endereco = value
  ##  cliente1 = Cliente()
    
    