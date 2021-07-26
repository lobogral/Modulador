from sys import path, argv
import re
import os

# Comando clonar
comandoClonar = 'git clone https://github.com/lobogral/'

# Importa las dependencias que necesita el programa
def importarDependencias(depsImportadas):
    arch = open('dependencias.txt', 'r')
    depsImportar = [lineaArch.rstrip('\n') for lineaArch in arch.readlines()]
    depsImportar = [val for val in depsImportar if val not in depsImportadas]
    arch.close()

    if depsImportar:
        os.mkdir('módulos')
        os.chdir('módulos')
    
    for depImportar in depsImportar:
        if depImportar not in depsImportadas:
            depsImportadas += [depImportar]
            os.system(comandoClonar + depImportar)
            os.chdir(depImportar)
            if os.path.isfile('dependencias.txt'):
                depsImportadas = importarDependencias(depsImportadas)
            os.chdir('..')

    if depsImportar:
        os.chdir('..')

    return depsImportadas

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
    if os.path.isfile('dependencias.txt'): importarDependencias([])
    os.chdir('..')

