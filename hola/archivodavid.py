def lines(nombreArchivo,N):
    try:
        f = open(nombreArchivo,"r")
        l = f.readlines()
        return l[:N]
    except:
        return("error")
simbolo= str(input("introduzca el simbolo entre comillas"))
for i in range(1,118):
    serie= (lines('pt-data1.csv',i).split('')
    print serie[2]
