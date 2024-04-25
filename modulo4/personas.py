class Persona:

    def __init__(self,fullname,fecha_nacimiento):
        self.fullname=fullname
        self.fecha_nacimiento=fecha_nacimiento

ListaPersonas=[]

with open('/workspaces/python0424/modulo4/personas.txt','r') as f:
    data=f.readlines()
    for i in data:
        info=i.split(';')
        fullname=info[1]+info[2]
        pTemp=Persona(fullname,info[3])
        ListaPersonas.append(pTemp)

print(ListaPersonas)