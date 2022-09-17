class Nodo:

    def __init__(self,clave):
        self.id = clave
        self.conectadoA = {}
        #nuevas variables
        self.estado = 'No visitado'
        self.predecesor=-1
        self.tiempoDescubrimiento=0
        self.tiempoFinalizacion=0

    def agregarVecino(self,vecino,ponderacion):
        self.conectadoA[vecino] = ponderacion

    def _str_(self):
        return str(self.id + self.estado)

    def obtenerConexiones(self):
        return self.conectadoA.keys()
    
    def obtenerAristas(self):
        return str([x.id for x in self.conectadoA])
    
    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self,vecino):
        return self.conectadoA[vecino]

    def asignaEstado(self, valorEstado):
        self.estado=valorEstado

    def obtenerEstado(self):
        return self.estado

    def asignarPredecesor(self,valorpredecesor):
        self.predecesor=valorpredecesor

    def obtenerPredecesor(self):
        return self.predecesor

    def asignarDescubrimiento(self,tiempoDes):
        self.tiempoDescubrimiento=tiempoDes

    def obtenerDescubrimiento(self):
        return self.tiempoDescubrimiento

    def asignarFinalizacion(self,tiempoFin):
        self.tiempoFinalizacion=tiempoFin

    def obtenerFinalizacion(self):
        return self.tiempoFinalizacion
