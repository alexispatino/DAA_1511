from arbol import Arbol

arbol_numeros = Arbol(20)
arbol_numeros.agregar(23)
arbol_numeros.agregar(57)
arbol_numeros.agregar(19)
arbol_numeros.agregar(67)
arbol_numeros.agregar(99)
arbol_numeros.preorden()
arbol_numeros.inorden()


busqueda = int(input("Ingresa un número para buscar en el árbol: "))
n = arbol_numeros.buscar(busqueda)
if n is None:
    print(f"{busqueda} no existe")
else:
    print(f"{busqueda} sí existe") 