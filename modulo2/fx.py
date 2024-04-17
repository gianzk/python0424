#defincion
def saludar():
    print("Hello ev...")

#call o llamado o invocacion
#saludar()

def saludarv2(name):
    print(f"Hello "+name)

saludarv2("carlos")
saludarv2("juanm")

def saludarv3(name):
    return f"Hello "+name

nameV1=saludarv3('name escogido')
print(nameV1)