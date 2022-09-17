from Grafo import Grafo


g = Grafo()
for i in (1,2,3,4,5):
    g.agregarNodo(i)

g.agregarArista(1,2)
g.agregarArista(2,3)
g.agregarArista(3,4)
g.agregarArista(4,5)
g.agregarArista(1,5)
g.agregarArista(3,1)

n=2
print("Busqueda en anchura desde el vertice ",n)
g.busquedaEnAnchura(g.obtenerNodo(n))