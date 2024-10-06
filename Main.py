from Controller.Usuario_service import Usuario_Service

def main():
    usuario_service = Usuario_Service()
    while True:
        usuario_service.chama_menu()
        opcoes = input("Escolha uma opção: ")

        try:
            opcoes = int(opcoes)
        
            match opcoes:
                case 1:
                    usuario_service.cadastrar_usuario_service()
                case 2:
                    usuario_service.ver_usuarios()
                case 3:
                    usuario_service.ver_usuario()
                case 4:
                    print("Hello World")
                case 6:
                    print("\033[31mSaindo...\033[0m")
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
                    
        except ValueError:
             print("Digite um número válido!")


if __name__ == "__main__":
    main()