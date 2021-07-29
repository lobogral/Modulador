from sys import path, argv
import os

# Agrego las dependencias de un programa
def agregarDependencias(ruta): 
    for dependencia in os.listdir(ruta):
        path.append(ruta + dependencia + '/src/')
        if os.path.isdir(ruta + dependencia + '/modules/'):
            agregarDependencias(ruta + dependencia + '/modules/')

# Busco el programa a ejecutar y accedo a su ruta
os.chdir('../temp')
arch = open("code.txt", "r")
os.chdir('../codes/' + arch.readline() + '/src/')
arch.close()

# Agrego las dependencias al programa
if os.path.isdir('../modules/'):
    agregarDependencias('../modules/')

# Ejecuto el programa
exec(open(argv[1]).read())
