class Menu():
    id              = int
    nombre          = str
    descripción     = str
    precio          = int
    disponibilidad  = bool
    
    def __init__(self,id,  nombre, descripcion, precio, disponibilidad):
        
    
        self.id             = id
        self.nombre         = nombre
        self.descripción    = descripcion
        self.precio         = precio
        self.disponibilidad = disponibilidad