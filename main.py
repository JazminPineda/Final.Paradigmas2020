import csv
import os #verifica si el archivo existia 

class Principal: #creo una clase 
    def __init__(self): # inicializo atributos
        self.csv_cliente = "Clientes.csv"
        self.csv_viajes = "viajes.csv"#quitar despues

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
            with open(self.csv_cliente, 'r',  newline='', encoding='UTF-8') as file:#abro el archivo con el nombre del 
                # se coloca un nuevo parametro para la funciòn open para que pueda leer cualquier tipo de caracter en español 
                # atributo de la clase
                lectura_csv = csv.DictReader(file)
                #encontrada = False#
                for line in lectura_csv:
                    
                    if cliente in line["Nombre"]: #accedo al nombre de la columna#lower todo en minuso
                        #encontrada = True#
                        buscar_cliente.append(line)
                        print(line)
        except IOError:
            print("\n Ocurrrio un error en el archivo  ")
        except UnicodeError as error:
            print(error)
            
        
        return buscar_cliente

    def Buscar_empresa(self, empresa):#se puede unificar validaciones despues incluso para leer archivo client y empresa
        
        buscar_empresa = []
        try:
            with open(self.csv_cliente, 'r',  newline='', encoding='UTF-8') as file:#abro el archivo con el nombre del 
                # atributo de la clase
                lectura_csv = csv.DictReader(file)
                for line in lectura_csv:
                    if empresa in line["Empresa"]: #accedo al nombre de la columna
                        buscar_empresa.append(line)
            
        except IOError:
                    print("\n Ocurrrio un error en el archivo  ")

        Total_usuarios = len(buscar_empresa)
        print(Total_usuarios) #falta formato
        return buscar_empresa


    def Total_Ventas(self, Client_empleado):
        acumulador = 0
        Lista_doct = []
        for linea_cliente in Client_empleado:
            Lista_doct.append(linea_cliente["Documento"]) #lista de dicc por cliente
       
        
        with open(self.csv_viajes, 'r',  newline='', encoding='UTF-8') as file:#abro el archivo con el nombre del 
                # atributo de la clase
                lectura_csv = csv.DictReader(file)
                
                for linea in lectura_csv:
                   if linea['Documento'] in Lista_doct: #Accedo al dicc con documento hago la comparacion de
                   #pertenencia para detectar si esta el doct a buscar
                        acumulador = float(linea['monto']) + acumulador 
                     
        print(f"El total de ventas es {acumulador}" )     
       
    def menu(self):
        while True:
            print("\n\nMenú Usuario \nElija una opción: "  
            "\n 1. Ingresar nombre de los archivos donde se encuentran los datos " 
            "\n 2. Buscar cliente" 
            "\n 3. Ver usuarios por empresa"
            "\n 4. Total de Ventas de viajes por nombre de empresa" 
            "\n 5. Información por empleado"
            "\n 6. Guardar Consulta"
            "\n 7. Salir ")

            opcion = input("")

            if opcion == "7":
                exit()
            
            if opcion == "1":
                self.buscar_archivos()
                    
            if opcion == "2":
                print("¿Cual cliente desea buscar? ")
                cliente = input("")
                self.Buscar_cliente(cliente)

            if opcion == "3":
                print("¿Cual empresa desea buscar? ")
                empresa = input("")
                self.Buscar_empresa(empresa)

            if opcion == "4":
                print("Digite nombre de la empresa, para ver el total de ventas ")
                empresa = input("")
                Clientes_empresa = self.Buscar_empresa(empresa)
                self.Total_Ventas(Clientes_empresa)

            if opcion == "5":
                 print("Digite numero de documento del empleado para ver información ")
                 empleado = input("")
                 Direc_empleado = self.Buscar_empresa(empleado)
                 self.Total_Ventas(Direc_empleado)
            else:
                    print("\n Por favor elija una opcion valida")    
            
            


def main():
    principal = Principal() # creamos instancia de la clase
    principal.menu()

if __name__ == "__main__": # Cuando se ejecuta el programa inicia como el 
    main()
