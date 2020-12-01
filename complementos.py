#!/usr/bin/env python
from os import listdir
from sys import argv

complementos = []
comp_nombres = []
productos = []
lis_produc = []
lis_elegidos = []

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

def lee_ficheros():
    global complementos, comp_nombres
    complementos=[l.split('|') for l in open('complemento.txt').read().splitlines()]
    comp_nombres = [c[0] for c in complementos]
    productos_ficheros = [f for f in listdir() if f.startswith('pr_')]
    for f in productos_ficheros: incorpora_producto(f)
    # ~ lista_productos = [f[:-8] for f in listdir(self.directorio) if f[-8:]=='-PIM.csv']
    # ~ productos=[l.split('|') for l in open('producto.txt').read().splitlines()]

def lista_productos():
    for p in productos:
        print(p[0][2],p[0][1])

def parametros_correctos(param):
    for l in lis_elegidos:
        if not l[0] in [p[0] for p in lis_produc]:
            exit('Error: producto ' + l[0] + ' desconocido')
            return False
    for l in range(2, len(argv), 2):
        if not argv[l] in ['0.5', '1', '1.5', '2', '2.5', '3']:
            exit('Error: cantidad ' + argv[l] + ' en producto ' + argv[l-1])
            return False
    return True

def ordena_elegidos():
    global lis_elegidos
    _l = []
    for l in lis_elegidos:
        for p in productos:
            if l[0] == p[0][0]: _l.append([l[0],len(p)])
    lis_elegidos = [l[0] for l in sorted(_l, key=lambda i: i[1], reverse=True)]
    print(lis_produc)

def rellena_listas_trabajo(param):
    global lis_produc, lis_elegidos
    for p in productos: lis_produc.append(p[0])
    for l in range(1, len(argv), 2):
        lis_elegidos.append([argv[l]])
    print(lis_elegidos)

def procesa(param):
    ordena_elegidos()
    pass

def main():
    global complementos, productos
    lee_ficheros()
    if len(argv) == 1: exit('Faltan argumentos (prod | producto num_unidades [...])')
    if argv[1].lower() == 'prod':
        lista_productos()
        exit()
    if len(argv) > 2:
        rellena_listas_trabajo(argv[2:])
        if parametros_correctos(argv[2:]): procesa(argv[2:])
    else:
        exit('Error en argumentos(producto num_unidades [...]')

if __name__ == '__main__':
    main()
