class Main:
    pass

print("Testando o projeto.")

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("João", "98765-4321")
conta = Conta(c1._nome, 6565, 300)

print(conta.titular, " numero: ", conta.numero, " seu saldo: ", conta.saldo)
print()
print("Abaixo Modulo Strings")

conta.deposita(10)
conta.saque(50)
conta.extrato()