from sys import path, argv
import os

def agregarDependencias(ruta): 
    for dependencia in os.listdir(ruta):
        path.append(ruta + dependencia + '/src/')
        if os.path.isdir(ruta + dependencia + '/modules/'):
            agregarDependencias(ruta + dependencia + '/modules/')

def ejecutarModulo(modulo):
    # Busco el programa a ejecutar y accedo a su ruta
    os.chdir('../temp')
    arch = open("code.txt", "r")
    os.chdir('../codes/' + arch.readline() + '/src/')
    arch.close()

    # Agrego las dependencias al programa
    if os.path.isdir('../modules/'):
        agregarDependencias('../modules/')

    # Ejecuto un modulo del programa
    arch = open(modulo + ".py", "r")
    programa = arch.read()
    arch.close()
    exec(programa)
