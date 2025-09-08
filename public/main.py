# Desenvolvedor: Gabriel Campos Amaral Ribeiro
# Resolução do Case do Processo Seletivo para Estágio – DTI Digital
# CRUD - AGENDA

# importa as funções do arquivo database.py com o apelido 'db'
import database as db

def main():
    db.criaBanco()  # cria o banco de dados se não existir
    while True:
        # exibe o menu principal
        print("\n---------- MENU ----------")
        print("\n[1] - Cadastrar contato")
        print("[2] - Listar contatos")
        print("[3] - Atualizar contato")
        print("[4] - Excluir contato")
        print("[5] - Sair")
        escolha = int(input("ESCOLHA: "))

        # verifica a opção escolhida
        if escolha == 1:
            db.cadastro()        # chama a função para cadastrar contato
        elif escolha == 2:
            db.leitura()         # chama a função para listar contatos
        elif escolha == 3:
            db.atualizacao()     # chama a função para atualizar contato
        elif escolha == 4:
            db.exclusao()        # chama a função para excluir contato
        else:
            print("\nObrigado!!! Volte Sempre !!! \n")
            break               # encerra o loop e o programa

# inicia o programa
main()
