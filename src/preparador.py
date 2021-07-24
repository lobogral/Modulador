from sys import path, argv
import re
import os

# Agrego en un archivo el programa correspondiente
arch = open("programa.txt", "w")
arch.write(argv[1])
arch.close()

# Importa el programa correspondiente
comandoClonar = 'git clone https://github.com/lobogral/'

os.chdir('..')
if (not os.path.isdir('codes')):
    os.mkdir('codes')
os.chdir('codes')
if (not os.path.isdir(argv[1])):
    os.system(comandoClonar + argv[1])

os.chdir(argv[1])

# Importa los módulos que necesita el programa
arch = open('dependencias.txt', 'r')
lineasDep = arch.readlines()
arch.close()
modulos = [linea.rstrip('\n') for linea in lineasDep]

if (not os.path.isdir('módulos')): 
    os.mkdir('módulos')
os.chdir('módulos')

for modulo in modulos:
    if (not os.path.isdir(modulo)):
        os.system(comandoClonar + modulo)
