from model.model import Model
from view.view import View
import string as s


class Controller:
    # A controller for agenda DB
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.main_menu()

#------------------------Controlador general----------------------#
    def main_menu(self):
        o = '0'
        while o != '3':
            self.view.menu()
            self.view.option('3')

            o = input()
            if o == '1':
                self.admi_Menu()
            elif o == '2':
                self.user_Menu()
            elif o == '3':
                return
            else:
                self.view.not_void_option()
        return

    def update_list(self, fs, vs):
        fields = []
        vals = []

        for f, v in zip(fs, vs):
            if v != '':
                fields.append(f + ' = %s')
                vals.append(v)

        return fields, vals
# Controlador cine Admin

    def admi_Menu(self):
        o = '0'
        while o != '9':
            self.view.cineMenuAdmin()
            self.view.option('9')
            o = input()
            if o == '1':
                self.menu_controlPersonal()
            elif o == '2':
                self.menu_controlSalas()
            elif o == '3':
                self.menu_controlIdioma()
            elif o == '4':
                self.menu_controlPeliculas()
            elif o == '5':
                self.menuControlFechas()
            elif o == '6':
                self.menu_controlFunciones()
            elif o == '7':
                self.menu_Boletos()
            elif o == '8':
                return
            else:
                self.view.not_void_option()
        return

# Menu y control boletos.
    def menu_Boletos(self):
        o = '0'
        while o != '7':
            self.view.subMenuBoletos()
            self.view.option('7')
            o = input()
            if o == '1':
                self.venderBoleto()
            elif o == '2':
                self.actualizarBoleto()
            elif o == '3':
                self.eliminarBoleto()
            elif o == '4':
                self.boletoID()
            elif o == '5':
                self.boletoFunID()
            elif o == '6':
                self.mostrarTodosBoletos()
            elif o == '7':
                return
            else:
                self.view.not_void_option()
                return
        return

    def actualizarBoleto(self):
        boletos = self.model.leerBoletos()
        self.view.showHeader('Lista de Boletos')
        for boleto in boletos:
            self.view.showBoletos(boleto)
            self.view.showMidder()
        self.view.showFooter()
        self.view.ask(
            'Selecciona el ID del boleto que deseas actualizar: ')
        bolID = input()
        boleto = self.model.leerBoletoId(bolID)
        if type(boleto) == tuple:
            self.view.showHeader(
                'Usted ha seleccionado el boleto numero ' + bolID + ' ')
        else:
            if boleto == None:
                self.view.error('El boleto no existe.')
            else:
                self.view.error('Problema al leer el boleto.')
            return
        self.view.msg(
            'Ingresa valores.(presione enter para dejar el campo como estaba.)')
        self.showFunciones()
        self.view.msg('Que funcion deseas asistir?; ')
        idFunc = input()
        self.view.msg('Selecciona tu sala: ')
        idSala = input()
        print('\n')
        asiento = self.model.asientosFromSala(idFunc, idSala)

        fila = asiento[1]
        columna = asiento[2]

        sala = []
        for i in range(fila):
            asientos = []
            for j in range(columna):
                nasiento = []
                nasiento.append(s.ascii_lowercase[i])
                nasiento.append(str(j))
                acreado = ''.join(nasiento)
                asientos.append(acreado)
            sala.append(asientos)

        seatSelected = self.model.leerBoletoIdFunc(idFunc)
        seatsOcupped = []
        for seat in seatSelected:
            seatsOcupped.append(seat[2])

        if seatsOcupped != None:
            for fila in sala:
                for seat in seatsOcupped:
                    if seat in fila:
                        indx = fila.index(seat)
                        fila[indx] = 'X'
                print(fila)
        else:
            for fila in sala:
                print(fila)

        self.view.msg('Elige tu asiento nuevo: ')
        seat = input()
        whole_vals = [idFunc, seat]
        fields, vals = self.update_list(
            ['funcionID', 'asiento'], whole_vals)
        vals.append(bolID)
        vals = tuple(vals)

        out = self.model.updateBoleto(fields, vals)

        if out == True:
            self.view.ok(bolID, 'Boleto Actualizado')
        else:
            self.view.error('No se pudo actualizar el boleto.')
        return

    def eliminarBoleto(self):
        boletos = self.model.leerBoletos()
        self.view.showHeader('Lista de Boletos')
        for boleto in boletos:
            self.view.showBoletos(boleto)
            self.view.showMidder()
        self.view.showFooter()
        self.view.ask(
            'Selecciona el ID del boleto que deseas actualizar: ')
        bolID = input()
        out =  self.model.deleteBoleto(bolID)
        if out == True:
            self.view.msg('Boleto eliminado correctamente-')
        else:
            self.view.msg('El boleto no existe.')

    def boletoID(self):
        self.mostrarTodosUsuarios()
        self.view.ask(
            'Selecciona el ID del usuario que es dueño del boleto: ')
        usID = input()
        boletos = self.model.leerBoletoIdUs(usID)
        print(type(boletos))
        if type(boletos) == list:
            self.view.showHeader('Lista boletos')
            for boleto in boletos:
                self.view.showBoletos(boleto)
                self.view.showMidder()
            self.view.showFooter()
        else:
            self.view.msg('Boletos no encontrados')


    def boletoFunID(self):
        self.showFunciones()
        self.view.ask(
            'Selecciona el ID de la funcion que deseas ver los boletos: ')
        funID = input()
        boletos = self.model.leerBoletoIdFunc(funID)
        if type(boletos) == list:
            self.view.showHeader('Lista boletos')
            for boleto in boletos:
                self.view.showBoletos(boleto)
                self.view.showMidder()
            self.view.showFooter()
        else:
            self.view.msg('Boletos no encontrados')
    
    def mostrarTodosBoletos(self):
        boletos = self.model.leerBoletos()
        self.view.showHeader('Lista de Boletos')
        for boleto in boletos:
            self.view.showBoletos(boleto)
            self.view.showMidder()
        self.view.showFooter()
