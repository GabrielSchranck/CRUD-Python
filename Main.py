from Controller.Usuario_controller import Usuario_controller

def main():
    usuario_controller = Usuario_controller()
    while True:
        usuario_controller.chama_menu()
        opcoes = input("Escolha uma opção: ")

        try:
            opcoes = int(opcoes)
        
            match opcoes:
                case 1:
                    usuario_controller.cadastrar_usuario_service()
                case 2:
                    usuario_controller.ver_usuarios()
                case 3:
                    usuario_controller.ver_usuario()
                case 4:
                    print("Hello World")
                case 5:
                    print("Hello World")
                case 6:
                    usuario_controller.sair()
                    break
                case _:
                    input("\033[31mOpção inválida. Tente novamente\033[0m.")
                    
        except ValueError:
             input("\033[31mDigite um número válido!\033[0m")


if __name__ == "__main__":
    main()