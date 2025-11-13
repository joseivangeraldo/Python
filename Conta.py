class Conta:
    def __init__(self, titular, numero, saldo = 0):
        self.titular = titular
        self.numero = numero
        self.saldo =  saldo

        @property  ### outro recurso do python para fazer a classe privada
        def get_saldo(self):
            return self._saldo
            
        def set_saldo(self, saldo):
            if (saldo < 0):
                print("O Saldo não pode ser negativo.")
            else:
                self._saldo = valor

    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print("Saque realizado com sucesso")
        else:
                print("Saldo insuficiente.")
        
    def deposita(self, valor):
            self.saldo += valor

    def extrato(self):
            print("Cliente: ", self.titular)
            print("Saldo Atual : ", self.saldo)
        