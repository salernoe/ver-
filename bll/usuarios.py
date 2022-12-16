from dal.db import Db


def agregar(apellido, nombre, dni, correo_electronico, usuario, contrasenia, rol_Id):    
    sql = "INSERT INTO USUARIOS(APELLIDO, NOMBRE, DNI, EMAIL, USUARIO, CONTRASEÑA, RID) VALUES(?, ?, ?, ?, ?, ?, ?);"
    parametros = (apellido, nombre, dni, correo_electronico, usuario, Db.encriptar_contraseña(contrasenia), rol_Id)
    Db.ejecutar(sql, parametros)

def actualizar(id, apellido, nombre, dni, correo_electronico, contrasenia, rol_Id):    
    sql = "UPDATE USUARIOS SET APELLIDO = ?, NOMBRE = ?, DNI = ?, EMAIL = ?, CONTRASEÑA = ?, RID = ? WHERE ID = ? AND ESTADO = 1;"
    parametros = (apellido, nombre, dni, correo_electronico, Db.encriptar_contraseña(contrasenia), rol_Id, id)
    Db.ejecutar(sql, parametros)

def actualizar_noPass(id, apellido, nombre, dni, correo_electronico, rol_Id):    
    sql = "UPDATE USUARIOS SET APELLIDO = ?, NOMBRE = ?, DNI = ?, EMAIL = ?, RID = ? WHERE ID = ? AND ESTADO = 1;"
    parametros = (apellido, nombre, dni, correo_electronico, rol_Id, id)
    Db.ejecutar(sql, parametros)    

def eliminar(id, logical = True):    
    if logical:
        sql = "UPDATE USUARIOS SET ESTADO = 0 WHERE ID = ? AND ESTADO = 1;"
    else:
        sql = "DELETE FROM USUARIOS WHERE ID = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)

def listar():
    sql = '''SELECT u.ID, u.APELLIDO, u.NOMBRE, u.DNI, u.EMAIL, u.USUARIO, u.RID, r.NOMBRE
            FROM USUARIOS u
            INNER JOIN TIPOS r ON u.RID = r.RID
            WHERE u.ESTADO = 1;'''
    result = Db.consultar(sql)
    return result

def filtrar(usuario):    
    sql = '''SELECT u.ID, u.APELLIDO, u.NOMBRE, u.DNI, u.EMAIL, u.USUARIO, u.RID, r.NOMBRE 
            FROM USUARIOS u
            INNER JOIN TIPOS r ON u.RID = r.RID
            WHERE u.USUARIO LIKE ? AND u.ESTADO = 1;'''    
    parametros = ('%{}%'.format(usuario),)    
    result = Db.consultar(sql, parametros)
    return result

def validar(usuario, contrasenia):    
    sql = "SELECT USUARIO FROM USUARIOS WHERE USUARIO = ? AND CONTRASEÑA = ? AND ESTADO = 1;"
    parametros = (usuario, Db.encriptar_contraseña(contrasenia))
    result = Db.consultar(sql, parametros, False)
    return result != None

def existe(usuario):
    sql = "SELECT COUNT(*) FROM USUARIOS WHERE USUARIO = ? AND ESTADO = 1;"
    parametros = (usuario,)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1

def validarTipo(usuario, contrasenia):    
    sql = "SELECT RID FROM USUARIOS WHERE USUARIO = ? AND CONTRASEÑA = ? AND ESTADO = 1;"
    parametros = (usuario, Db.encriptar_contraseña(contrasenia))
    result = Db.consultar(sql, parametros, False)    
    return result[0]

def obtener_id(id):
    sql = '''SELECT u.ID, u.APELLIDO, u.NOMBRE, u.DNI, u.EMAIL, u.USUARIO, u.RID, r.NOMBRE
            FROM USUARIOS u
            INNER JOIN TIPOS r ON u.RID = r.RID
            WHERE u.ID = ? AND u.ESTADO = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result

def id_usuario(usuario):
    sql = '''SELECT ID
            FROM USUARIOS             
            WHERE USUARIO = ? AND ESTADO = 1;'''
    parametros = (usuario,)
    result = Db.consultar(sql, parametros, False)    
    return result