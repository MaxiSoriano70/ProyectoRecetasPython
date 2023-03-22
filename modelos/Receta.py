import json
from datetime import datetime
# -*- coding: utf-8 -*-

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

class Receta:
    count=1
    def __init__(self,nombre,listaIngredientes,listaPasos,tiempoPreparacion,tiempoCoccion,idReceta=0,):
        if(idReceta==0):
            self.idReceta=Receta.count
            Receta.count+=1
        else:
            self.idReceta=idReceta
            Receta.count=idReceta
        self.nombre=nombre.capitalize()
        self.listaIngredientes=listaIngredientes
        self.preparacion=listaPasos
        """ self.imagen="" """
        self.tiempoDePreparacion=tiempoPreparacion.lower()
        self.tiempoDeCoccion=tiempoCoccion.lower()
        self.fechaCreacion=datetime.now()

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre.capitalize()
    
    def get_listaIngredientes(self):
        return self.__listaIngredientes
    
    def set_listaIngredientes(self, listaIngredientes):
        self.__listaIngredientes = listaIngredientes
    
    def get_listaPasos(self):
        return self.__listaPasos
    
    def set_listaPasos(self, listaPasos):
        self.__listaPasos = listaPasos
    
    def get_tiempoDePreparacion(self):
        return self.__tiempoDePreparacion
    
    def set_tiempoDePreparacion(self, tiempoDePreparacion):
        self.__tiempoDePreparacion = tiempoDePreparacion.lower()
    
    def get_tiempoDeCoccion(self):
        return self.__tiempoDeCoccion
    
    def set_tiempoDeCoccion(self, tiempoDeCoccion):
        self.__tiempoDeCoccion = tiempoDeCoccion.lower()
    
    def get_fechaCreacion(self):
        return self.fechaCreacion
    
    def buscar_ingrediente(self, idIngrediente):
        for ingrediente in self.listaIngredientes:
            if ingrediente.get_idIngrediente() == idIngrediente:
                return ingrediente
        return None
    
    def editar_nombre_ingrediente(self, idIngrediente, nuevo_nombre):
        ingrediente=self.buscar_ingrediente(idIngrediente)
        if(ingrediente==None):
            return None
        ingrediente.set_nombre(nuevo_nombre)

    def editar_unidad_medida_ingrediente(self, idIngrediente, nueva_medida):
        ingrediente=self.buscar_ingrediente(idIngrediente)
        if(ingrediente==None):
            return None
        ingrediente.set_unidadDeMedida(nueva_medida)

    def editar_cantidad_ingrediente(self, idIngrediente, nueva_cantidad):
        ingrediente=self.buscar_ingrediente(idIngrediente)
        if(ingrediente==None):
            return None
        ingrediente.set_cantidad(nueva_cantidad)

    def mostrar_ingrediente(self,idIngrediente):
        ingrediente=self.buscar_ingrediente(idIngrediente)
        if(ingrediente==None):
            return None
        print(f"- Nombre: {ingrediente.get_nombre()}")
        print(f"  Cantidad: {ingrediente.get_cantidad()}")
        print(f"  Unidad de medida: {ingrediente.get_unidadDeMedida()}")

    def mostrar_ingredientes(self):
        print("Lista de ingredientes:")
        for ingrediente in self.listaIngredientes:
            print(f"- Nombre: {ingrediente.get_nombre()}")
            print(f"  Cantidad: {ingrediente.get_cantidad()}")
            print(f"  Unidad de medida: {ingrediente.get_unidadDeMedida()}")

    def mostrar_lista_pasos(self):
        print("Lista de Pasos:")
        aux=1
        for paso in self.preparacion:
            print(f"{aux}. {paso}")
            aux+=1
    
    def a_json(self):
        # Convierte la lista de objetos Ingrediente en una lista de diccionarios
        lista_ingredientes = []
        for ingrediente in self.listaIngredientes:
            lista_ingredientes.append({
                'idIngrediente': ingrediente.idIngrediente,
                'nombre': ingrediente.nombre,
                'unidadDeMedida': ingrediente.unidadDeMedida,
                'cantidad': ingrediente.cantidad
            })
        # Convierte datetime en una cadena legible
        fecha_creacion = self.fechaCreacion.isoformat()
        return {
            'idReceta': self.idReceta,
            'nombre': self.nombre,
            'listaIngredientes': lista_ingredientes,
            'preparacion': self.preparacion,
            'tiempoDePreparacion': self.tiempoDePreparacion,
            'tiempoDeCoccion': self.tiempoDeCoccion,
            'fechaCreacion': fecha_creacion
        }