# Menu y control de funciones:
    def menu_controlFunciones(self):
        o = '0'
        while o != '9':
            self.view.subMenuFunciones()
            self.view.option('9')
            o = input()
            if o == '1':
                self.crearFuncion()
            elif o == '2':
                self.actualizarFuncion()
            elif o == '3':
                self.eliminarFuncion()
            elif o == '4':
                self.buscarFunId()
            elif o == '5':
                self.buscarFunFecha()
            elif o == '6':
                self.buscarFunSala()
            elif o == '7':
                self.buscarFunHora()
            elif o == '8':
                self.buscarFunPelicula()
            elif o == '9':
                self.showFunciones()
            else:
                self.view.not_void_option()
        return

    def ask_Funcion(self):
        peliculas = self.model.leerPeliculas()
        if type(peliculas) == list:
            self.view.showHeader('Lista de Peliculas')
            for pelicula in peliculas:
                self.view.showPelicula(pelicula)
                self.view.showMidder()
            self.view.showFooter()
        self.view.ask(
            '¿Que pelicula se proyectara en esta funcion?(Ingrese el ID de la pelicula): ')
        peliID = input()
        salas = self.model.leerSalas()
        self.view.showHeader('Lista de salas')
        for sala in salas:
            self.view.mostrarSala(sala)
            self.view.showMidder()
        self.view.showFooter()
        self.view.ask(
            '¿Que sala proyectara esta funcion?(Ingrese el ID de la sala): ')
        salaID = input()
        fechas = self.model.leerFechas()
        self.view.showHeader('Lista de fechas')
        for fecha in fechas:
            self.view.showFecha(fecha)
            self.view.showMidder()
        self.view.showFooter()
        self.view.ask(
            '¿En que fecha se proyectara esta funcion?(Ingrese el ID de la fecha): ')
        fechaID = input()
        self.view.ask('¿En que hora se proyectara esta funcion?: ')
        hora = input()
        return [peliID, salaID, fechaID, hora]

    def crearFuncion(self):
        peliID, salaID, fechaID, hora = self.ask_Funcion()
        out = self.model.crearFuncion(peliID, salaID, fechaID, hora)
        if out == True:
            self.view.msg('La funcion se ha añadidio exitosamente!')
        else:
            self.view.msg('La funcion no se ha podido agregar.')

    def actualizarFuncion(self):
        funciones = self.model.leerFunciones()
        self.view.showHeaderFunc('Lista de Funciones')
        for funcion in funciones:
            self.view.showFunciones(funcion)
            self.view.showMidderFunc()
        self.view.showFooterFunc()
        self.view.ask(
            'Selecciona el ID de la funcion que deseas actualizar: ')
        funID = input()
        funcion = self.model.leerFuncionId(funID)
        print(funcion)
        if type(funcion) == tuple:
            self.view.showHeader(
                'Usted ha seleccionado la funcion numero ' + funID + ' ')
        else:
            if funcion == None:
                self.view.error('La funcion no existe.')
            else:
                self.view.error('Problema al leer la funcion')
            return
        self.view.msg(
            'Ingresa valores.(presione enter para dejar el campo como estaba.)')
        whole_vals = self.ask_Funcion()
        fields, vals = self.update_list(
            ['peliculaID', 'salaID', 'fechaID', 'hora'], whole_vals)
        vals.append(funID)
        vals = tuple(vals)

        out = self.model.updateFuncion(fields, vals)

        if out == True:
            self.view.ok(funID, 'Funcion Actualizada')
        else:
            self.view.error('No se pudo actualizar la Funcion.')
        return

    def eliminarFuncion(self):
        funciones = self.model.leerFunciones()
        self.view.showHeaderFunc('Lista de Funciones')
        for funcion in funciones:
            self.view.showFunciones(funcion)
            self.view.showMidderFunc()
        self.view.showFooterFunc()
        self.view.ask(
            '¿Que pelicula desea eliminar?(Inserte el ID de la funcion): ')
        funID = input()
        out = self.model.deleteFuncion(funID)
        if out == True:
            self.view.ok(funID, 'ha sido eliminado correctamente')
        else:
            self.view.msg('La funcion no existe!')

    def buscarFunId(self):
        self.view.ask('Introduce el ID de la funcion: ')
        funID = input()
        funcion = self.model.leerFuncionId(funID)
        self.view.showFunciones(funcion)

    def buscarFunFecha(self):
        self.mostrarFechas()
        self.view.ask(
            '¿Que fecha deseas buscar?(Introduce el id de la fecha): ')
        idFecha = input()
        funciones = self.model.leerFuncionFechaId(idFecha)
        if type(funciones) == list:
            self.view.showHeaderFunc('Lista de Funciones')
            for funcion in funciones:
                self.view.showFunciones(funcion)
                self.view.showMidderFunc()
            self.view.showFooterFunc()
        else:
            self.view.msg('No existe funcion para esta fecha.')

    def buscarFunSala(self):
        self.mostrarSalas()
        self.view.ask('¿Que sala deseas buscar?(Introduce el id de la sala): ')
        idSala = input()
        funciones = self.model.leerFuncionSalaId(idSala)
        if type(funciones) == list:
            self.view.showHeaderFunc('Lista de Funciones')
            for funcion in funciones:
                self.view.showFunciones(funcion)
                self.view.showMidderFunc()
            self.view.showFooterFunc()
        else:
            self.view.msg('No existe funcion para esta sala.')

    def buscarFunHora(self):
        self.view.ask(
            '¿Que hora deseas buscar?(Introduce la hora en formato de 12hrs)')
        hora = input()
        funciones = self.model.leerFuncionHora(hora)
        if type(funciones) == list:
            self.view.showHeaderFunc('Lista de Funciones')
            for funcion in funciones:
                self.view.showFunciones(funcion)
                self.view.showMidderFunc()
            self.view.showFooterFunc()
        else:
            self.view.msg('No existen funciones a esta hora.')

    def buscarFunPelicula(self):
        self.mostrarPeliculas()
        self.view.ask(
            '¿Que pelicula deseas buscar en las funciones?(Introduce el ID de la pelicula): ')
        idPel = input()
        funciones = self.model.leerFuncionPeliculaId(idPel)
        if type(funciones) == list:
            self.view.showHeaderFunc('Lista de Funciones')
            for funcion in funciones:
                self.view.showFunciones(funcion)
                self.view.showMidderFunc()
            self.view.showFooterFunc()
        else:
            self.view.msg('No existen funciones para esta pelicula.')

