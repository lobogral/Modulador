"""
Realiza importaciones de modulos para desarrollo
"""
from sys import path
import os
import re

def __importarDepsGit(urlsDepsImportadas, rutArch):
    arch = open(rutArch, 'r')
    repositorios = re.findall('https://github.com/\w+/\w+', arch.read())
    urlsDepsImportar = [lineaArch.rstrip('\n') for lineaArch in repositorios]
    urlsDepsImportar = [val for val in urlsDepsImportar if val not in urlsDepsImportadas]
    arch.close()
    
    for urlDepImportar in urlsDepsImportar:
        if urlDepImportar not in urlsDepsImportadas:
            nombreRepDep = urlDepImportar.split('/').pop()
            rutArch = nombreRepDep + '\setup.py'
            os.system('git clone ' + urlDepImportar)
            os.system('pip install --no-deps -e ' + nombreRepDep)
            urlsDepsImportadas += [urlDepImportar]
            if os.path.isfile(rutArch):
                urlsDepsImportadas = __importarDepsGit(urlsDepsImportadas, rutArch)

    return urlsDepsImportadas

def importarRepositorio(urlRep):

    nombreRep = urlRep.split('/').pop()

    # Importa el repositorio correspondiente
    os.chdir('../..')

    if (not os.path.isdir(nombreRep)):

        os.system('git clone ' + urlRep)

        # Importa las dependencias de git
        rutArch = ""    
        if os.path.isfile(nombreRep + '/setup.py'):
            rutArch = nombreRep + "/setup.py"
        if os.path.isfile(nombreRep + '/requirements.txt'):
            rutArch = nombreRep + "/requirements.txt"
    
        if os.path.isfile(nombreRep + '/depsGit.txt'):
            __importarDepsGit([], rutArch)
