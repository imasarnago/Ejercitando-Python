class User:
    def __init__(self):
        self.email = input ("Introduzca su email : ")
        self.__password = input("Introduzca su contraseña : ")
        self.permissions = ['edit','create','update']
        self.username = None
        
        
    def setear_useraname (self):
        self.username = input ("Introduzca el username que desea")
        print (f"Username cambiado exitosamente a {self.username}") 
        
class UserPro(User):
    def __init__(self):
        super().__init__()
        self.permissions += ['delete','download']
    def pay_subscription(self,monto):
        print (f"Usted ha pagado exitosamente la subscripción de ${monto}")

class UserManager():
    def create_user (self,subscription):
        if subscription:
            user = UserPro()
        else:
            user = User()
        print (f"Se ha creado exitosamente su usuario. Sus permisos son : {user.permissions}")
        
        
UserManager().create_user(False)

User().__password