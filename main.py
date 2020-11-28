import csv
import os  # verifica si el archivo existia
import operator


class Principal:  # creo una clase
    def __init__(self):  # inicializo atributos
        self.csv_cliente = "Clientes.csv"
        self.csv_viajes = "viajes.csv"  # quitar despues
        

    def buscar_archivos(self):
        archivo_cliente = input(
            "Ingrese el nombre del archivo donde se encuentran los clientes ")
        # validacion cuando el archiv no existe
        while not os.path.exists(archivo_cliente):
            archivo_cliente = input(
                "\n El archivo no se encuentra? Ingresarlo nuevamente ")
        self.csv_cliente = archivo_cliente

        archivo_viajes = input(
            "Ingrese el archivo donde desea buscar el total de viajes ")
        # validacion cuando el archiv no existe
        while not os.path.exists(archivo_viajes):
            archivo_viajes = input(
                "\n El archivo no se encuentra? Ingresarlo nuevamente ")
        self.csv_viajes = archivo_viajes

    def Buscar_cliente(self, cliente):  # falta buscar cual archivo

        buscar_cliente = []
        try:
            # abro el archivo con el nombre del
            with open(self.csv_cliente, 'r',  newline='', encoding='UTF-8') as file:
                # se coloca un nuevo parametro para la funciòn open para que pueda leer cualquier tipo de caracter en español
                # atributo de la clase
                lectura_csv = csv.DictReader(file)
                #encontrada = False#
                for field in lectura_csv.fieldnames:
                    print(field, end=' | ')
                print()
                for line in lectura_csv:

                    # accedo al nombre de la columna#lower todo en minuso
                    if cliente in line["Nombre"]:
                        #encontrada = True#
                        buscar_cliente.append(line)
                        self.formato()
                        for value in line.values():
                            print(value, end=' | ')
                        print()
                if len(buscar_cliente) == 0:
                    print("En el archivo no se encuentra ningún cliente por ese nombre ")
        
        except IOError:
            print("\n Ocurrrio un error en el archivo  ")
        except UnicodeError as error:
            print(error)

        return buscar_cliente

    # se puede unificar validaciones despues incluso para leer archivo client y empresa
    def Buscar_empresa(self, empresa):
        empresas = []   
        buscar_empresa = {}
        try:
            # abro el archivo con el nombre del
            with open(self.csv_cliente, 'r',  newline='', encoding='UTF-8') as file:
                # atributo de la clase
                lectura_csv = csv.DictReader(file)
                for line in lectura_csv:
                    if empresa.lower() in line["Empresa"].lower():  # accedo al nombre de la columna
                        #empresas.append(line["Empresa"])
                        if line["Empresa"] not in buscar_empresa:
                            buscar_empresa[line["Empresa"]] = []
                            buscar_empresa[line["Empresa"]].append(line) 
                        
                        else:
                            buscar_empresa[line["Empresa"]].append(line) 

        except IOError:
            print("\n Ocurrrio un error en el archivo  ")

        self.formato()
        for clave_empresa in buscar_empresa:
            print(f"Empresa: {clave_empresa}")  # falta formato
            print(f"Total Usuarios: {len(buscar_empresa[clave_empresa])}")
            self.formato()    

            print('        Nombre''         Dirección''       Documento''      Fecha Alta' '     Correo Electrónico''  Empresa')
            for usuario in buscar_empresa[clave_empresa]:
                
                print(f"{usuario['Nombre']:15} {usuario['Dirección']:10} {usuario['Documento']:10} \
                {usuario['Fecha Alta']:10}  {usuario['Correo Electrónico']:10} {usuario['Empresa']:10}")
                self.formato()    

        return buscar_empresa

    def Total_Ventas(self, empresa):
       
        Lista_doct = []
        Ventas_cliente = {}

        try:
            # apareo
            with open(self.csv_cliente, 'r',  newline='', encoding='UTF-8') as f_clientes, \
                open(self.csv_viajes, 'r',  newline='', encoding='UTF-8') as f_viajes:
                # atributo de la clase
                Clientes_csv = csv.reader(f_clientes)
                Viajes_csv = csv.reader(f_viajes)
                    
                #saltea encabezados
                next(Clientes_csv) 
                next(Viajes_csv) 

                #Leer
                Cliente = next(Clientes_csv, None)
                Viajes = next(Viajes_csv, None)

                while (Cliente or Viajes):#mientras q halla un regist se ejecuta en ambos archivos
                    if Cliente:
                        if empresa.lower() in Cliente[5].lower():
                            if Cliente[5] not in Ventas_cliente:
                                Ventas_cliente[Cliente[5]] = {}
                                Ventas_cliente[Cliente[5]]["Documento"] = []
                                Ventas_cliente[Cliente[5]]["Documento"].append(Cliente[2]) #ingreso doc cliente
                                Ventas_cliente[Cliente[5]]["Monto"] = 0 # acumulador se inicia dicc
                            else:
                                Ventas_cliente[Cliente[5]]["Documento"].append(Cliente[2])#si lo encuentra 
                        Cliente = next(Clientes_csv, None) #avanza a la siguiente linea
                    
                    if Viajes:
                        print(f"{Viajes}")
                        for key in Ventas_cliente.keys(): #traigo los nombres
                            print(key)
                            if Viajes[0] in Ventas_cliente[key]["Documento"]:
                                Ventas_cliente[cliente]["Monto"] = float(Viajes[2]) + Ventas_cliente[key]["Monto"]
                        Viajes = next(Viajes_csv, None)

                print(Ventas_cliente)
                for cliente in Ventas_cliente.keys():
                    self.formato()
                    print(f"{cliente} ${Ventas_cliente[cliente]['Monto']:10.2f}")#Solo dos decimales
                    self.formato()
        except IOError:
            print("\n Ocurrrio un error en el archivo  ") 

        

    def Buscar_registros(self, Campo, Valor_buscar):
        pass


    def formato(self):
        print( "-" * os.get_terminal_size()[0])
   
        

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

            elif opcion == "1":
                self.buscar_archivos()

            elif opcion == "2":
                print("¿Cual cliente desea buscar? ")
                cliente = input("")
                self.Buscar_cliente(cliente)

            elif opcion == "3":
                print("¿Cual empresa desea buscar? ")
                empresa = input("")
                self.Buscar_empresa(empresa)

            elif opcion == "4":
                print("Digite nombre de la empresa, para ver el total de ventas ")
                empresa = input("")
                self.Total_Ventas(empresa)

            elif opcion == "5":
                print("Digite numero de documento del empleado para ver información ")
                empleado = input("")
            
            
            else:
                print("\n Por favor elija una opcion valida")


def main():
    principal = Principal()  # creamos instancia de la clase
    principal.menu()


if __name__ == "__main__":  # Cuando se ejecuta el programa inicia como el
    main()
