from sys import path, argv
import re
import os

# Agrego las dependencias de un programa
def agregarDependencias(ruta): 
    for dependencia in os.listdir(ruta):
        path.append(ruta + dependencia + '/código/')
        if os.path.isdir(ruta + dependencia + '/módulos/'):
            agregarDependencias(ruta + dependencia + '/módulos/')

# Busco el programa a ejecutar
arch = open("programa.txt", "r")
rutaPrograma = '../codes/' + arch.readline() + '/'
arch.close()

# Agrego las dependencias al programa
if os.path.isdir(rutaPrograma + '/módulos/'):
    agregarDependencias(rutaPrograma + '/módulos/')

# Ejecuto el programa
rutaSubPrograma = rutaPrograma + '/código/' + argv[1]
subPrograma = open(rutaSubPrograma, 'r', encoding='utf8')
texto = subPrograma.readlines()
subPrograma.close()

texto = "".join(texto)
texto = re.sub('desde (.+) importar (.+)', 'from \g<1> import \g<2>', texto)
texto = re.sub('escribir\(', 'print(', texto)
texto = re.sub('tamaño\(', 'len(', texto)
exec(texto)
