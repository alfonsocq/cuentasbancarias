class Cuentabancaria:
   
   def __init__(self,balancedecuenta,interes):
     self.balancedecuenta = 0
     self.interes= 0
   def deposito(self,monto):
     self.balancedecuenta += monto
   def retiro(self, monto):
     if (self.balancedecuenta-monto) < 0:
      print("Fondos insuficientes, cobrando una tarifa de 5 dolares")
      self.balancedecuenta -= 5
     else:
      self.balancedecuenta -= monto
   def mostrar_info_cuenta(self):
      print(balancedecuenta)
      print(interes)
   def generar_interes(self):
      self.interes += (self.balancedecuenta*1/100)

Kloe = Cuentabancaria(0,0)
Firulais = Cuentabancaria(0,0)


Kloe.deposito(100)
Kloe.deposito(200)
Kloe.deposito(40)
Kloe.retiro(350)
Kloe.generar_interes()

Firulais.deposito(300)
Firulais.deposito(500)
Firulais.retiro(100)
Firulais.retiro(200)
Firulais.retiro(100)
Firulais.retiro(100)
Firulais.generar_interes

print(Kloe.balancedecuenta + Kloe.interes)

print(Firulais.balancedecuenta + Firulais.interes)


