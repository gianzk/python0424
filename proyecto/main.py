from servicios.functions import *
from monitoreo.logger import *

log= Logger()

def showOpcionts():
    msg="""
     Bienvenido ...
    1. Cargar Dat
    2. Gene R
    3. Mostra G
    4. Salir
    """
    print(msg)
    opcion=int(input("Ingrese la opcion :"))
    return opcion

def getFunction(opcion):
   # hacer el bucle 
    if opcion == 1:
        print("ingrese aqui")
        loadData()
        log.message(f'realizo la carga de archivo')
    if opcion ==2:
        #póner log
        generateReport()
    if opcion ==3 :
        showData()

if __name__=='__main__':
    while True:
        opcion=showOpcionts()
        getFunction(opcion)