# Menu y control de fechas:
    def menuControlFechas(self):
        o = '0'
        while o != '7':
            self.view.subMenuFechas()
            self.view.option('7')
            o = input()
            if o == '1':
                self.crearfecha()
            elif o == '2':
                self.actualizarFecha()
            elif o == '3':
                self.eliminarFecha()
            elif o == '4':
                self.buscarFechaId()
            elif o == '5':
                self.buscarFecha()
            elif o == '6':
                self.mostrarFechas()
            elif o == '7':
                return
            else:
                self.view.not_void_option()
        return

    def crearfecha(self):
        self.view.ask('¿Que fecha deseas agregar?(AAAA-MM-DD): ')
        fecha = input()
        out = self.model.crearFecha(fecha)
        if out == True:
            self.view.msg('Fecha creada correctamente!')
        else:
            self.view.msg('La fecha no se pudo agregar.')

    def actualizarFecha(self):
        fechas = self.model.leerFechas()
        self.view.showHeader('Lista de fechas')
        for fecha in fechas:
            self.view.showFecha(fecha)
        self.view.msg(
            '¿Que fecha desea actualizar?(Inserte el ID de la fecha): ')
        idFecha = input()
        self.view.msg('¿Que fecha desea que sea ahora?(AAAA-MM-DD): ')
        fecha = input()
        out = self.model.updateFecha(idFecha, fecha)
        if out == True:
            self.view.msg('Fecha actualizada correctamente!')
        else:
            self.view.msg('La fecha no se pudo actualizar.')

    def eliminarFecha(self):
        fechas = self.model.leerFechas()
        self.view.showHeader('Lista de fechas')
        for fecha in fechas:
            self.view.showFecha(fecha)
        self.view.showFooter()
        self.view.msg(
            '¿Que fecha desea eliminar?(Inserte el ID de la fecha): ')
        idFecha = input()
        out = self.model.deleteFecha(idFecha)
        if out == True:
            self.view.msg('Fecha Eliminada correctamente!')
        else:
            self.view.msg('La fecha no existe.')

    def buscarFechaId(self):
        self.view.ask('Introduce el ID de la fecha: ')
        fechaID = input()
        fecha = self.model.leerFechaId(fechaID)
        self.view.showFecha(fecha)

    def buscarFecha(self):
        self.view.ask('Introduce la fecha (aaaa-mm--dd): ')
        fecha = input()
        out = self.model.leerFecha(fecha)
        if type(out) == tuple:
            self.view.showFecha(out)
        else:
            self.view.msg('No se pudo encontrar la fecha.')

    def mostrarFechas(self):
        fechas = self.model.leerFechas()
        self.view.showHeader('Lista de fechas')
        for fecha in fechas:
            self.view.showFecha(fecha)
            self.view.showMidder()
        self.view.showFooter()

