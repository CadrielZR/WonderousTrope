from models import Users

#CRUD Usuarios
SQL_CRIA_USUARIOS = 'INSERT into usuarios (id, nome, senha) values (%s,%s,%s)'
SQL_ATUALIZA_USUARIOS = 'UPDATE usuarios SET id=%s, nome=%s, senha=%s where id=%s'
SQL_BUSCA_USUARIOS_POR_ID = 'SELECT id, nome, senha from usuarios where id = %s'
SQL_DELETA_USUARIOS = 'delete from usuarios where id = %s'

#classes
class UsuarioDao():
    def __init__(self, db):
        self.__db =db

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_USUARIOS_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario


def traduz_usuario(tupla):
    return Users(tupla[0], tupla[1], tupla[2])