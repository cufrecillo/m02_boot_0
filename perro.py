class Perro():
    def __init__(self, n, e, p):
        self.nombre = n
        self.edad = e
        self.peso = p
        
    def ladrar(self):
        if self.peso >= 8:
            print("GUUUAAUU  GUAAAUUU")
        else:
            print("guau guau")
            
    def __str__(self):
        return "Perro {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)
    
class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False
    
    def __str__(self):
        return "Perro de Asistencia de {}".format(self.amo)
    
    def __pasear__(self):
        print("{} ayudo a mi dueño {}, a pasear".formart(self.amo))
        
    def ladrar(self):
        if self.__trabajando:
            print("shhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
            
    def trabajando(self, valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.trabajando = valor