# Desenvolvedor: Gabriel Campos Amaral Ribeiro
# Resolução do Case do Processo Seletivo para Estágio – DTI Digital
# CRUD - AGENDA

# importa pacotes necessarios
import sqlite3 as sql 
import datetime

# cria o banco de dados
def criaBanco():
  conexao = sql.connect('database.db')  # conecta ao banco ou cria o arquivo
  cursor = conexao.cursor()             # inicializa o cursor para executar comandos SQL

  # cria a tabela CONTATOS com id, nome, numero e data de nascimento
  cursor.execute('''CREATE TABLE IF NOT EXISTS CONTATOS 
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  nome TEXT NOT NULL,
                  numero_celular TEXT NOT NULL,
                  data_nascimento DATE )
                  ''')

  conexao.commit()  # salva alteracoes no banco
  cursor.close()    # fecha o cursor
  conexao.close()   # fecha a conexao

def cadastro():
  # conecta ao banco de dados
  conexao = sql.connect('database.db')
  cursor = conexao.cursor()

  # VALIDAÇÃO DAS INFORMACOES DO USUARIO
  while True:
      # pede o nome, remove espacos extras e coloca a primeira letra maiuscula
      nome = input("\nNOME: ").strip().title()

      # verifica se o nome ja existe no banco
      cursor.execute("SELECT 1 FROM CONTATOS WHERE nome = ?", (nome,))

      if nome == ' ':
          print("NOME INVALIDO! DIGITE NOVAMENTE!")
      elif cursor.fetchone():  # se já existir algum registro
          print("NOME JA CADASTRADO! DIGITE NOVAMENTE!")
      else:
          break

  # validacaoo do numero de celular (deve ter 11 digitos)
  while True:
      numero_celular = input("CELULAR [31...]: ").strip()
      if len(numero_celular) != 11:
          print("NUMERO DE CELULAR INVALIDO! DIGITE NOVAMENTE!")
      else:
          break

  # validacao da data de nascimento
  while True:
      data_nascimento = input("DATA NASCIMENTO (DDMMYYYY): ").strip()

      if len(data_nascimento) != 8:
          print("DATA DE NASCIMENTO INVALIDA! DIGITE NOVAMENTE!")
          continue

      dia = int(data_nascimento[:2])
      mes = int(data_nascimento[2:4])
      ano = int(data_nascimento[4:])

      if dia > 31 or dia < 1:
          print("DIA INVALIDO! DIGITE NOVAMENTE!")
          continue
      elif mes > 12 or mes < 1:
          print("MES INVALIDO! DIGITE NOVAMENTE!")
          continue
      elif ano > datetime.datetime.now().year:
          print("ANO INVALIDO! DIGITE NOVAMENTE!")
          continue

      break

  # insere o contato no banco de dados
  cursor.execute(''' INSERT INTO CONTATOS (nome, numero_celular, data_nascimento)
  VALUES (?, ?, ?)''', (nome, numero_celular, data_nascimento))

  print("\nCONTATO CADASTRADO COM SUCESSO !!!")

  # salva alteracoes e fecha conexão
  conexao.commit()
  cursor.close()
  conexao.close()

def leitura():
  # conecta ao banco de dados
  conexao = sql.connect('database.db')
  cursor = conexao.cursor()

  # busca todos os contatos
  cursor.execute("SELECT * FROM CONTATOS")
  dados = cursor.fetchall()  # pega todas as linhas do banco

  if not dados:
      print("NAO EXISTE CONTATOS")
  else:
      for linha in dados:
          id, nome, numero_celular, data_nascimento = linha
          # converte a data para string, mantendo zeros a esquerda
          data = str(data_nascimento).zfill(8)
          dia = int(data[:2])
          mes = int(data[2:4])

          # exibe os dados do contato
          print(f"\n[{id}] - NOME: {nome} | CELULAR: {numero_celular} | ANIVERSARIO: {dia:02}/{mes:02}/{datetime.datetime.now().year}")

  # fecha a conexao
  conexao.commit()
  cursor.close()
  conexao.close()

