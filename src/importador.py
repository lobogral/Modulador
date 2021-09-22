"""
Realiza importaciones de modulos para desarrollo
"""
from sys import path
import os

def __importarDepsGit(urlsDepsImportadas, nombreRep):
    arch = open(nombreRep + '/depsGit.txt', 'r')
    urlsDepsImportar = [lineaArch.rstrip('\n') for lineaArch in arch.readlines()]
    urlsDepsImportar = [val for val in urlsDepsImportar if val not in urlsDepsImportadas]
    arch.close()
    
    for urlDepImportar in urlsDepsImportar:
        if urlDepImportar not in urlsDepsImportadas:
            os.system('git clone ' + urlDepImportar)
            nombreRep = urlDepImportar.split('/').pop()
            urlsDepsImportadas += [urlDepImportar]
            if os.path.isfile(nombreRep + '/depsGit.txt'):
                urlsDepsImportadas = __importarDepsGit(urlsDepsImportadas, nombreRep)

    return urlsDepsImportadas

def __importarDepsPython():

    depsPython = []
    carpetas = os.listdir()
    carpetas.remove('Modulador')
    for carpeta in carpetas:
        if os.path.isfile(carpeta + '/depsPython.txt'):
            arch = open(carpeta + '/depsPython.txt', 'r')
            depsPython += [linea.rstrip('\n') for linea in arch.readlines()]
            arch.close()

    if depsPython:
        os.system("py -m venv entVir")
        install = list(set(['pip install ' + dep for dep in depsPython]))
        install = ['call entVir\Scripts/activate.bat'] + install + ['deactivate']
        install = " & ".join(install)
        os.system(install)

def importarRepositorio(urlRep):

    nombreRep = urlRep.split('/').pop()
    
    # Agrego en un archivo temporal el nombre del repositorio
    os.chdir('..')
    if (not os.path.isdir('temp')): os.mkdir('temp')
    os.chdir('temp')
    arch = open("code.txt", "w")
    arch.write(nombreRep)
    arch.close()

    # Importa el repositorio correspondiente
    os.chdir('../..')

    if (not os.path.isdir(nombreRep)):
        os.system('git clone ' + urlRep)

        # Importa las dependencias de git
        if os.path.isfile(nombreRep + '/depsGit.txt'):
            __importarDepsGit([], nombreRep)

        # Importa las dependencias de python en un entorno virtual
        __importarDepsPython()
