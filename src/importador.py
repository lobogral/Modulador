from sys import path, argv
import re
import os

# Importa las dependencias que necesita un programa
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
            os.system('git clone ' + depImportar)
            os.chdir(depImportar.split('/').pop())
            if os.path.isfile('dependencias.txt'):
                depsImportadas = importarDependencias(depsImportadas)
            os.chdir('..')

    if depsImportar:
        os.chdir('..')

    return depsImportadas

# Agrego en un archivo temporal el programa correspondiente
os.chdir('..')
if (not os.path.isdir('temp')): os.mkdir('temp')
os.chdir('temp')
arch = open("code.txt", "w")
arch.write(argv[1].split('/').pop())
arch.close()

# Importa el programa correspondiente
os.chdir('..')
if (not os.path.isdir('codes')): os.mkdir('codes')
os.chdir('codes')

if (not os.path.isdir(argv[1])):
    os.system('git clone ' + argv[1])
    os.chdir(argv[1].split('/').pop())
    if os.path.isfile('dependencias.txt'): importarDependencias([])
    os.chdir('..')

