from sys import path
import os

def __importarDependencias(depsImportadas):
    arch = open('deps.txt', 'r')
    depsImportar = [lineaArch.rstrip('\n') for lineaArch in arch.readlines()]
    depsImportar = [val for val in depsImportar if val not in depsImportadas]
    arch.close()

    if depsImportar:
        os.mkdir('modules')
        os.chdir('modules')
    
    for depImportar in depsImportar:
        if depImportar not in depsImportadas:
            depsImportadas += [depImportar]
            os.system('git clone ' + depImportar)
            os.chdir(depImportar.split('/').pop())
            if os.path.isfile('deps.txt'):
                depsImportadas = __importarDependencias(depsImportadas)
            os.chdir('..')

    if depsImportar:
        os.chdir('..')

    return depsImportadas


def importarRepositorio(repositorio):
    # Agrego en un archivo temporal el programa correspondiente
    os.chdir('..')
    if (not os.path.isdir('temp')): os.mkdir('temp')
    os.chdir('temp')
    arch = open("code.txt", "w")
    arch.write(repositorio.split('/').pop())
    arch.close()

    # Importa el programa correspondiente
    os.chdir('..')
    if (not os.path.isdir('codes')): os.mkdir('codes')
    os.chdir('codes')

    if (not os.path.isdir(repositorio.split('/').pop())):
        os.system('git clone ' + repositorio)
        os.chdir(repositorio.split('/').pop())
        if os.path.isfile('deps.txt'): __importarDependencias([])
        os.chdir('..')