# Menu y control de idiomas.

    def menu_controlIdioma(self):
        o = '0'
        while o != '7':
            self.view.subMenuIdiomas()
            self.view.option('7')
            o = input()
            if o == '1':
                self.crearIdioma()
            elif o == '2':
                self.actualizarIdioma()
            elif o == '3':
                self.eliminarIdioma()
            elif o == '4':
                self.buscarIdiomaId()
            elif o == '5':
                self.buscarIdioma()
            elif o == '6':
                self.mostrarIdiomas()
            elif o == '7':
                return
            else:
                self.view.not_void_option()
        return

    def crearIdioma(self):
        self.view.ask('¿Que idioma deseas crear?: ')
        idioma = input()
        out = self.model.crearIdioma(idioma)
        if out == True:
            self.view.msg('Idioma creado con exito!')
        else:
            self.view.msg('No se pudo crear el idioma.')

    def actualizarIdioma(self):
        idiomas = self.model.leerIdiomas()
        self.view.showHeader('Lista de idiomas')
        for idioma in idiomas:
            self.view.showIdioma(idioma)
            self.view.showMidder()
        self.view.showFooter()
        self.view.ask(
            '¿Que idioma te interesa actualizar?(Introduce el ID del idioma): ')
        idiomaID = input()
        self.view.ask('¿Ahora que idioma quieres que sea?: ')
        descr = input()
        out = self.model.updateIdioma(idiomaID, descr)
        if out == True:
            self.view.ok(idiomaID, 'Idioma Actualizado')
        else:
            self.view.error('No se pudo actualizar el idioma.')
        return

    def eliminarIdioma(self):
        idiomas = self.model.leerIdiomas()
        self.view.showHeader('Lista de idiomas')
        for idioma in idiomas:
            self.view.showIdioma(idioma)
            self.view.showMidder()
        self.view.showFooter()
        self.view.ask(
            '¿Que idioma te interesa eliminar?(Introduce el ID del idioma): ')
        idiomaID = input()
        out = self.model.deleteIdioma(idiomaID)
        if out == True:
            self.view.msg('Idioma eliminado correctamente.')
        else:
            self.view.msg('El idioma no existe.')

    def buscarIdiomaId(self):
        self.view.ask('Introduce el ID del idioma: ')
        idiomaID = input()
        idioma = self.model.leerIdiomaId(idiomaID)
        self.view.showIdioma(idioma)

    def buscarIdioma(self):
        self.view.ask('Introduce el idioma: ')
        idioma = input()
        out = self.model.leerIdioma(idioma)
        if type(out) == tuple:
            self.view.showIdioma(out)
        else:
            self.view.msg('No se pudo encontrar el idioma.')

    def mostrarIdiomas(self):
        idiomas = self.model.leerIdiomas()
        self.view.showHeader('Lista de idiomas')
        for idioma in idiomas:
            self.view.showIdioma(idioma)
            self.view.showMidder()
        self.view.showFooter()

# Menu Peliculas
    def menu_controlPeliculas(self):
        o = '0'
        while o != '9':
            self.view.subMenuPeliculas()
            self.view.option('9')
            o = input()
            if o == '1':
                self.createPelicula()
            elif o == '2':
                self.actualizarPelicula()
            elif o == '3':
                self.eliminarPelicula()
            elif o == '4':
                self.buscarPeliculaN()
            elif o == '5':
                self.buscarPeliculaC()
            elif o == '6':
                self.buscarPeliculaId()
            elif o == '7':
                self.buscarPeliculaIdioma()
            elif o == '8':
                self.mostrarPeliculas()
            elif o == '9':
                return
            else:
                self.view.not_void_option()
        return

