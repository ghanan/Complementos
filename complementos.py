#!/usr/bin/env python
from os import listdir

complementos = []
comp_nombres = []
productos = []

def incorpora_producto(p):
    global productos
    producto = [l.split('|') for l in open(p).read().splitlines()]
    identificador = producto[0]
    for complemento in producto[1:]:
        if not complemento[0] in comp_nombres:
            exit('Error: '+identificador[0]+' -> '+complemento[0])
        try: kk = float(complemento[1]) + 0.0
        except: exit('Error: '+identificador[0]+' -> '+complemento[0]+': '+complemento[1])
    productos.append(producto)
    print(productos)


def lee_ficheros():
    global complementos, comp_nombres
    complementos=[l.split('|') for l in open('complemento.txt').read().splitlines()]
    comp_nombres = [c[0] for c in complementos]
    productos_ficheros = [f for f in listdir() if f.startswith('pr_')]
    for f in productos_ficheros: incorpora_producto(f)
    # ~ lista_productos = [f[:-8] for f in listdir(self.directorio) if f[-8:]=='-PIM.csv']
    # ~ productos=[l.split('|') for l in open('producto.txt').read().splitlines()]

def main():
    global complementos, productos
    lee_ficheros()
    # ~ print(productos)

if __name__ == '__main__':
    main()
