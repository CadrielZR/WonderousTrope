class Users():
    def __init__(self, id, nome, senha):
        self._id =id
        self._nome = nome
        self._senha = senha

class Writing():
    def __init__(self,id, prompts):
        self._id = id
        self._prompts = prompts

class Drawing():
    def __init__(self,id,prompts):
        self._id=id
        self._prompts=prompts

class Generos():
    def __init__(self,id,nome):
        self._id = id
        self._nome = nome