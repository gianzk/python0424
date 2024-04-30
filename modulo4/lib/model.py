from sqlite3 import Connection

class UsuarioBd:
    list_usuarios=[]    
    def __init__(self,conextion:Connection) -> None:
        self.conextion=conextion
        pass
    def setData(self,nombre,edad,email):
        self.nombre=nombre
        self.edad=edad
        self.email=email
    def getTuple(self):
        return (self.nombre,self.edad,self.email)

    def inserInBd(self):
       cursor=self.conextion.cursor()
       query=f"INSERT INTO usuarios VALUES ('{self.getTuple()[0]}',{self.getTuple()[1]},'{self.getTuple()[2]}')"
       cursor.execute(query)
       self.conextion.commit()

    def getUsers(self):
        cursor=self.conextion.cursor()
        query="select * from usuarios"
        cursor.execute(query)
        datos=cursor.fetchall()
#        print(datos[0],"=>",type(datos[0]))
        for i in datos:
            print(i)
            print("nombre",i[0])
            self.list_usuarios.append(i[0])
        
    def userExist(self,user):
        if user in self.list_usuarios:
            print("usuario existe")
        else:
            print("usuario no existe")
            self.otherFx()
    def otherFx(self):
        print("otra funcion")