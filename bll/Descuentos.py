from dal.db import Db



def agregar(dia, descuento):    
    sql = "INSERT INTO DESCUENTOS(DIAS, DESCUENTOS) VALUES(?, ?);"
    parametros = (dia, descuento)
    Db.ejecutar(sql, parametros)

def actualizar(dia, descuento, id):    
    sql = "UPDATE DESCUENTOS SET DIAS = ?, DESCUENTOS = ? WHERE DID = ? AND ESTADO = 1;"
    parametros = (dia, descuento, id)
    Db.ejecutar(sql, parametros)    

def eliminar(id, logical = True):    
    if logical:
        sql = "UPDATE DESCUENTOS SET ESTADO = 0 WHERE DID = ? AND ESTADO = 1;"
    else:
        sql = "DELETE FROM DESCUENTOS WHERE ID = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)

def listar():
    sql = '''SELECT DID, DIAS, DESCUENTOS, ESTADO
            FROM DESCUENTOS;'''
    result = Db.consultar(sql)
    return result

def obtener_id(id):
    sql = '''SELECT DID, DIAS, DESCUENTOS, ESTADO
            FROM DESCUENTOS            
            WHERE DID = ? AND ESTADO = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result

