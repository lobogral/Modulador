from sys import path, argv
import re
import os

# Agrego las dependencias de un programa
def agregarDependencias(ruta): 
    for dependencia in os.listdir(ruta):
        path.append(ruta + dependencia + '/src/')
        if os.path.isdir(ruta + dependencia + '/modules/'):
            agregarDependencias(ruta + dependencia + '/modules/')

# Busco el programa a ejecutar
os.chdir('../temp')
arch = open("code.txt", "r")
rutaPrograma = '../codes/' + arch.readline() + '/'
arch.close()

# Agrego las dependencias al programa
if os.path.isdir(rutaPrograma + '/modules/'):
    agregarDependencias(rutaPrograma + '/modules/')

# Ejecuto el programa
rutaSubPrograma = rutaPrograma + '/src/' + argv[1]
subPrograma = open(rutaSubPrograma, 'r', encoding='utf8')
texto = subPrograma.readlines()
subPrograma.close()

texto = "".join(texto)
texto = re.sub('desde (.+) importar (.+)', 'from \g<1> import \g<2>', texto)
texto = re.sub('escribir\(', 'print(', texto)
texto = re.sub('tamaño\(', 'len(', texto)
exec(texto)
