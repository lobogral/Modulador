from sys import path, argv
import re
import os

# Comando clonar
comandoClonar = 'git clone https://github.com/lobogral/'

# Importa los módulos que necesita el programa
def importarModulos():
    if os.path.isfile('dependencias.txt'): 
        arch = open('dependencias.txt', 'r')
        modulos = [linea.rstrip('\n') for linea in arch.readlines()]
        arch.close()

        if (not os.path.isdir('módulos')): 
            os.mkdir('módulos')

        os.chdir('módulos')
        for modulo in modulos:
            if (not os.path.isdir(modulo)):
                os.system(comandoClonar + modulo)
                os.chdir(modulo)
                importarModulos()
                os.chdir('..')
        os.chdir('..')


# Agrego en un archivo el programa correspondiente
arch = open("programa.txt", "w")
arch.write(argv[1])
arch.close()

# Importa el programa correspondiente
os.chdir('..')
if (not os.path.isdir('codes')):
    os.mkdir('codes')
os.chdir('codes')
if (not os.path.isdir(argv[1])):
    os.system(comandoClonar + argv[1])

os.chdir(argv[1])
importarModulos()

