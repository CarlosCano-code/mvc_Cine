from model.model import Model

class View:
    # A view for a agenda DB
    def __init__(self):
        self.model = Model()
    def start(self):
        print('********************')
        print('*BIENVENIDO AL CINE*')
        print('********************')

    def end(self):
        print('******************')
        print('* Hasta la vista *')
        print('******************')

    def menu(self):
        print('****************')
        print('*     MENU     *')
        print('****************')
        print('1. Ingresar como Administrador')
        print('2. Ingresar como visitante')
        print('3. Salir')

    def option(self, last):
        print('Seleccione una opción (1-'+last+'): ', end='')

    def not_void_option(self):
        print('¡Opción no valida\nIntente de nuevo¡')

    def ask(self, output):
        print(output, end='')

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def error(self, err):
        print(' ¡ERROR! '.center(len(err)+4, '-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))
    #--------------------------Vista de Cine Usuario------------------------#
    def cineMenuAdmin(self):
        print('************************')
        print('* -- Submenu Admin-- *')
        print('************************')
        print('1. Operaciones de Control de personal')
        print('2. Operaciones de Control de salas')
        print('3. Operaciones de Control de idiomas')
        print('4. Operaciones de Control de peliculas')
        print('5. Operaciones de Control de fechas.')
        print('6. Operaciones de Control de funciones')
        print('7. Operaciones de Control y Venta de boletos')
        print('8. Regresar.')

    def subMenuBoletos(self):
        print('************************')
        print('* -- Submenu Boletos-- *')
        print('************************')
        print('1. Vender boleto.')
        print('2. Actualizar boleto.')
        print('3. Eliminar un boleto.')
        print('4. Buscar un boleto por ID del dueño.')
        print('5. Mostrar boletos vendidos para una función.')           
        print('6. Mostrar todos los boletos.')
        print('7. Salir')

    def subMenuFunciones(self):
        print('************************')
        print('* -- Submenu Funciones-- *')
        print('************************')
        print('1. Agregar una funcion nueva.')
        print('2. Actualizar una funcion.')
        print('3. Eliminar una funcion.')
        print('4. Buscar una funcion por ID.')
        print('5. Buscar funcion por fecha.')
        print('6. Buscar funcion por sala.')   
        print('7. Buscar funcion por hora.')    
        print('8. Mostrar funciones de una pelicula.')           
        print('9. Mostrar todas las funciones.')
        print('0. Salir')

    def subMenuIdiomas(self):
        print('************************')
        print('* -- Submenu Idioma-- *')
        print('************************')
        print('1. Agregar un idioma nuevo.')
        print('2. Actualizar un idioma.')
        print('3. Eliminar un idioma.')
        print('4. Buscar un idioma por ID.')
        print('5. Buscar idioma por su nombre.')            
        print('6. Mostrar todas los idiomas.')
        print('7. Salir')
    
    def subMenuFechas(self):
        print('************************')
        print('* -- Submenu Idioma-- *')
        print('************************')
        print('1. Agregar una fecha nueva.')
        print('2. Actualizar una fecha.')
        print('3. Eliminar una fecha.')
        print('4. Buscar una fecha por ID.')
        print('5. Buscar fecha.')            
        print('6. Mostrar todas las fechas.')
        print('7. Salir')

    def subMenuPeliculas(self):
        print('*********************************')
        print('* -- Submenu Control de Peliculas-- *')
        print('*********************************')
        print('1. Agregar una pelicula nueva.')
        print('2. Actualizar una pelicula.')
        print('3. Eliminar una pelicula.')
        print('4. Buscar una pelicula por titulo.')
        print('5. Buscar peliculas por su clasificacion.')            
        print('6. Buscar peliculas por su ID.')
        print('7. Mostrar todas las peliculas del mismo idioma.')
        print('8. Mostrar todas las peliculas.')
        print('9. Salir')

    def subMenuSalas(self):
        print('*********************************')
        print('* -- Submenu Control Personal-- *')
        print('*********************************')
        print('1. Agregar una sala nueva.')
        print('2. Actualizar una sala.')
        print('3. Eliminar una sala.')
        print('4. Buscar una sala por id.')
        print('5. Buscar salas por su tipo.')            
        print('6. Mostrar todas las salas.')
        print('7. Salir')

# MOSTRAR SALAS
    def mostrarSala(self, record):
        print('|ID SALA|\t|***Tipos***|\t|Filas|\t |Columnas|\t')
        print('  ', record[0], '\t'*2, record[1], '\t'*2, record[2],
            '\t   ', record[3])

    def subMenuPersonal(self):
        print('*********************************')
        print('* -- Submenu Control Personal-- *')
        print('*********************************')
        print('1. Agregar un nuevo usuario.')
        print('2. Eliminar un usuario.')
        print('3. Actualizar un usuario.')
        print('4. Buscar un usuario')
        print('5. Mostrar todos los usuarios.')
        print('6. Salir')

    def buscarUsers(self):
        print('*********************************')
        print('* -- Submenu Buscar-- *')
        print('*********************************')
        print('1. Buscar por ID.')
        print('2. Buscar por nombre.')
        print('3. Buscar por apellidos.')
        print('4. Regresar')
    #--------------------------Vista de Cine Usuario------------------------#

    def cineMenuUser(self):
        print('************************')
        print('* -- Submenu Usuario-- *')
        print('************************')
        print('1. Registrarse(¡Crea tu usuario antes de comprar un boleto!)')
        print('2. Mostrar funciones')
        print('3. Comprar boleto')
        print('4. Regresar.')

    def showUser(self, record):
        print('ID del usuario: ', record[0])
        print('Nombre: ', record[1])
        print('Apellido 1: ', record[2])
        print('Apellido 2: : ', record[3])

    def showHeader(self, header):
        print(header.center(53, '*'))
        print('-'*53)

    def showMidder(self):
        print('-'*53)

    def showFooter(self):
        print('*'*53)

# Mostrar funciones

    def showFunciones(self, record):
        print('|Funcion|\t |Nombre de la Pelicula|\t |Idioma|\t |Clasificacion|\t|Duracion|\t|Sala|')
        print('\t', record[0], '\t', record[1], '\t\t', record[2],
            '\t\t', record[3], '\t'*2, record[4], '\t', record[5])

    def showHeaderFunc(self, header):
        print(header.center(120, '*'))
        print('-'*120)

    def showMidderFunc(self):
        print('-'*120)

    def showFooterFunc(self):
        print('*'*120, '\n')

    """
    SHOW BOLETO
    """
    def showBoletos(self, record):
        print('|Nro.Boleto| \t |Asiento|\t |Nombre|\t |Sala|\t |Pelicula|\t |Fecha de funcion|\t |Hora de funcion| ')
        print('\t',record[0],'\t'*2,record[1],'\t',record[2]+record[3],'\t',record[4],'\t',record[5],'\t',record[6],'\t',record[7])

    def showBoleto(self, record):
        print('Tu numero de boleto:\t', record[0])
        print('Tu asiento es el:   \t', record[1])
        print('A nombre de:        \t', record[2]+' '+record[3])
        print('La sala es:         \t', record[4])
        print('Tu pelicula         \t', record[5])
        print('Fecha de la funcion:\t', record[6])
        print('Hora de la funcion: \t', record[7])

    def showBoletoV(self, record):
        print('Tu numero de boleto:\t', record[0])
        print('Tu asiento es el:   \t', record[1])
        print('Vendido por:        \t', record[2] +' '+ record[3])
        print('La sala es:         \t', record[4])
        print('Tu pelicula         \t', record[5])
        print('Fecha de la funcion:\t', record[6])
        print('Hora de la funcion: \t', record[7])

#Mostrar idiomas
    def showIdioma(self, record):
        print('|ID Idioma|\t|***IDIOMA***|')
        print('  ', record[0], '\t'*2, record[1])

    def showPelicula(self, record):
        print('|ID|\t |Nombre de la Pelicula|\t |Idioma|\t |Clasificacion|\t|Sipnosis|\t|Duracion|')
        print(record[0], '\t', record[1], '\t\t', record[2],
            '\t\t', record[3], '\t'*2, record[4], '\t', record[5],)
    
    def showFecha(self, record):
        print('|ID Fecha|\t|***Fecha***|')
        print('  ', record[0], '\t'*2, record[1])