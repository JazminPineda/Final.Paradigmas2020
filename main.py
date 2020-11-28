import csv
import os  # verifica si el archivo existia
import operator


class BusquedaEmpleado:
    self.Termino = ""
    self.Campos = []
    self.Documento = ""
    self.Viajes = []
    

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
        Total_ventas = 0
        Empresa = ""
        try:
            ## apareo
            with open(self.csv_cliente, 'r',  newline='', encoding='UTF-8') as f_clientes, \
                open(self.csv_viajes, 'r',  newline='', encoding='UTF-8') as f_viajes:
                # atributo de la clase
                Clientes_csv = csv.DictReader(f_clientes)
                Viajes_csv = csv.DictReader(f_viajes)
                print(Clientes_csv)
                for linea in Clientes_csv:
                    # print(linea)
                    if empresa.lower() in linea["Empresa"].lower():
                        Empresa = linea["Empresa"]
                        Lista_doct.append(linea["Documento"])
                print(Lista_doct)
                for linea in Viajes_csv:
                    if linea["Documento"] in  Lista_doct:
                        Total_ventas = float(linea["monto"].replace(",","")) + Total_ventas#La , se reem x nada
            
        except IOError:
            print("\n Ocurrrio un error en el archivo  ") 
        
        print( "-" * os.get_terminal_size()[0])
        print(f"Empresa: {Empresa}  ${Total_ventas:0.2f}")
        print( "-" * os.get_terminal_size()[0])

    def Buscar_empleado(self, dni):
        
         try:
            ## apareo
            with open(self.csv_cliente, 'r',  newline='', encoding='UTF-8') as f_clientes, \
                open(self.csv_viajes, 'r',  newline='', encoding='UTF-8') as f_viajes:

                clientes_csv = csv.reader(f_clientes)
                viajes_csv = csv.reader(f_viajes)

                # Saltea los encabezados
                next(clientes_csv)
                next(viajes_csv)

                # Empieza a leer
                cliente = next(clientes_csv, None)
                viaje = next(viajes_csv, None)
                while (cliente):
                    print("{}, {} ({})".format(cliente[1], cliente[2], cliente[0]))
                    if (not viaje or viaje[0] != cliente[0]):
                        print("\tNo se registran viajes")
                    while (viaje and viaje[0] == cliente[0]):
                        print("\t{}: {}".format(viaje[1], viaje[2]))
                        viaje = next(viajes_csv, None)
                    cliente = next(clientes_a, None)

                # Cierro los archivos
                clientes_a.close()
                viajes_a.close()

    def Buscar_registros(self, Campo, Valor_buscar):
        pass


    def formato(self):
        print( "-" * os.get_terminal_size()[0])
   

    

        
    def menu(self):
        while True:
            print("\nMenú Usuario \nElija una opción: "
                  "\n 1. Ingresar nombre de los archivos donde se encuentran los datos "
                  "\n 2. Buscar cliente"
                  "\n 3. Ver usuarios por empresa"
                  "\n 4. Total de Ventas de viajes por nombre de empresa"
                  "\n 5. Información por empleado"
                  "\n 6. Salir ")

            opcion = input("")

            if opcion == "6":
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
                dni = input("")
                self.Buscar_empleado(dni)
            else:
                print("\n Por favor elija una opcion valida")


def main():
    principal = Principal()  # creamos instancia de la clase
    principal.menu()


if __name__ == "__main__":  # Cuando se ejecuta el programa inicia como el
    main()
