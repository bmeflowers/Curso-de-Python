class Vehículos:
    def __init__(self, marca,modelo, precio):
        #encapsulacióm
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True

    def vender(self):
        if self.disponible:
            self.disponible = False
            print(f"El vehiculo {self.marca}. Ha sido vendido")
        else:
            print(f"El vehiculo {self.modelo}. No esta disponible")
    
    #abstracción
    def disponibilidad(self):
        return self.disponible
    
    #abstraccón
    def obtener_precio(self):
        return self.precio
    
    def iniciar_func(self):
        raise NotImplementedError("Este método debe ser implementado por la sub clase")
        
    def detener_fuc(self):
        raise NotImplementedError("Este método debe ser implementado por la sub clase")

#herencia
class Auto(Vehículos):
    #Polimorfismo
    def iniciar_func(self):
        if not self.disponible:
            return f"El motor del coche {self.marca} está en marcha"
        else:
            return f"El coche {self.marca} no está disponible"

    #polimorfismo   
    def detener_func(self):
        if self.disponible:
            return f"El motor del coche {self.marca} se ha detenido"
        else: 
            return f"El coche {self.marca}. No está disponible"

#herencia
class Bicicleta(Vehículos):
    #polimorfismo
    def iniciar_func(self):
        if not self.disponible:
            return f"La bicicleta {self.marca} está en marcha"
        else:
            return f"La bicicleta {self.marca} no está disponible"
    
    #polimorfismo
    def detener_func(self):
        if self.disponible:
            return f"La bicicleta {self.marca} se ha detenido"
        else: 
            return f"La bicicleta {self.marca}. No está disponible"
    
class Camion(Vehículos):
    def iniciar_func(self):
        if not self.disponible:
            return f"El motor del camión {self.marca} está en marcha"
        else:
            return f"El camión {self.marca} no está disponible"
        
    def detener_func(self):
        if self.disponible:
            return f"El motor del camión {self.marca} se ha detenido"
        else: 
            return f"El camión {self.marca}. No está disponible"

class Cliente:
    def __init__(self, name):
        self.name = name 
        self.autos_comprados = []

    def comprar_vehiculo(self, vehiculo: Vehículos):
        if vehiculo.disponibilidad():
            vehiculo.vender()
            self.autos_comprados.append(vehiculo)

        else:
            print(f"El vehículo {vehiculo.marca} no está disponible")

    def preguntar_vehiculo(self, vehiculo: Vehículos):
        if vehiculo.disponibilidad():
            V_disponible = "Disponible"
        else:
            V_disponible = "No disponible"
        print(f"El {vehiculo.marca} está {V_disponible} y cuesta {vehiculo.precio}")

class Dealership:
    def __init__(self):
        self.inventario = []
        self.clientes = []

    def añadir_vehiculos(self, vehiculo: Vehículos):
        self.inventario.append(vehiculo)
        print(f"El vehiculo {vehiculo.marca} ha sido añadido al inventario")

    def registro_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)
        print(f"El cliente {cliente.name} ha sido añadido")

    def mostrar_veh_disp(self):
        print("Vehículos disponibles en la tienda")
        for vehiculo in self.inventario:
            if vehiculo.disponibilidad():
                print(f"-{vehiculo.marca} por {vehiculo.precio}")

#instancias
auto1 = Auto("Toyota", "Corolla", 20000)
bici1 = Bicicleta("Yamaha", "M_70T", 1000)
camion1 = Camion("Volvo", "FH19", 80000)

cliente1 = Cliente("Carla")

tienda = Dealership()
tienda.añadir_vehiculos(auto1)
tienda.añadir_vehiculos(bici1)
tienda.añadir_vehiculos(camion1)

#Mostrar vehiculos disponibles
tienda.mostrar_veh_disp()

#cliente consulta por un vehiculo
cliente1.preguntar_vehiculo(auto1)

#cliente compra vehiculo
cliente1.comprar_vehiculo(auto1)

#Mostrar vehiculos disponibles
tienda.mostrar_veh_disp()