# CONTROLADORES PARA PELICULAS
    def askPelicula(self):
        self.view.ask('Nombre: ')
        nombrePelicula = input()
        self.view.ask('Clasificación: ')
        clasificacion = input()
        self.view.ask('Sipnosis: ')
        sipnosis = input()
        self.view.ask('Duración: ')
        duracion = input()
        idiomas = self.model.leerIdiomas()
        self.view.showHeader('Lista de idiomas')
        for idioma in idiomas:
            self.view.showIdioma(idioma)
            self.view.showMidder()
        self.view.showFooter()
        self.view.ask('Selecciona el ID del idioma de la pelicula: ')
        idiom = input()
        return [idiom, nombrePelicula, clasificacion, sipnosis, duracion]

    def createPelicula(self):
        idiom, nombrePelicula, clasificacion, sipnosis, duracion = self.askPelicula()
        out = self.model.crearPelicula(
            idiom, nombrePelicula, clasificacion, sipnosis, duracion)
        if out == True:
            self.view.ok('El usuario '+nombrePelicula + ' se ha ', 'agregado')
        else:
            self.view.error('No se ha podido agregar la pelicula!!')
            return

    def actualizarPelicula(self):
        peliculas = self.model.leerPeliculas()
        self.view.showHeader('Lista de Peliculas')
        for pelicula in peliculas:
            self.view.showPelicula(pelicula)
            self.view.showMidder()
        self.view.showFooter()
        self.view.ask(
            'Selecciona el ID de la pelicula que deseas actualizar: ')
        peliID = input()
        pelicula = self.model.leerPeliculaId(peliID)
        if type(pelicula) == tuple:
            self.view.showHeader(
                'Usted ha seleccionado la pelicula numero ' + peliID + ' ')
        else:
            if pelicula == None:
                self.view.error('La pelicula no existe.')
            else:
                self.view.error('Problema al leer la pelicula')
            return
        self.view.msg(
            'Ingresa valores.(presione enter para dejar el campo como estaba.)')
        whole_vals = self.askPelicula()
        fields, vals = self.update_list(
            ['idiomaID', 'nombrePelicula', 'clasificacion', 'sipnosis', 'duracion'], whole_vals)
        vals.append(peliID)
        print(vals)
        vals = tuple(vals)

        out = self.model.updatePelicula(fields, vals)

        if out == True:
            self.view.ok(peliID, 'Pelicula Actualizada')
        else:
            self.view.error('No se pudo actualizar la pelicula.')
        return

    def buscarPeliculaN(self):
        self.view.ask('¿Que pelicula deseas buscar?: ')
        peliNombre = input()
        peliculas = self.model.leerPeliculaNombre(peliNombre)
        if type(peliculas) == list:
            self.view.showHeader('Lista de Peliculas')
            for pelicula in peliculas:
                self.view.showPelicula(pelicula)
                self.view.showMidder()
            self.view.showFooter()
        else:
            self.view.msg('Peliculas no encontradas.')

    def buscarPeliculaC(self):
        self.view.ask('¿De que clasificación deseas saber las peliculas?: ')
        clasi = input()
        peliculas = self.model.leerPeliculasClasificacion(clasi)
        if type(peliculas) == list:
            self.view.showHeader('Lista de Peliculas')
            for pelicula in peliculas:
                self.view.showPelicula(pelicula)
                self.view.showMidder()
            self.view.showFooter()
        else:
            self.view.msg('Peliculas no encontradas.')

    def buscarPeliculaId(self):
        self.view.ask(
            '¿Que pelicula deseas buscar?(Inserte su ID; en caso de no saberlo use otra de nuestras opciones): ')
        peliId = input()
        pelicula = self.model.leerPeliculaId(peliId)

        self.view.showHeader('Lista de Pelicula')
        self.view.showPelicula(pelicula)
        self.view.showMidder()
        self.view.showFooter()

    def buscarPeliculaIdioma(self):
        idiomas = self.model.leerIdiomas()
        self.view.showHeader('Lista de idiomas')
        for idioma in idiomas:
            self.view.showIdioma(idioma)
            self.view.showMidder()
        self.view.showFooter()
        self.view.ask(
            '¿En que idioma deseas buscar las peliculas?(inserte su ID): ')
        idiomaID = input()
        peliculas = self.model.leerPeliculaIdioma(idiomaID)
        if type(peliculas) == list:
            self.view.showHeader('Lista de Peliculas')
            for pelicula in peliculas:
                self.view.showPelicula(pelicula)
                self.view.showMidder()
            self.view.showFooter()
        else:
            self.view.msg('Peliculas no encontradas.')

    def mostrarPeliculas(self):
        peliculas = self.model.leerPeliculas()
        if type(peliculas) == list:
            self.view.showHeader('Lista de Peliculas')
            for pelicula in peliculas:
                self.view.showPelicula(pelicula)
                self.view.showMidder()
            self.view.showFooter()
        else:
            self.view.msg('Peliculas no encontradas.')

    def eliminarPelicula(self):
        peliculas = self.model.leerPeliculas()
        if type(peliculas) == list:
            self.view.showHeader('Lista de Peliculas')
            for pelicula in peliculas:
                self.view.showPelicula(pelicula)
                self.view.showMidder()
            self.view.showFooter()
        else:
            self.view.msg('Peliculas no encontradas.')
        self.view.ask('¿Que pelicula deseas eliminar?(Introduzca el ID): ')
        peliID = input()
        out = self.model.deletePelicula(peliID)
        if out == True:
            self.view.ok('La pelicula numero ' + peliID, 'se ha eliminado')
        else:
            self.view.error(
                'No se ha podido eliminar la pelicula ó no existe!!')
            return

