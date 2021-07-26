from sys import path, argv
import re
import os

# Comando clonar
comandoClonar = 'git clone https://github.com/lobogral/'

# Importa los módulos que necesita el programa
def importarModulos(lista):
    arch = open('dependencias.txt', 'r')
    modulos = [linea.rstrip('\n') for linea in arch.readlines()]
    modulos = [val for val in modulos if val not in lista]
    arch.close()

    if modulos:
        os.mkdir('módulos')
        os.chdir('módulos')
    
    for modulo in modulos:
        if modulo not in lista:
            lista += [modulo]
            os.system(comandoClonar + modulo)
            os.chdir(modulo)
            if os.path.isfile('dependencias.txt'):
                lista = importarModulos(lista)
            os.chdir('..')

    if modulos:
        os.chdir('..')

    return lista

# Agrego en un archivo el programa correspondiente
arch = open("programa.txt", "w")
arch.write(argv[1])
arch.close()

# Importa el programa correspondiente
os.chdir('..')
if (not os.path.isdir('codes')): os.mkdir('codes')
os.chdir('codes')

if (not os.path.isdir(argv[1])):
    os.system(comandoClonar + argv[1])
    os.chdir(argv[1])
    if os.path.isfile('dependencias.txt'): importarModulos([])
    os.chdir('..')

