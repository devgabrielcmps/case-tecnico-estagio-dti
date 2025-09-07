# Desenvolvedor: Gabriel Campos Amaral Ribeiro
# Resolução do Case do Processo Seletivo para Estágio – DTI Digital
# CRUD - AGENDA

#importa o pack sqlite para a aplicacao
import sqlite3 as sql

#importa as funcoes criadas no arquivo database.py e da o apelido de db pra facilitar
import database as db

def main():
  #Chama a funcao para criacao do banco de dados
  db.criaBanco()
  while(True):
    print("-------------------------")
    print("\n[1] - Cadastrar contato")
    print("[2] - Listar contatos")
    print("[3] - Atualizar contato")
    print("[4] - Excluir contato")
    print("[5] - Sair")
    escolha=int(input("ESCOLHA: "))

    #Tratamento de erros

    #Escolhas
    if(escolha==1):
      db.cadastro()

    elif(escolha==2):
      db.leitura()

    elif(escolha==3):
      db.atualizacao()

    elif(escolha==4):
      db.exclusao()

    else:
      print("\nObrigado!!! Volte Sempre !!! \n")
      break;

main()
    