# Controlador Operaciones de salas:

    def menu_controlSalas(self):
        o = '0'
        while o != '7':
            self.view.subMenuSalas()
            self.view.option('7')
            o = input()
            if o == '1':
                self.createSala()
            elif o == '2':
                self.actualizarSala()
            elif o == '3':
                self.eliminarSala()
            elif o == '4':
                self.buscarSalaID()
            elif o == '5':
                self.buscarSalasTipo()
            elif o == '6':
                self.mostrarSalas()
            elif o == '7':
                return
            else:
                self.view.not_void_option()
        return

    def createSala(self):
        self.view.ask('¿Cuantas filas tiene la sala?(números enteros)')
        rows = input()
        self.view.ask('¿Cuantas columnas tiene la sala?(números enteros)')
        cols = input()
        self.view.ask('¿Que tipo de sala es? (iMax, 3D, Tradicional)')
        tipo = input()
        out = self.model.crearSala(rows, cols, tipo)
        if out == True:
            self.view.ok('La sala de' + tipo, 'se ha agregado')
        else:
            self.view.error('No se ha podido agregar la sala!')
            return

    def actualizarSala(self):
        salasa = self.model.leerSalas()
        for sala in salasa:
            self.view.showHeader('Lista de salas')
            self.view.mostrarSala(sala)
            self.view.showMidder()
        self.view.showFooter()
        self.view.ask('Seleccione su sala a modificar:')
        idSala = input()
        self.view.ask('Tipo de sala:')
        tipo = input()
        self.view.ask('Inserte cuantas filas tiene su sala ahora:')
        filas = input()
        self.view.ask('Inserte cuantas columnas tiene su sala ahora:')
        columnas = input()
        out = self.model.updateSala(idSala, filas, columnas, tipo)
        if out == True:
            self.view.ok('La sala numero ' + idSala, 'se ha actulizado')
        else:
            self.view.error('No se ha podido actualizar la sala!')
            return

    def eliminarSala(self):
        salas = self.model.leerSalas()
        for sala in salas:
            self.view.showHeader('Lista de salas')
            self.view.mostrarSala(sala)
            self.view.showMidder()
        self.view.showFooter()
        self.view.ask('Seleccione la sala que desea eliminar:')
        idSala = input()
        out = self.model.deleteSala(idSala)
        if out == True:
            self.view.ok('La sala numero ' + idSala, 'se ha eliminado')
        else:
            self.view.error('No se ha podido eliminar la sala!')
            return

    def buscarSalaID(self):
        self.view.ask('¿Que numero de sala deseas buscar?')
        salaID = input()
        sala = self.model.leerSalaID(salaID)
        print(sala)
        self.view.mostrarSala(sala)

    def buscarSalasTipo(self):
        self.view.ask('¿Que tipo de salas deseas buscar?')
        tipo = input()
        salaS = self.model.leerSalaTipo(tipo)
        self.view.showHeader('Lista de salas')
        for sala in salaS:
            self.view.mostrarSala(sala)
            self.view.showMidder()
        self.view.showFooter()

    def mostrarSalas(self):
        salas = self.model.leerSalas()
        self.view.showHeader('Lista de salas')

        for sala in salas:
            self.view.mostrarSala(sala)
            self.view.showMidder()
        self.view.showFooter()

# Controlador Operaciones de Empleados

    def menu_controlPersonal(self):
        o = '0'
        while o != '6':
            self.view.subMenuPersonal()
            self.view.option('6')
            o = input()
            if o == '1':
                self.createUser()
            elif o == '2':
                self.eliminarUsuario()
            elif o == '3':
                self.actualizarUsuario()
            elif o == '4':
                self.buscarUsuario()
            elif o == '5':
                self.mostrarTodosUsuarios()
            elif o == '6':
                return
            else:
                self.view.not_void_option()
        return

