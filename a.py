import sys

#print (f'Número de parámetros: {len(sys.argv)}')
#print (f'Lista de argumentos: {sys.argv}')

#print (f'informar {sys.argv[5]}')

for p in range (len(sys.argv)):
    if sys.argv[p] == '-t':
        tiempo = int(sys.argv[p + 1])
        print(f't: {tiempo}')

    if sys.argv[p] == '-c':
        columna = int(sys.argv[p + 1])
        print(f'c: {columna}')

    if sys.argv[p] == '-f':
        fila = int(sys.argv[p + 1])
        print(f'f: {fila}')