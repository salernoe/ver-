from dal.db import Db

def listar():
    sql = "SELECT RID, NOMBRE FROM TIPOS ORDER BY RID;"
    result = Db.consultar(sql)
    return result