# Funciones menu control personal.

    def eliminarUsuario(self):
        self.mostrarTodosUsuarios()
        self.view.msg('Introduce el ID de usuario que deseas eliminar: ')
        userID = input()
        count = self.model.deleteUser(userID)
        if count != 0:
            self.view.ok(userID, ' se elimino de los usuarios.')
        else:
            if count == 0:
                self.view.error('El usuario no existe.')

    def actualizarUsuario(self):
        print('Escriba los datos del usuario que desea actualizar:\n')
        nombre, apellido1, apellido2 = self.askUsuario()
        usuario = self.model.leerUserName(nombre, apellido1, apellido2)
        self.view.showUser(usuario)
        self.view.ask('Si es el usuario que deseas modificar escribe su ID: ')
        usuarioID = input()
        if type(usuario) == tuple:
            self.view.showHeader(
                'Usted ha seleccionado el usuario numero ' + usuarioID + ' ')
        else:
            if usuario == None:
                self.view.error('El usuario no existe.')
            else:
                self.view.error('Problema al leer la el usuario')
            return

        self.view.msg(
            'Ingresa valores.(presione enter para dejar el campo como estaba.)')
        whole_vals = self.askUsuario()
        fields, vals = self.update_list(
            ['nombre', 'apellido1', 'apellido2'], whole_vals)
        vals.append(usuarioID)
        vals = tuple(vals)

        out = self.model.updateUserx(fields, vals)
        print(out)
        if out == True:
            self.view.ok(usuarioID, 'Usuario Actualizado')
        else:
            self.view.error('No se pudo actualizar el usuario.')
        return

    def buscarUsuario(self):
        o = '0'
        while o != '3':
            self.view.buscarUsers()
            self.view.option('3')
            o = input()
            if o == '1':
                userID = input('Inserta el ID del usuario que deseas buscar:')
                usuario = self.model.leerUserId(userID)
                self.view.showHeader(
                    'Usted ha seleccionado el usuario numero ' + userID + ' ')
                self.view.showMidder()
                self.view.showUser(usuario)
                self.view.showMidder()
                self.view.showFooter()
            elif o == '2':
                name = input(
                    'Escriba el nombre por el cual se filtraran los usuarios:')
                usuarios = self.model.leerUsersN(name)
                for usuario in usuarios:
                    self.view.showUser(usuario)
                    self.view.showMidder()
                self.view.showFooter()
            elif o == '3':
                apellido1 = input('Escriba el primer apellido del usuario:')
                apellido2 = input('Escriba el segundo apellido del usuario:')
                usuarios = self.model.leerUsersA(apellido1, apellido2)
                for usuario in usuarios:
                    self.view.showUser(usuario)
                    self.view.showMidder()
                self.view.showFooter()
            elif o == '4':
                return
            else:
                self.view.not_void_option()
        return

    def mostrarTodosUsuarios(self):
        usuarios = self.model.leerUsers()
        for usuario in usuarios:
            self.view.showUser(usuario)
            self.view.showMidder()
        self.view.showFooter()

