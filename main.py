import csv
import os  # verifica si el archivo existia
import operator

class BusquedaEmpleado:
    def __init__(self):#se inicializan en cada instancia
        self.Termino = ""  #atributos de clase
        self.Documento = ""
        self.Viajes = []
        self.campos_clientes = []
        self.campos_viajes = []
        self.Datos_empleado = []


class Principal:  # creo una clase
    def __init__(self):  # inicializo atributos
        self.csv_cliente = ""
        self.csv_viajes = ""  
        self.archivo_log = ""
        self.opcion_menu = {
                    1: "Configuración archivos",
                    2: "Buscar cliente",
                    3: "Ver usuarios por empresa",
                    4: "Total de Ventas de viajes por nombre de empresa",
                    5: "Información por empleado",
                    6: "Salir "
                }
    def valida_no_existe(self, archivo):
        while not os.path.exists(archivo):
            archivo = input(
                "\n El archivo no se encuentra? Ingresarlo nuevamente ")
    
    def buscar_archivos(self):
        archivo_cliente = input("Ingrese el nombre del archivo donde se encuentran los clientes ")
        self.valida_no_existe(archivo_cliente) 
        self.csv_cliente = archivo_cliente

        archivo_viajes = input("Ingrese el archivo donde desea buscar el total de viajes ")
        self.valida_no_existe(archivo_viajes) 
        self.csv_viajes = archivo_viajes

        nomb_log = input("Ingrese el nombre del archivo donde se guardará el .log ")
        while len(nomb_log) == 0 and ".log" not in nomb_log:
            nomb_log = input("El nombre del archivo no es valido. Ingrese el nombre del archivo donde se guardará el .log ")
        self.archivo_log = nomb_log

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
                    if cliente.lower() in line["Nombre"].lower():
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
             
                for linea in Clientes_csv:
                    # print(linea)
                    if empresa.lower() in linea["Empresa"].lower():
                        Empresa = linea["Empresa"]
                        Lista_doct.append(linea["Documento"])
             
                for linea in Viajes_csv:
                    if linea["Documento"] in  Lista_doct:
                        Total_ventas = float(linea["monto"].replace(",","")) + Total_ventas#La , se reem x nada
            
        except IOError:
            print("\n Ocurrrio un error en el archivo  ") 
        
        self.formato() 
        print(f"Empresa: {Empresa}  ${Total_ventas:0.2f}")
        self.formato() 

    def Buscar_empleado(self, dni):
        resultado = BusquedaEmpleado() #instancia de clase
        resultado.Termino = dni #atributo
        try:
            ## apareo
            with open(self.csv_cliente, 'r',  newline='', encoding='UTF-8') as f_clientes, \
                open(self.csv_viajes, 'r',  newline='', encoding='UTF-8') as f_viajes:

                clientes_csv = csv.reader(f_clientes)
                viajes_csv = csv.reader(f_viajes)

                cl = csv.DictReader(f_clientes)
                vi = csv.DictReader(f_viajes)

                #se guardan campos enla clase resultado
                resultado.campos_clientes = cl.fieldnames
                resultado.campos_viajes = vi.fieldnames

 
                # Empieza a leer
                cliente = next(clientes_csv, None)
                viaje = next(viajes_csv, None)
                while (cliente):
                    # print("{}, {} ({})".format(cliente[1], cliente[2], cliente[0]))
                    
                    if int(dni) == int(cliente[2]):
                        resultado.Documento = cliente[2]
                        resultado.Datos_empleado = cliente
                    
                    while(viaje): #leo linea y accedo si esta el doct verific q sea igual al q me solicitaron
                        if int(dni) == int(viaje[0]):
                            resultado.Viajes.append(viaje)#atributo viaje
                        viaje = next(viajes_csv, None)
                    cliente = next(clientes_csv, None)
                
                  
        except IOError:
            print("\n Ocurrrio un error en el archivo  ")
     
        return resultado

    def print_resultado(self, resultado):
        self.formato() 
        print(f"Documento: {resultado.Documento}")
        self.formato() 
        print(resultado.campos_clientes)
        print(resultado.Datos_empleado)
        self.formato()
        print(f"Total viajes: {len(resultado.Viajes)}, Monto: {sum([float(viaje[2].replace(',','')) for viaje in resultado.Viajes]):0.2f}") #for de manera comprensiva 
        self.formato()
        print(resultado.campos_viajes)
        for lista in resultado.Viajes: #datos de la persona o cliente
            print( lista)

    def Buscar_registros(self, Campo, Valor_buscar):
        pass


    def formato(self):
        print( "-" * os.get_terminal_size()[0])
    
    def consultas_log(self, texto):
        if ( self.archivo_log != ""):
            try:
                with open(self.archivo_log, 'a',  newline='', encoding='UTF-8') as file:
                    file.write(texto + "\n")#guarda la opcion del menu
                
            except IOError:
                print("\n Ocurrrio un error en el archivo  ")
    

        
    def menu(self):
        while True:
            
            print("\nMenú Usuario")
            for clave, valor in self.opcion_menu.items():
                print(f"{clave}. {valor}")

            opcion = input("Elija una opción: ")
            
            if opcion.isnumeric() and opcion in self.opcion_menu.keys():#verificamos que es numerico
                self.consultas_log(self.opcion_menu[int(opcion)])

            if opcion == "6":
                print("bye bye")
                exit()

            if opcion == "1":
                self.buscar_archivos()
            
            if self.csv_cliente == "" or self.csv_viajes == "" or self.archivo_log == "":
                print("Ir a la configuracion opción 1")

            

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
                while not dni.isnumeric():
                    print("No es valido. Digite numero de documento del empleado para ver información ")
                    dni = input("")
                    
                resultado = self.Buscar_empleado(dni)
                self.print_resultado(resultado)
            
            
            elif opcion not in ["6","1"]:
                print("\n Por favor elija una opcion valida")
           


def main():
    principal = Principal()  # creamos instancia de la clase
    principal.menu()


if __name__ == "__main__":  # Cuando se ejecuta el programa inicia como el
    main()
