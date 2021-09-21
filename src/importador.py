"""
Realiza importaciones de modulos para desarrollo
"""
from sys import path
import os

def __importarDependencias(urlsDepsImportadas, nombreRep):
    arch = open(nombreRep + '/depsGit.txt', 'r')
    urlsDepsImportar = [lineaArch.rstrip('\n') for lineaArch in arch.readlines()]
    urlsDepsImportar = [val for val in urlsDepsImportar if val not in urlsDepsImportadas]
    arch.close()
    
    for urlDepImportar in urlsDepsImportar:
        if urlDepImportar not in urlsDepsImportadas:
            urlsDepsImportadas += [urlDepImportar]
            os.system('git clone ' + urlDepImportar)
            nombreDep = urlDepImportar.split('/').pop()
            if os.path.isfile(nombreDep + '/depsGit.txt'):
                urlsDepsImportadas = __importarDependencias(urlsDepsImportadas, nombreDep)

    return urlsDepsImportadas

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
            __importarDependencias([], nombreRep)

        # Importa las dependencias de python
        os.system("py -m venv entVir")

        depsPython = []
        carpetas = os.listdir()
        carpetas.remove('entVir')
        carpetas.remove('Modulador')
        for carpeta in carpetas:
            if os.path.isfile(carpeta + '/depsPython.txt'):
                arch = open(carpeta + '/depsPython.txt', 'r')
                depsPython += [linea.rstrip('\n') for linea in arch.readlines()]
                arch.close()
        install = list(set(['pip install ' + dep for dep in depsPython]))
        install = ['call entVir\Scripts/activate.bat'] + install + ['deactivate']
        install = " & ".join(install)
        os.system(install)
