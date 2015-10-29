## Las ideas no fluyen
## Sabemos lo que tenemos que hacer
def Dicc quimico (simbolo,nombre,masaatomica):
    N = 118
    def lines(nombreArchivo,N):
 try:
  f = open(nombreArchivo,"r")
  l = f.readlines()
  Data =l[:N]
  simbolo = Data[2]
  nombre = Data[3]
  if simbolo in Data[2]:
      return
