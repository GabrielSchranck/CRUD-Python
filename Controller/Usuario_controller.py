from Model.Objects.Usuario import Usuario
from View.MenuView import MenuView
from Model.Repositories.UsuarioRepository import UsuarioRepository

class Usuario_controller():
    def __init__(self):
        self.usuarios = []
        self.proximo_id = 1
        self.inicia_lista_usuarios()

    def inicia_lista_usuarios(self):
        usuarioRepository = UsuarioRepository()
        self.usuarios = usuarioRepository.seleciona_todos_usuarios()

        for usuario in self.usuarios:
            self.proximo_id += 1

    def cadastrar_usuario(self, nome, idade, email, cpf, curso):
        usuario = Usuario(self.proximo_id, nome, idade, email, cpf, curso)
        self.usuarios.append(usuario)
        self.proximo_id += 1
        return usuario
    
    def ler_dados_cadastro(self):
        while True:
            nome = input("Digite seu nome: ")
            if not nome.isalpha():
                print("Digite um nome válido!")
                MenuView.limpar_console()
                continue

            idade = input("Digite sua idade: ") 
            if not idade.isdigit():
                print("Digite uma idade válida!")
                MenuView.limpar_console()
                continue

            email = input("Digite seu email: ")
            if "@" not in email or "." not in email.split("@")[-1]:
                print("Você deve digitar um email válido!")
                MenuView.limpar_console()
                continue

            cpf = input("Digite seu cpf: ")
            if not cpf.isdigit() or len(cpf) != 11:
                print("Digite um cpf válido!")
                MenuView.limpar_console()
                continue

            curso = input("Digite seu curso: ")
            if not curso:
                print("O curso não pode ser vazio!")
                MenuView.limpar_console()
                continue

            return nome, idade, email, cpf, curso

    def mostra_usuario(self, pesquisa):
        naoEncontrado = False
        for usuario in self.usuarios:
            if usuario.nome == pesquisa:
                MenuView.exibe_usuario(usuario)
            else:
                naoEncontrado = True

        if naoEncontrado:
            print("\033[31mUsuário não encontrado")

    # def alterar_usuario(self, usuario):        
        