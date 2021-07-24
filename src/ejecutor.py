from sys import path, argv
import re

# Busco el programa a ejecutar
arch = open("programa.txt", "r")
rutaPrograma = '../codes/' + arch.readline() + '/'
arch.close()

# Busco las dependencias a agregar
arch = open(rutaPrograma + 'dependencias.txt', 'r')
lineasDep = arch.readlines()
arch.close()
modulos = [linea.rstrip('\n') for linea in lineasDep]

# Agrego las dependencias
for modulo in modulos:
    path.append(rutaPrograma + '/módulos/' + modulo + '/código/')

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
