
class Producto():
    def __init__(self,codigo, descripcion, precio):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio

    def precio_con_iva(self):
        return self.precio * 1.21


    @classmethod
    def crear_desde_lista(cls, lista):
            return cls(lista[0], lista[1], lista[2])

    @staticmethod
    def validar_codigo(codigo):
        return codigo.startswith("ART") and len(codigo) > 5
    

p = Producto.crear_desde_lista(["ART001", "Yerba 1kg", 2500])
print(p.precio_con_iva())          # 3025.0
print(Producto.validar_codigo("ART001"))  # True
print(Producto.validar_codigo("XX1"))     # False