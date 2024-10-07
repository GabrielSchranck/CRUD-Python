from View.MenuView import MenuView
from Service.Usuario_service import Usuario_Service
from Model.Repositories.UsuarioRepository import UsuarioRepository

class Usuario_controller():
    def __init__(self):
        self.service = Usuario_Service()

    def chama_menu(self):
        MenuView.limpar_console()
        MenuView.exibe_menu()
    
    def cadastrar_usuario_service(self):
        MenuView.limpar_console()
        usuarioRepository = UsuarioRepository()

        if usuarioRepository.criar_usuario(self.service.cadastrar_usuario(*self.service.ler_dados_cadastro())):
            MenuView.limpar_console()
            print("\033[33mUsuário cadastrado com sucesso\033[0m")
            input("\033[32mPressione Enter para continuar...\033[0m")
        else:
            print("\033[31mErro ao cadastrar usuário\033[0m")
            input("\033[32mPressione Enter para continuar...\033[0m")
    
    def ver_usuarios(self):
        MenuView.limpar_console()
        MenuView.exibe_usuarios_cadastrados(self.service.usuarios)
        input("\033[32mPressione Enter para continuar...\033[0m")
        MenuView.limpar_console()
    
    def ver_usuario(self):
        MenuView.limpar_console()
        self.service.mostra_usuario(input("\033[34mInsira o nome do usuário:\033[0m "))
        input("\033[32mPressione Enter para continuar...\033[0m")

    def sair(self):
        MenuView.limpar_console()
        print("\033[31mSaindo...\033[0m")