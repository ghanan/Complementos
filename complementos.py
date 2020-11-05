#!/usr/bin/env python

complementos = []
productos = []

def lee_ficheros():
    global complementos, productos
    complementos=[l.split('|') for l in open('complemento.txt').read().splitlines()]
    productos=[l.split('|') for l in open('producto.txt').read().splitlines()]

def main():
    global complementos, productos
    lee_ficheros()
    print(productos)

if __name__ == '__main__':
    main()
