from sys import path
import os

def __agregarSrcDependencias(urlsDepsAgregadas, nombreRep):
    arch = open('../../' + nombreRep + '/deps.txt', 'r')
    urlsDepsAgregar = [lineaArch.rstrip('\n') for lineaArch in arch.readlines()]
    urlsDepsAgregar = [val for val in urlsDepsAgregar if val not in urlsDepsAgregadas]
    arch.close()
    
    for urlDepAgregar in urlsDepsAgregar:
        if urlDepAgregar not in urlsDepsAgregadas:
            urlsDepsAgregadas += [urlDepAgregar]
            nombreDep = urlDepAgregar.split('/').pop()
            path.append('../../' + nombreDep + '/src/')
            if os.path.isfile('../../' + nombreDep + '/deps.txt'):
                urlsDepsAgregadas = __agregarSrcDependencias(urlsDepsAgregadas, nombreDep)

    return urlsDepsAgregadas

def ejecutarModulo(nombreModRep, argv):
    # Busco el src del repositorio y accedo a su ruta
    os.chdir('../temp')
    arch = open("code.txt", "r")
    nombreRep = arch.readline()
    arch.close()

    os.chdir('../../' + nombreRep + '/src/')

    # Agrego los src de las dependencias del repositorio
    if os.path.isfile('../../' + nombreRep + '/deps.txt'):
        __agregarSrcDependencias([], nombreRep)

    # Ejecuto un modulo del repositorio
    arch = open(nombreModRep + ".py", "r")
    moduloRep = arch.read()
    arch.close()

    # Aquí se está usando argv implícitamente
    exec(moduloRep)
