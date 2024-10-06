from View.MenuView import MenuView
from Controller.Usuario_controller import Usuario_controller
from Model.Repositories.UsuarioRepository import UsuarioRepository

class Usuario_Service():
    def __init__(self):
        self.controller = Usuario_controller()

    def chama_menu(self):
        MenuView.limpar_console()
        MenuView.exibe_menu()
    
    def cadastrar_usuario_service(self):
        MenuView.limpar_console()
        usuarioRepository = UsuarioRepository()

        if usuarioRepository.criar_usuario(self.controller.cadastrar_usuario(*self.controller.ler_dados_cadastro())):
            MenuView.limpar_console()
            print("\033[33mUsuário cadastrado com sucesso\033[0m")
            input("\033[32mPressione Enter para continuar...\033[0m")
        else:
            print("\033[31mErro ao cadastrar usuário\033[0m")
            input("\033[32mPressione Enter para continuar...\033[0m")
    
    def ver_usuarios(self):
        MenuView.limpar_console()
        MenuView.exibe_usuarios_cadastrados(self.controller.usuarios)
        input("\033[32mPressione Enter para continuar...\033[0m")
        MenuView.limpar_console()
    
    def ver_usuario(self):
        MenuView.limpar_console()
        self.controller.mostra_usuario(input("\033[34mInsira o nome do usuário:\033[0m "))
        input("\033[32mPressione Enter para continuar...\033[0m")