ingrediente1=Ingrediente("maiz","gramos","100")
ingrediente2=Ingrediente("Aceite","cucharadas","3")
ingrediente3=Ingrediente("Azucar","gramos","200")
ingrediente4=Ingrediente("manteca","gramos","100")
ingredientes=[ingrediente1,ingrediente2,ingrediente3,ingrediente4]

pasos=["Colocar aceite en una cacerola y llevar al fuego.","Incorporar el maiz pisingallo en la cacerola y tapar.","En una cacerola colocar el azucar y llevar al fuego para que se disuelva y tome colocar caramelo.",
"Agregar la manteca al caramelo.","Anadir el pochoclo listo y revolver"]

receta1=Receta(nombre="Pochoclos",listaIngredientes=ingredientes,listaPasos=pasos,tiempoPreparacion="15 minutos",tiempoCoccion="10 minutos")

ingre1=Ingrediente("huevos","unidADES","4")
ingre2=Ingrediente("Jamon cocido","gramos","200")
ingre3=Ingrediente("Ajo","dientes","2")
ingre4=Ingrediente("Sal","gr","a gusto")
ingre5=Ingrediente("Pimienta","gr","a gusto")
ingre6=Ingrediente("Oregano","gr","a gusto")
ingre7=Ingrediente("Mozzarella","gr","500")
ingre8=Ingrediente("Pan rayado","gr","Cantidad necesaria")
ingre9=Ingrediente("Salsa de tomate","L","1/2")
ingre10=Ingrediente("Sal","gr","a gusto")
ingre11=Ingrediente("Peceto","K","1")
ingre12=Ingrediente("Aceite","L","a gusto")
ingre13=Ingrediente("Papas","K","1")

ingres=[ingre1,ingre2,ingre3,ingre4,ingre5,ingre6,ingre7,ingre8,ingre9,ingre10,ingre11,ingre12,ingre13]
pa=["Pele los ajos y pique junto con el perejil.","Coloque los huevos en un bowl y bata hasta disolverlos bien. Luego agregue el perejil, los ajos y condimente con sal y pimienta.","Pele y corte las papas en bastones, luego sequelas.","Coloque la carne en la mezcla anterior, deje unos minutos, retire y pase por pan rallado.","En una sarten con abundante aceite caliente fria las milanesas. Retire y escurra en papel absorbente.","Acomode luego las milanesas en una placa para horno, bane con salsa de tomate, encima el jamon cocido y por ultimo la mozzarella.","Cocine en horno bien caliente hasta gratinar la mozzarella.","En una sarten con abundante aceite caliente fria las papas. Retire y escurra en papel absorbente.","Espolvoree las milanesas con oregano y acompane con las papas fritas."]

receta2=Receta(nombre="Milanesa a la napolitana",listaIngredientes=ingres,listaPasos=pa,tiempoPreparacion="40 min",tiempoCoccion="20 min")

def guardar_receta(receta, archivo):
    with open(archivo, 'a', encoding='utf-8') as f:
        json.dump(receta.a_json(), f)

guardar_receta(receta1, 'json/recetas.json')
guardar_receta(receta2, 'json/recetas.json')