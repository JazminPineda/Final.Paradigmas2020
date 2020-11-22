import csv
import os #verifica si el archivo existia 

class Principal: #creo una clase 
    def __init__(self): # inicializo atributos
        self.csv_cliente = ""
        self.csv_viajes = ""

    def  buscar_archivos(self):
        archivo_cliente = input("Ingrese el nombre del archivo donde se encuentran los clientes ")
        while not os.path.exists(archivo_cliente):# validacion cuando el archiv no existe
            archivo_cliente = input("\n El archivo no se encuentra? Ingresarlo nuevamente ")
        self.csv_cliente = archivo_cliente

        archivo_viajes = input("Ingrese el archivo donde desea buscar el total de viajes ")
        while not os.path.exists(archivo_viajes):# validacion cuando el archiv no existe
            archivo_viajes = input("\n El archivo no se encuentra? Ingresarlo nuevamente ")
        self.csv_viajes = archivo_viajes


    def Buscar_cliente(self, cliente):#falta buscar cual archivo
    
        buscar_cliente = []
        try:
            with open(self.csv_cliente, 'r',  newline='') as file:#abro el archivo con el nombre del 
                # atributo de la clase
                lectura_csv = csv.DictReader(file)
                for line in lectura_csv:
                    if cliente in line["Nombre"]: #accedo al nombre de la columna
                        buscar_cliente.append(line)
        except IOError:
            print("\n Ocurrrio un error en el archivo  ")
        return buscar_cliente

    def menu(self):
        while True:
            print("\n\nMenú Usuario \nElija una opción: "  
            "\n 1. Ingresar nombre de los archivos donde se encuentran los datos " 
            "\n 2. Buscar cliente" 
            "\n 3. Ver usuario por empresa"
            "\n 4. Total de Ventas de viajes por nombre de empresa" 
            "\n 5. Información por empleado"
            "\n 6. Guardar Consulta"
            "\n 7. Salir ")

            opcion = input("")

            if opcion == "6":
                exit()
            
            if opcion == "1":
                self.buscar_archivos()
                    
            if opcion == "2":
                print("¿Cual cliente desea buscar? ")
                cliente = input("")
                self.Buscar_cliente( "", cliente)
        
            else:
                    print("\n Por favor elija una opcion valida")    
            
            if opcion == "3":
                print("")


def main():
    principal = Principal() # creamos instancia de la clase
    principal.menu()

if __name__ == "__main__": # Cuando se ejecuta el programa inicia como el 
    main()
