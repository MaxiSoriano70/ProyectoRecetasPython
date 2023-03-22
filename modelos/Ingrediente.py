class Ingrediente:
    count=1
    def __init__(self,nombre,unidadDeMedida,cantidad,idIngrediente=0):
        if(idIngrediente==0):
            self.idIngrediente=Ingrediente.count
            Ingrediente.count+=1
        else:
            self.idIngrediente=idIngrediente
            Ingrediente.count=idIngrediente
        self.nombre=nombre.capitalize()
        self.unidadDeMedida=unidadDeMedida.lower()
        self.cantidad=cantidad.lower()

    def get_idIngrediente(self):
        return self.idIngrediente

    def set_nombre(self,nombre):
        self.nombre=nombre.capitalize()
    
    def get_nombre(self):
        return self.nombre
    
    def set_unidadDeMedida(self,unidadDeMedida):
        self.unidadDeMedida=unidadDeMedida.lower()
    
    def get_unidadDeMedida(self):
        return self.unidadDeMedida
    
    def set_cantidad(self,cantidad):
        self.cantidad=cantidad.lower()
    
    def get_cantidad(self):
        return self.cantidad