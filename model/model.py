from mysql import connector


class Model:

    # Conector to DB
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connector_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connector_to_db(self):
        self.cnx = connector.connect(**self.config_db, buffered=True)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    """
    METODOS PARA IDIOMAS
    """

    def crearIdioma(self, idioma):
        try:
            sql = 'INSERT INTO idioma(`descr`) VALUES(%s)'
            vals = (idioma,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leerIdiomas(self):
        try:
            sql = 'SELECT * FROM idioma'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err

    def leerIdiomaId(self, id):
        try:
            sql = 'SELECT * FROM idioma WHERE idiomaID = %s'
            vals = (id,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err

    def leerIdioma(self, idioma):
        try:
            sql = 'SELECT * FROM idioma WHERE descr = %s'
            vals = (idioma,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err

    def updateIdioma(self, id, descr):
        try:
            sql = 'UPDATE idioma SET  descr=%s WHERE idiomaID = %s'
            vals = (descr, id)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def deleteIdioma(self, idiomaID):
        try:
            sql = 'DELETE FROM idioma WHERE idiomaID = %s'
            vals = (idiomaID,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    METODOS PARA fecha
    """

    def crearFecha(self, fecha):
        try:
            sql = 'INSERT INTO fecha(`fecha`) VALUES(%s)'
            vals = (fecha,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leerFechas(self):
        try:
            sql = 'SELECT * FROM fecha'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err

    def leerFechaId(self, id):
        try:
            sql = 'SELECT * FROM fecha WHERE fechaID = %s'
            vals = (id,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def leerFecha(self, fecha):
        try:
            sql = 'SELECT * FROM fecha WHERE fecha=%s'
            vals = (fecha,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def updateFecha(self, id, fecha):
        try:
            sql = 'UPDATE fecha SET  fecha=%s WHERE fechaID = %s'
            vals = (fecha, id)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def deleteFecha(self, fechaID):
        try:
            sql = 'DELETE FROM fecha WHERE fechaID = %s'
            vals = (fechaID,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    METODOS PARA ASIENTOS
    """

    def crearAsientos(self, rows, cols):
        try:
            sql = 'INSERT INTO asientos(`asientos_x`,`asientos_y`) VALUES(%s,%s)'
            vals = (rows, cols)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def devolverIdAsiento(self):
        try:
            sql = 'SELECT MAX(asientoID) AS id FROM asientos'
            self.cursor.execute(sql)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def leerAsientos(self):
        try:
            sql = 'SELECT * FROM asientos'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err

    def leerAsientosId(self, id):
        try:
            sql = 'SELECT * FROM asientos WHERE asientoID = %s'
            vals = (id,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record

        except connector.Error as err:
            return err

    def updateAsietos(self, id, asientos_x, asientos_y):
        try:
            if asientos_x != ' ' and asientos_y != ' ':
                sql = 'UPDATE asientos SET  asientos_x=%s, asientos_y=%s  WHERE asientoID = %s'
                vals = (asientos_x, asientos_y, id)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
            elif asientos_x != ' ' and asientos_y == ' ':
                sql = 'UPDATE asientos SET  asientos_x=%s WHERE asientoID = %s'
                vals = (asientos_x, id)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
            elif asientos_x == ' ' and asientos_y != ' ':
                sql = 'UPDATE asientos SET  asientos_y=%s WHERE asientoID = %s'
                vals = (asientos_y, id)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delecteAsientos(self, asientoID):
        try:
            sql = 'DELETE FROM asientos WHERE asientoID = %s'
            vals = (asientoID,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    METODOS PARA usuerx
    """

    def crearUser(self, namex, lname1, lname2):
        try:
            sql = 'INSERT INTO userx(`nombre`,`apellido1`,`apellido2`) VALUES(%s, %s, %s)'
            vals = (namex, lname1, lname2)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leerUsers(self):
        try:
            sql = 'SELECT * FROM userx'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err

    def leerUserId(self, id):
        try:
            sql = 'SELECT * FROM userx WHERE userxID = %s'
            vals = (id,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err

    def leerUserName(self, name, apellido1, apellido2):
        try:
            sql = 'SELECT * FROM userx WHERE nombre = %s AND apellido1 = %s AND apellido2=%s'
            vals = (name, apellido1, apellido2)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records

        except connector.Error as err:
            return err

    def leerUserNames(self, name, apellido1, apellido2):
        try:
            sql = 'SELECT * FROM userx WHERE nombre = %s AND apellido1 = %s AND apellido2=%s'
            vals = (name, apellido1, apellido2)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err

    def leerUsersN(self, name):
        try:
            sql = 'SELECT * FROM userx WHERE nombre = %s'
            vals = (name,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leerUsersA(self, apellido1, apellido2):
        try:
            sql = 'SELECT * FROM userx WHERE apellido1 = %s AND apellido2 =%s'
            vals = (apellido1, apellido2)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err
    
    def updateUserx(self, fields, vals):
        try:
            sql = 'UPDATE userx SET '+','.join(fields)+' WHERE userxID = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def deleteUser(self, userxid):
        try:
            sql = 'DELETE FROM userx WHERE userxID = %s'
            vals = (userxid,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    METODOS PARA pelicula
    """

    def crearPelicula(self, idiomaID, nombrePelicula, clasificacion, sipnosis, duracion):
        try:
            sql = 'INSERT INTO pelicula(`idiomaID`,`nombrePelicula`,`clasificacion`,`sipnosis`,`duracion`) VALUES(%s, %s, %s, %s, %s)'
            vals = (idiomaID, nombrePelicula,
                    clasificacion, sipnosis, duracion)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leerPeliculas(self):
        try:
            sql = 'SELECT pelicula.peliculaID, pelicula.nombrePelicula, idioma.descr, pelicula.clasificacion, pelicula.sipnosis, pelicula.duracion FROM pelicula INNER JOIN idioma ON pelicula.idiomaID=idioma.idiomaID'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leerPeliculaId(self, id):
        try:
            sql = 'SELECT pelicula.peliculaID, pelicula.nombrePelicula, idioma.descr, pelicula.clasificacion, pelicula.sipnosis, pelicula.duracion FROM pelicula INNER JOIN idioma ON pelicula.idiomaID=idioma.idiomaID WHERE pelicula.peliculaID =%s '
            vals = (id,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def leerPeliculaNombre(self, nombrePelicula):
        try:
            sql = 'SELECT pelicula.peliculaID, pelicula.nombrePelicula, idioma.descr, pelicula.clasificacion, pelicula.sipnosis, pelicula.duracion FROM pelicula INNER JOIN idioma ON  pelicula.idiomaID=idioma.idiomaID WHERE pelicula.nombrePelicula = %s;'
            vals = (nombrePelicula,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leerPeliculasClasificacion(self, clas):
        clas = clas.capitalize()
        try:
            sql = 'SELECT pelicula.peliculaID, pelicula.nombrePelicula, idioma.descr, pelicula.clasificacion, pelicula.sipnosis, pelicula.duracion FROM pelicula INNER JOIN idioma ON  pelicula.idiomaID=idioma.idiomaID WHERE pelicula.clasificacion = %s'
            vals = (clas,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leerPeliculaIdioma(self, idiomaID):
        
        try:
            sql = 'SELECT  pelicula.peliculaID, pelicula.nombrePelicula, idioma.descr, pelicula.clasificacion, pelicula.sipnosis, pelicula.duracion FROM pelicula INNER JOIN idioma ON idioma.idiomaID=pelicula.idiomaID WHERE idioma.idiomaID=%s'
            vals = (idiomaID,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def updatePelicula(self, fields, vals):
        try:
            sql = 'UPDATE pelicula SET ' + ','.join(fields) + ' WHERE peliculaID = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def deletePelicula(self, pelciulaID):
        try:
            sql = 'DELETE FROM pelicula WHERE peliculaID = %s'
            vals = (pelciulaID,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    METODOS PARA sala
    """

    def crearSala(self, rows, cols, tipo):
        self.crearAsientos(rows, cols)
        asientoId, = self.devolverIdAsiento()
        try:
            sql = 'INSERT INTO sala(`asientoID`,`tipo`) VALUES(%s,%s)'
            vals = (asientoId, tipo)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leerSalas(self):
        try:
            sql = 'SELECT sala.salaID, sala.tipo, a.asientos_x, a.asientos_y FROM sala JOIN asientos a  ON sala.asientoID = a.asientoID '
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leerSalaID(self, id):
        try:
            sql = 'SELECT sala.salaID, sala.tipo, a.asientos_x, a.asientos_y FROM sala JOIN asientos a ON sala.asientoID = a.asientoID WHERE sala.salaID = %s'
            vals = (id,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def leerSalaTipo(self, tipo):
        try:
            sql = 'SELECT sala.salaID, sala.tipo, a.asientos_x, a.asientos_y FROM sala JOIN asientos a ON a.asientoID = sala.asientoID WHERE sala.tipo = %s'
            vals = (tipo,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def updateSala(self, ida, rows, cols, tipo):
        self.updateAsietos(ida, rows, cols)
        try:
            sql = 'UPDATE sala SET tipo =%s WHERE salaID = %s'
            vals = (tipo, ida)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def deleteSala(self, id):
        out  = self.delecteAsientos(id)
        if out == True:
            return True
        else:
            return False
    """
    METODOS PARA boletos
    """

    def crearBoleto(self, funcion, seat):
        try:
            sql = 'INSERT INTO boleto(`funcionID`,`asiento`) VALUES(%s,%s)'
            vals = (funcion, seat)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leerBoletos(self):
        try:
            sql = 'SELECT b.boletoID, b.asiento, u.nombre, u.apellido1, s.salaID, p.nombrePelicula, fe.fecha, f.hora, i.descr FROM boleto b JOIN boleto_usuario bu ON b.boletoID = bu.boletoID JOIN funcion f ON b.funcionID = f.funcionID JOIN userx u ON u.userxID = bu.userxID JOIN pelicula p ON f.peliculaID = p.peliculaID JOIN fecha fe ON f.fechaID = fe.fechaID JOIN sala s ON f.salaID = s.salaID JOIN idioma i ON i.idiomaID = p.idiomaID'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leerBoletoId(self, idb):
        try:
            sql = 'SELECT b.boletoID, b.asiento, u.nombre, u.apellido1, s.salaID, p.nombrePelicula, fe.fecha, f.hora, i.descr FROM boleto b JOIN boleto_usuario bu ON b.boletoID = bu.boletoID JOIN funcion f ON b.funcionID = f.funcionID JOIN userx u ON u.userxID = bu.userxID JOIN pelicula p ON f.peliculaID = p.peliculaID JOIN fecha fe ON f.fechaID = fe.fechaID JOIN sala s ON f.salaID = s.salaID JOIN idioma i ON i.idiomaID = p.idiomaID WHERE b.boletoID = %s '
            vals = (idb,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def leerBoletoIdFunc(self, idfuncion):
        try:
            sql = 'SELECT b.boletoID, b.asiento, u.nombre, u.apellido1, s.salaID, p.nombrePelicula, fe.fecha, f.hora, i.descr FROM boleto b JOIN boleto_usuario bu ON b.boletoID = bu.boletoID JOIN funcion f ON b.funcionID = f.funcionID JOIN userx u ON u.userxID = bu.userxID JOIN pelicula p ON f.peliculaID = p.peliculaID JOIN fecha fe ON f.fechaID = fe.fechaID JOIN sala s ON f.salaID = s.salaID JOIN idioma i ON i.idiomaID = p.idiomaID WHERE b.funcionID = %s'
            vals = (idfuncion,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leerBoletoIdUs(self, idUs):
        try:
            sql = 'SELECT b.boletoID, b.asiento, u.nombre, u.apellido1, s.salaID, p.nombrePelicula, fe.fecha, f.hora, i.descr FROM boleto b JOIN boleto_usuario bu ON b.boletoID = bu.boletoID JOIN funcion f ON b.funcionID = f.funcionID JOIN userx u ON u.userxID = bu.userxID JOIN pelicula p ON f.peliculaID = p.peliculaID JOIN fecha fe ON f.fechaID = fe.fechaID JOIN sala s ON f.salaID = s.salaID JOIN idioma i ON i.idiomaID = p.idiomaID WHERE bu.userxID = %s'
            vals = (idUs,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leerBoletoSeat(self, seat, idFunc):
        try:
            sql = 'SELECT b.boletoID, b.funcionID, b.asiento FROM boleto b WHERE b.asiento = %s AND b.funcionID=%s'
            vals = (seat, idFunc)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def updateBoleto(self, fields, vals):
        try:
            sql = 'UPDATE boleto SET ' + \
                ','.join(fields) + ' WHERE boletoID = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def deleteBoleto(self, idb):

        try:
            sql = 'DELETE FROM boleto WHERE boletoID = %s'
            vals = (idb,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    """
    METODOS PARA boleto_usuario  
    """

    def crearBoletoU(self, idu, idb):
        try:
            sql = 'INSERT INTO boleto_usuario(`boletoID`,`userxID`) VALUES(%s,%s)'
            vals = (idu, idb)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leerBoletosU(self):
        try:
            sql = 'SELECT * FROM boleto_usuario'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leerBoletoUID(self, uid):
        try:
            sql = 'SELECT * FROM boleto_usuario WHERE userxID =%'
            vals = (uid,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def leerBoletoUBID(self, bid):
        try:
            sql = 'SELECT * FROM boleto_usuario WHERE boletoID =%'
            vals = (bid,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def deleteBoletoU(self, idb, idu):
        try:
            sql = 'DELETE FROM boleto_usuario WHERE boletoID =%s AND userxID = %s'
            vals = (idb,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    METODOS PARA funcion  
    """

    def crearFuncion(self, peliculaID, salaID, fechaID, hora):
        try:
            sql = 'INSERT INTO funcion(`peliculaID`,`salaID`,`fechaID`,`hora`) VALUES(%s,%s,%s,%s)'
            vals = (peliculaID, salaID, fechaID, hora)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leerFunciones(self):
        try:
            sql = 'SELECT f.funcionID, p.nombrePelicula, i.descr, p.clasificacion, p.duracion, s.salaID, fe.fecha FROM funcion f JOIN pelicula p ON f.peliculaID =p.peliculaID JOIN idioma i ON p.idiomaID = i.idiomaID JOIN sala s ON f.salaID = s.salaID JOIN fecha fe ON f.fechaID = fe.fechaID;'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leerFuncionId(self, id):
        try:
            sql = 'SELECT f.funcionID, p.nombrePelicula, i.descr, p.clasificacion, p.duracion, s.salaID, fe.fecha FROM funcion f JOIN pelicula p ON f.peliculaID =p.peliculaID JOIN idioma i ON p.idiomaID = i.idiomaID JOIN sala s ON f.salaID = s.salaID JOIN fecha fe ON f.fechaID = fe.fechaID WHERE f.funcionID =%s'
            vals = (id,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def leerFuncionPeliculaId(self, id):
        try:
            sql = 'SELECT f.funcionID, p.nombrePelicula, i.descr, p.clasificacion, p.duracion, s.salaID, fe.fecha FROM funcion f JOIN pelicula p ON f.peliculaID =p.peliculaID JOIN idioma i ON p.idiomaID = i.idiomaID JOIN sala s ON f.salaID = s.salaID JOIN fecha fe ON f.fechaID = fe.fechaID WHERE f.peliculaID =%s'
            vals = (id,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leerFuncionSalaId(self, id):
        try:
            sql = 'SELECT f.funcionID, p.nombrePelicula, i.descr, p.clasificacion, p.duracion, s.salaID, fe.fecha FROM funcion f JOIN pelicula p ON f.peliculaID =p.peliculaID JOIN idioma i ON p.idiomaID = i.idiomaID JOIN sala s ON f.salaID = s.salaID JOIN fecha fe ON f.fechaID = fe.fechaID WHERE f.salaID =%s'
            vals = (id,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leerFuncionFechaId(self, id):
        try:
            sql = 'SELECT f.funcionID, p.nombrePelicula, i.descr, p.clasificacion, p.duracion, s.salaID, fe.fecha FROM funcion f JOIN pelicula p ON f.peliculaID =p.peliculaID JOIN idioma i ON p.idiomaID = i.idiomaID JOIN sala s ON f.salaID = s.salaID JOIN fecha fe ON f.fechaID = fe.fechaID  WHERE f.fechaID =%s'
            vals = (id,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leerFuncionHora(self, hora):
        try:
            sql = 'SELECT f.funcionID, p.nombrePelicula, i.descr, p.clasificacion, p.duracion, s.salaID, fe.fecha FROM funcion f JOIN pelicula p ON f.peliculaID =p.peliculaID JOIN idioma i ON p.idiomaID = i.idiomaID JOIN sala s ON f.salaID = s.salaID JOIN fecha fe ON f.fechaID = fe.fechaID WHERE f.hora =%s'
            vals = (hora,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def updateFuncion(self, fields, vals):
        try:
            sql = 'UPDATE funcion SET ' + \
                ','.join(fields) + ' WHERE funcionID = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def deleteFuncion(self, idFuncion):
        try:
            sql = 'DELETE FROM funcion WHERE funcionID =%s'
            vals = (idFuncion,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    
    # ASIENTOS DESDE FUNCION

    def asientosFromSala(self, idFuncion, idSala):
        try:
            sql = 'SELECT a.asientoID, a.asientos_x, a.asientos_y FROM asientos a JOIN sala s ON a.asientoID = s.asientoID JOIN funcion f ON f.salaID = s.salaID WHERE s.salaID = %s AND f.funcionID = %s;'
            vals = (idSala, idFuncion)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def aDisponible (self, lst, asiento):
        if asiento in lst:
            return False
        else:
            return True