from models import Users, Writing, Generos, Drawing, Writing_fav, Drawing_fav

#CRUD Usuarios
SQL_CRIA_USUARIOS = 'INSERT into usuario(id, nome, senha) values (%s,%s,%s)'
SQL_ATUALIZA_USUARIOS = 'UPDATE usuario SET id=%s, nome=%s, senha=%s where id=%s'
SQL_BUSCA_USUARIOS_POR_ID = 'SELECT id, nome, senha from usuario where id = %s'
SQL_BUSCA_USUARIO_POR_ID_LISTA = 'SELECT id, nome, senha from usuario'
SQL_DELETA_USUARIOS = 'delete from usuario where id = %s'

#CRUD Writing Prompts
SQL_ATUALIZA_WRITING_PROMPTS = 'UPDATE writing SET id=%s, prompts=%s where id=%s'
SQL_BUSCA_WRITING_PROMPTS_POR_ID = 'SELECT id, prompts from writing where id=%s'

#CRUD Generos
SQL_BUSCA_GENEROS_POR_ID = 'SELECT id, nome from generos where id=%s'
SQL_BUSCA_GENEROS_POR_ID_LISTA = 'SELECT id, nome from generos'

#CRUD Drawing Prompts
SQL_ATUALIZA_DRAWING_PROMPTS = 'UPDATE drawing SET id=%s, prompts=%s where id=%s'
SQL_BUSCA_DRAWING_PROMPTS_POR_ID = 'SELECT id, prompts from drawing where id=%s'

#CRUD Writing favorites
SQL_CRIA_WRITING_FAV = 'INSERT into writing_fav(id, prompts) values (%s,%s)'
SQL_ATUALIZA_WRITING_FAV = 'UPDATE writing_fav SET id=%s, prompts=%s where id=%s'
SQL_BUSCA_WRITING_FAV_POR_ID = 'SELECT id, prompts from writing_fav where id = %s'
SQL_BUSCA_WRITING_FAV_POR_ID_LISTA = 'SELECT id, prompts from writing_fav'
SQL_DELETA_WRITING_FAV = 'delete from writing_fav where id = %s'

#CRUD Drawing Favorites
SQL_CRIA_DRAWING_FAV = 'INSERT into drawing_fav(id, prompts) values (%s,%s)'
SQL_ATUALIZA_DRAWING_FAV = 'UPDATE drawing_fav SET id=%s, prompts=%s where id=%s'
SQL_BUSCA_DRAWING_FAV_POR_ID = 'SELECT id, prompts from drawing_fav where id = %s'
SQL_BUSCA_DRAWING_FAV_POR_ID_LISTA = 'SELECT id, prompts from drawing_fav'
SQL_DELETA_DRAWING_FAV = 'delete from drawing_fav where id = %s'


#classes
#Usuarios
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

def traduz_usuario_lista(usuario):
    def cria_usuario_com_tupla(tupla):
        return Users(tupla[0], tupla[1], tupla[2])
    return list(map(cria_usuario_com_tupla, usuario))

#Writing_prompts
class WritingPromptDao():
    def __init__(self,db):
        self.__db = db

    def busca_por_id(self,id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_WRITING_PROMPTS_POR_ID,(id,))
        tupla = cursor.fetchone()
        return Writing(tupla[0], tupla[1])

def traduz_writing(prompt):
    def cria_prompt_tupla(tupla):
        return Writing(str(tupla[0]), tupla[1])
    return list(map(cria_prompt_tupla,prompt))

#Genero
class GeneroDao():
    def __init__(self,db):
        self.__db=db


    def busca_por_id(self,id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_GENEROS_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Generos(tupla[1], id=tupla[0])

    def lista (self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_GENEROS_POR_ID_LISTA)
        genero = traduz_genero_lista(cursor.fetchall())
        return genero

#Drawing Prompts:
class DrawingPromptDao():
    def __init__(self,db):
        self.__db=db

    def busca_por_id(self,id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_DRAWING_PROMPTS_POR_ID,(id,))
        tupla = cursor.fetchone()
        return Drawing(tupla[0], tupla[1])

class WritingFavDao():
    def __init__(self, db):
        self.__db=db

    def salvar(self, prompt):
        cursor =self.__db.connection.cursor()
        cursor.execute(SQL_CRIA_WRITING_FAV, (prompt._id, prompt._prompts))

        self.__db.connection.commit()
        return prompt

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_WRITING_FAV_POR_ID_LISTA)
        prompts = traduz_writing_fav(cursor.fetchall())
        return prompts

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_WRITING_FAV_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Writing_fav(tupla[0],tupla[1])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_WRITING_FAV, (id,))
        self.__db.connection.commit()

class DrawingFavDao():
    def __init__(self, db):
        self.__db=db

    def salvar(self, prompt):
        cursor =self.__db.connection.cursor()
        cursor.execute(SQL_CRIA_DRAWING_FAV, (prompt._id, prompt._prompts))

        self.__db.connection.commit()
        return prompt

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_DRAWING_FAV_POR_ID_LISTA)
        prompts = traduz_drawing_fav(cursor.fetchall())
        return prompts

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_DRAWING_FAV_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Writing_fav(tupla[0],tupla[1])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_DRAWING_FAV, (id,))
        self.__db.connection.commit()


def traduz_writing_fav(prompt):
    def cria_prompt_tupla(tupla):
        return Writing_fav(tupla[0], tupla[1])
    return list(map(cria_prompt_tupla,prompt))

def traduz_drawing_fav(prompt):
    def cria_prompt_tupla(tupla):
        return Drawing_fav(tupla[0], tupla[1])
    return list(map(cria_prompt_tupla,prompt))

def traduz_genero(tupla):
    return Generos(tupla[0], tupla[1])

def traduz_genero_lista(genero):
    def cria_usuario_com_tupla(tupla):
        return Generos(tupla[0], tupla[1])
    return list(map(cria_usuario_com_tupla, genero))