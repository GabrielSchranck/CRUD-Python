from Model.Data.database import Database

class UsuarioRepository():
    def __init__(self):
        self.database = Database()

    def seleciona_todos_usuarios(self):
        return self.database.usuarios

    def criar_usuario(self, usuario):
        if not usuario:
            return False
        else:
            self.database.create_user(usuario)
            return True
