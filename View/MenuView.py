import os

class MenuView():
    @staticmethod
    def exibe_menu():
        print("""
           \033[34m-----Menu------\033[0m
        \033[32m1- Cadastrar usuário\033[0m
        \033[35m2- Ver usuários\033[0m
        \033[35m3- Ver usuário\033[0m
        \033[33m4- Alterar usuário\033[0m
        \033[31m5- Remover usuário\033[0m
        \033[34m6- Sair\033[0m
        """)
    
    @staticmethod
    def exibe_usuarios_cadastrados(usuarios):
        if not usuarios:
            print("\033[31mNão há clientes para serem exibidos\033[0m")
        else:
            for usuario in usuarios:
                print(f"""
                \033[34m------------------------\033[0m
                id: \033[32m{usuario.id}\033[0m
                nome: \033[36m{usuario.nome}\033[0m    cpf: \033[33m{usuario.cpf}\033[0m
                email: \033[35m{usuario.email}\033[0m  curso: \033[36m{usuario.curso}\033[0m
                """)

    @staticmethod
    def exibe_usuario(usuario):
        print(f"""
                \033[34m------------------------\033[0m
                id: \033[32m{usuario.id}\033[0m
                nome: \033[36m{usuario.nome}\033[0m    cpf: \033[33m{usuario.cpf}\033[0m
                email: \033[35m{usuario.email}\033[0m  curso: \033[36m{usuario.curso}\033[0m
                """)

    @staticmethod
    def limpar_console():
        if os.name == 'nt':  
            os.system('cls')
        else: 
            os.system('clear')