# Controlador cine Usuario
    def user_Menu(self):
        o = '0'
        while o != '4':
            self.view.cineMenuUser()
            self.view.option('4')

            o = input()
            if o == '1':
                self.createUser()
            elif o == '2':
                self.showFunciones()
            elif o == '3':
                self.comprarBoleto()
            elif o == '4':
                return self.main_menu()
            else:
                self.view.not_void_option()
        return

    def askUsuario(self):
        self.view.ask('Nombre:')
        nombre = input()
        self.view.ask('Primer Apellido: ')
        flname = input()
        self.view.ask('Segundo Apellido:')
        slname = input()

        return [nombre, flname, slname]

    def createUser(self):
        nombre, flname, slname = self.askUsuario()
        out = self.model.crearUser(nombre, flname, slname)
        if out == True:
            self.view.ok('El usuario '+nombre + ' ' + flname + ' ', 'agregado')
        else:
            self.view.error('No se ha podido agregar el usuario!')
            return

    def showFunciones(self):
        funciones = self.model.leerFunciones()
        if type(funciones) == list:
            self.view.showHeaderFunc('Todas las funciones')
            for funcion in funciones:
                self.view.showFunciones(funcion)
                self.view.showMidderFunc()
                self.view.showFooterFunc()
        else:
            self.view.error('Problema al leer las funciones!')

    def comprarBoleto(self):

        nombre, flname, slname = self.askUsuario()
        usuarios = self.model.leerUserNames(nombre, flname, slname)
        if type(usuarios) == list:
            self.view.showHeader(
                'Tu usuario es:(Favor de recordar su ID lo necesitara más tarde.) \n')
            for usuario in usuarios:
                self.view.showUser(usuario)

            self.showFunciones()
            print('Selecciona tu función: \n')
            idFunc = input()
            print('\n')
            self.view.msg('Selecciona tu sala: ')
            idSala = input()
            print('\n')
            asiento = self.model.asientosFromSala(idFunc, idSala)
            fila = asiento[1]
            columna = asiento[2]

            sala = []
            for i in range(fila):
                asientos = []
                for j in range(columna):
                    nasiento = []
                    nasiento.append(s.ascii_lowercase[i])
                    nasiento.append(str(j))
                    acreado = ''.join(nasiento)
                    asientos.append(acreado)
                sala.append(asientos)

            seatSelected = self.model.leerBoletoIdFunc(idFunc)
            seatsOcupped = []
            for seat in seatSelected:
                seatsOcupped.append(seat[1])

            if seatsOcupped != None:
                for fila in sala:
                    for seat in seatsOcupped:
                        if seat in fila:
                            indx = fila.index(seat)
                            fila[indx] = 'X'
                    print(fila)
            else:
                for fila in sala:
                    print(fila)

            self.view.msg('\n Selecciona un asiento disponible:\n')
            aselect = input()

            self.view.msg('\n Introduce tu ID de usuario:')
            usuarioID = input()
            seatOc = self.model.aDisponible(seatsOcupped,aselect)
            while seatOc != True:
                self.view.msg('\n Selecciona un asiento disponible:\n')
                aselect = input()
                seatOc = self.model.aDisponible(seatsOcupped,aselect)
            self.model.crearBoleto(idFunc, aselect)
            boletoSeat = self.model.leerBoletoSeat(aselect, idFunc)
            idBoletoSeat = boletoSeat[0]
            self.model.crearBoletoU(idBoletoSeat, usuarioID)

            seatSelected = self.model.leerBoletoIdFunc(idFunc)

            for seat in seatSelected:
                seatsOcupped.append(seat[2])

            boletoRecord = self.model.leerBoletoId(idBoletoSeat)
            self.view.showHeader('Tu Boleto :  \n')
            self.view.showBoleto(boletoRecord)
        else:
            self.view.error(
                'Problema al crear tu boleto, Por favor intentalo de nuevo')

    def venderBoleto(self):

        nombre, flname, slname = self.askUsuario()
        usuarios = self.model.leerUserNames(nombre, flname, slname)
        if type(usuarios) == list:
            self.view.showHeader(
                'Tu usuario es:(Favor de recordar su ID lo necesitara más tarde.) \n')
            for usuario in usuarios:
                self.view.showUser(usuario)

            self.showFunciones()
            print('Selecciona tu función: \n')
            idFunc = input()
            self.view.msg('Selecciona tu sala: ')
            idSala = input()
            print('\n')
            asiento = self.model.asientosFromSala(idFunc, idSala)

            fila = asiento[1]
            columna = asiento[2]

            sala = []
            for i in range(fila):
                asientos = []
                for j in range(columna):
                    nasiento = []
                    nasiento.append(s.ascii_lowercase[i])
                    nasiento.append(str(j))
                    acreado = ''.join(nasiento)
                    asientos.append(acreado)
                sala.append(asientos)

            seatSelected = self.model.leerBoletoIdFunc(idFunc)
            print(seatSelected)
            seatsOcupped = []
            for seat in seatSelected:
                seatsOcupped.append(seat[1])
            print(seatsOcupped)
            if seatsOcupped != None:
                for fila in sala:
                    for seat in seatsOcupped:
                        if seat in fila:
                            indx = fila.index(seat)
                            fila[indx] = 'X'
                    print(fila)
            else:
                for fila in sala:
                    print(fila)

            self.view.msg('\n Selecciona un asiento disponible:\n')
            aselect = input()

            self.view.msg('\n Introduce tu ID de usuario:')
            usuarioID = input()

            seatOc = self.model.aDisponible(seatsOcupped,aselect)
            while seatOc != True:
                self.view.msg('\n Selecciona un asiento disponible:\n')
                aselect = input()
                seatOc = self.model.aDisponible(seatsOcupped,aselect)
                
            self.model.crearBoleto(idFunc, aselect)
            boletoSeat = self.model.leerBoletoSeat(aselect, idFunc)
            idBoletoSeat = boletoSeat[0]
            self.model.crearBoletoU(idBoletoSeat, usuarioID)

            seatSelected = self.model.leerBoletoIdFunc(idFunc)

            for seat in seatSelected:
                seatsOcupped.append(seat[2])

            boletoRecord = self.model.leerBoletoId(idBoletoSeat)
            self.view.showHeader('Tu Boleto :  \n')
            self.view.showBoletoV(boletoRecord)
        else:
            self.view.error(
                'Problema al crear tu boleto, Por favor intentalo de nuevo')
