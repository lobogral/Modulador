from sys import path
import os

def __agregarSrcDependencias(ruta): 
    for dependencia in os.listdir(ruta):
        path.append(ruta + dependencia + '/src/')
        if os.path.isdir(ruta + dependencia + '/modules/'):
            __agregarSrcDependencias(ruta + dependencia + '/modules/')

def ejecutarModulo(modulo, argv):
    # Busco el src del repositorio y accedo a su ruta
    os.chdir('../temp')
    arch = open("code.txt", "r")
    os.chdir('../codes/' + arch.readline() + '/src/')
    arch.close()

    # Agrego los src de las dependencias del repositorio
    if os.path.isdir('../modules/'):
        __agregarSrcDependencias('../modules/')

    # Ejecuto un modulo del repositorio
    arch = open(modulo + ".py", "r")
    programa = arch.read()
    arch.close()
    exec(programa)