def atualizacao():
  # conecta ao banco de dados
  conexao = sql.connect('database.db')
  cursor = conexao.cursor()

  # busca todos os contatos
  cursor.execute("SELECT * FROM CONTATOS")
  dados = cursor.fetchall()  # pega todas as linhas do banco

  if not dados:
      print("NAO EXISTE CONTATOS")
      cursor.close()
      conexao.close()
      return
  else:
      while True:
          # escolhe como localizar o contato
          opcao = int(input(" Como deseja localizar o contato? \n [1] NOME | [2] ID: "))

          if opcao == 1:
              nome_antigo = input("Digite o nome do contato que deseja atualizar: ").strip().title()
              break
          elif opcao == 2:
              identificador = input("Digite numero do ID do contato que deseja atualizar: ")
              break
          else:
              print("OPCAO INVALIDA !!! ESCOLHA NOVAMENTE \n")

      while True:
          # escolhe qual informacao atualizar
          escolha = int(input("Deseja atualizar qual informacao? [ [1] NOME | [2] CELULAR | [3] DATA DE NASCIMENTO ]: \n Escolha: "))

          if escolha == 1:
              # atualiza o nome
              nome_novo = input("NOME: ").strip().title()
              cursor.execute("SELECT 1 FROM CONTATOS WHERE nome = ?", (nome_novo,))

              if nome_novo == ' ':
                  print("NOME INVALIDO! DIGITE NOVAMENTE!")
              elif cursor.fetchone():
                  print("NOME JA CADASTRADO! DIGITE NOVAMENTE!")
              else:
                  if opcao == 1:
                      cursor.execute("UPDATE CONTATOS SET nome = ? WHERE nome = ?", (nome_novo, nome_antigo))
                      print("NOME ALTERADO COM SUCESSO! \n")
                      conexao.commit()
                      cursor.close()
                      conexao.close()
                      return
                  elif opcao == 2:
                      cursor.execute("UPDATE CONTATOS SET nome = ? WHERE id = ?", (nome_novo, identificador))
                      print("NOME ALTERADO COM SUCESSO! \n")
                      conexao.commit()
                      cursor.close()
                      conexao.close()
                      return

          elif escolha == 2:
              # atualiza o numero de celular
              while True:
                  numero_celular = input("CELULAR [31...]: ").strip()
                  if len(numero_celular) != 11:
                      print("NUMERO DE CELULAR INVALIDO! DIGITE NOVAMENTE!")
                  else:
                      if opcao == 1:
                          cursor.execute("UPDATE CONTATOS SET numero_celular = ? WHERE nome = ?", (numero_celular, nome_antigo))
                          print("NUMERO DE CELULAR ALTERADO COM SUCESSO! \n")
                          conexao.commit()
                          cursor.close()
                          conexao.close()
                          return
                      elif opcao == 2:
                          cursor.execute("UPDATE CONTATOS SET numero_celular = ? WHERE id = ?", (numero_celular, identificador))
                          print("NUMERO DE CELULAR ALTERADO COM SUCESSO! \n")
                          conexao.commit()
                          cursor.close()
                          conexao.close()
                          return

          elif escolha == 3:
              # atualiza a data de nascimento
              while True:
                  data_nascimento = input("DATA NASCIMENTO (DDMMYYYY): ").strip()

                  if len(data_nascimento) != 8:
                      print("DATA DE NASCIMENTO INVALIDA! DIGITE NOVAMENTE!")
                      continue

                  dia = int(data_nascimento[:2])
                  mes = int(data_nascimento[2:4])
                  ano = int(data_nascimento[4:])

                  if dia > 31 or dia < 1:
                      print("DIA INVALIDO! DIGITE NOVAMENTE!")
                      continue
                  elif mes > 12 or mes < 1:
                      print("MES INVALIDO! DIGITE NOVAMENTE!")
                      continue
                  elif ano > datetime.datetime.now().year:
                      print("ANO INVALIDO! DIGITE NOVAMENTE!")
                      continue
                  else:
                      if opcao == 1:
                          cursor.execute("UPDATE CONTATOS SET data_nascimento = ? WHERE nome = ?", (data_nascimento, nome_antigo))
                          print("DATA DE NASCIMENTO ALTERADO COM SUCESSO! \n")
                          conexao.commit()
                          cursor.close()
                          conexao.close()
                          return
                      elif opcao == 2:
                          cursor.execute("UPDATE CONTATOS SET data_nascimento = ? WHERE id = ?", (data_nascimento, identificador))
                          print("DATA DE NASCIMENTO ALTERADO COM SUCESSO! \n")
                          conexao.commit()
                          cursor.close()
                          conexao.close()
                          return

          else:
              print("OPCAO INVALIDA !!! ESCOLHA NOVAMENTE \n")

def exclusao():
  # conecta ao banco de dados
  conexao = sql.connect('database.db')
  cursor = conexao.cursor()

  # busca todos os contatos
  cursor.execute("SELECT * FROM CONTATOS")
  dados = cursor.fetchall()  # pega todas as linhas do banco

  if not dados:
      print("NAO EXISTE CONTATOS")
      cursor.close()
      conexao.close()
      return

  while True:
      # escolhe como localizar o contato para exclusao
      opcao = int(input(" Como deseja localizar o contato para exlusao? \n [1] NOME | [2] ID: "))

      if opcao == 1:
          nome = input("Digite o nome do contato que deseja excluir: ").strip().title()
          cursor.execute("DELETE FROM CONTATOS WHERE nome = ?", (nome,))
          print("\nCONTATO EXCLUIDO COM SUCESSO !!! \n")
          break
      elif opcao == 2:
          identificador = input("Digite numero do ID do contato que deseja excluir: ")
          cursor.execute("DELETE FROM CONTATOS WHERE id = ?", (identificador,))
          print("\nCONTATO EXCLUIDO COM SUCESSO !!!")
          break
      else:
          print("OPCAO INVALIDA !!! ESCOLHA NOVAMENTE \n")

  # salva alteracoes e fecha conexao
  conexao.commit()
  cursor.close()
  conexao.close()

  
 

