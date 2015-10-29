def simbolo(simbolo,N):
    f = open(nombreArchivo,"r")
    l = f.readlines()
    linea = l[N]
    simbolo = linea[1]
    if simbolo in linea:
        print (l[N])
