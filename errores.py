def obtener_total(factura):
    # factura es un diccionario tipo: {"numero": "A-001", "neto": "2500"}
    # Convertí factura["neto"] a float
    # Devolvé el total con IVA (neto * 1.21)
    # Si el neto no se puede convertir, imprimí "Neto inválido" y devolvé 0
    try:
        neto = float(factura["neto"])
        return neto * 1.21
        
    except ValueError:
        print("Neto invalido")
        return 0
    
    except KeyError:
        print("No se encontro el neto de la factura")
        return 0
    
print(obtener_total({"numero": "A-001", "neto": "2500"}))
print(obtener_total({"numero": "A-002", "neto": "abc"}))
print(obtener_total({"numero": "A-003"}))