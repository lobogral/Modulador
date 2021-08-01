from sys import path
import os

def __importarDependencias(urlsDepsImportadas):
    arch = open('deps.txt', 'r')
    urlsDepsImportar = [lineaArch.rstrip('\n') for lineaArch in arch.readlines()]
    urlsDepsImportar = [val for val in urlsDepsImportar if val not in urlsDepsImportadas]
    arch.close()

    if urlsDepsImportar:
        os.mkdir('modules')
        os.chdir('modules')
    
    for urlDepImportar in urlsDepsImportar:
        if urlDepImportar not in urlsDepsImportadas:
            urlsDepsImportadas += [urlDepImportar]
            os.system('git clone ' + urlDepImportar)
            nombreDep = urlDepImportar.split('/').pop()
            os.chdir(nombreDep)
            if os.path.isfile('deps.txt'):
                urlsDepsImportadas = __importarDependencias(urlsDepsImportadas)
            os.chdir('..')

    if urlsDepsImportar:
        os.chdir('..')

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
    os.chdir('..')
    if (not os.path.isdir('codes')): os.mkdir('codes')
    os.chdir('codes')

    if (not os.path.isdir(nombreRep)):
        os.system('git clone ' + urlRep)
        os.chdir(nombreRep)
        if os.path.isfile('deps.txt'): __importarDependencias([])
        os.chdir('..')
