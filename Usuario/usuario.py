class Usuario:
    def __init__(self, nombre, email, balance):
        self.nombre = nombre
        self.email = email
        self.balance_cuenta = balance
        
        
    def hacer_deposito(self, amount):
        self.balance_cuenta += amount

    def hacer_giro(self, amount):
        self.balance_cuenta -= amount

    def transferir_dinero(self, other_user, amount):
        self.hacer_giro(amount)
        other_user.hacer_deposito(amount)

    def mostrar_balance_usuario (self):
        print(self.nombre,"$", self.balance_cuenta)


Usuario1=Usuario("Guido van Rossum", "guido@python.com", 900)     
Usuario2=Usuario("Adrien", "adrien@python.com", 400)  
Usuario3=Usuario("Benny Bob", "benny@python.com", 200)  


Usuario1.hacer_deposito(100)
Usuario1.hacer_deposito(200)
Usuario1.hacer_deposito(150)
Usuario1.hacer_giro(50)
Usuario1.mostrar_balance_usuario()

Usuario2.hacer_deposito(100)
Usuario2.hacer_deposito(200)
Usuario2.hacer_giro(150)
Usuario2.hacer_giro(50)
Usuario2.mostrar_balance_usuario()

Usuario3.hacer_deposito(200)
Usuario3.hacer_giro(20)
Usuario3.hacer_giro(40)
Usuario3.hacer_giro(100)
Usuario3.mostrar_balance_usuario()

#Realizar transferencia de dinero de usuario 1 a usuario 3
Usuario1.transferir_dinero(Usuario3, 200)
Usuario1.mostrar_balance_usuario()
Usuario3.mostrar_balance_usuario()