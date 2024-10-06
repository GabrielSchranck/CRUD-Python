from msilib.schema import File
import os
from Model.Objects.Usuario import Usuario

class Database():
    def __init__(self):
        self.database_name = "Dados.txt"
        self.usuarios = []
        self.verificar_existe_banco()
        self.buscar_dados()

    def verificar_existe_banco(self):
        if not os.path.exists(self.database_name):
            with open(self.database_name, 'w') as f:
                pass

    def buscar_dados(self):
        try:
            with open(self.database_name, 'r') as f:
                linhas = f.readlines()

                for linha in linhas:
                    id, nome, idade, email, cpf, curso = linha.strip().split(',')
                    usuario = Usuario(id, nome, idade, email, cpf, curso)
                    self.usuarios.append(usuario)
        
        except FileNotFoundError:
            print("Arquivo não encontrado.")

    def create_user(self, usuario):
        self.usuarios.append(usuario)
        try:
            with open(self.database_name, 'a') as f:  
                linha = f"{usuario.id},{usuario.nome},{usuario.idade},{usuario.email},{usuario.cpf},{usuario.curso}"
                f.write(linha + "\n")

        except FileNotFoundError:
            print("Arquivo não encontrado.")
