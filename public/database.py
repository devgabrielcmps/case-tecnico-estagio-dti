# Desenvolvedor: Gabriel Campos Amaral Ribeiro
# Resolução do Case do Processo Seletivo para Estágio – DTI Digital
# CRUD - AGENDA

#importa o pack sqlite para a aplicacao
import sqlite3 as sql
import datetime

#criacao do banco de dados
def criaBanco():
  conexao=sql.connect('database.db') #inicia a conexao com o banco ou cria se necessario

  cursor = conexao.cursor() #inicializa o cursos que o q permite criar,excluir no banco

  cursor.execute('''CREATE TABLE IF NOT EXISTS CONTATOS 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 nome TEXT NOT NULL,
                 numero_celular TEXT NOT NULL,
                 data_nascimento DATE )
                 ''')
  
  conexao.commit()
  cursor.close()
  conexao.close()
 

def cadastro():

  conexao=sql.connect('database.db')
  cursor = conexao.cursor()

  #VALIDACAO DAS INFORMACOES 
  while(True):
    nome=input("NOME: ").strip().capitalize() #pede ao usuario o nome e tira espacos inuteis com .strip e coloca somente a primeira letra maiuscula com .capitalize

    cursor.execute("SELECT 1 FROM CONTATOS WHERE nome = ?",(nome,)) #faz a verificacao se ja existe o nome no banco de dados (colocar de onde eu tirei isso)

    if(nome == ' '):
      print("NOME INVALIDO! DIGITE NOVAMENTE!")
    elif cursor.fetchone():
      print("NOME JA CADASTRADO! DIGITE NOVAMENTE!")
    else:
      break
  
  while(True):
    numero_celular=input("CELULAR [31...]: ").strip()
    if (len(numero_celular) != 11):
      print("NUMERO DE CELULAR INVALIDO! DIGITE NOVAMENTE!")
    else:
      break
  
  while(True):
    data_nascimento=input("DATA NASCIMENTO (DDMMYYYY): ").strip()
    
    if (len(data_nascimento) != 8):
      print("DATA DE NASCIMENTO INVALIDA! DIGITE NOVAMENTE!")
      continue

    dia=int(data_nascimento[:2])
    mes=int(data_nascimento[2:4])
    ano=int(data_nascimento[4:])

    if (dia>31 or dia<1):
      print("DIA INVALIDO! DIGITE NOVAMENTE!")
      continue
    elif(mes>12 or mes<1):
      print("MES INVALIDO! DIGITE NOVAMENTE!")
      continue
    elif(ano>datetime.datetime.now().year):
      print("ANO INVALIDO! DIGITE NOVAMENTE!")
      continue
    
    break

  cursor.execute(''' 
  INSERT INTO CONTATOS (nome,numero_celular,data_nascimento)
  VALUES (?,?,?)
  ''',(nome,numero_celular,data_nascimento))

  print("\nCONTATO CADASTRADO COM SUCESSO !!! \n")

  conexao.commit()
  cursor.close()
  conexao.close()

  
def leitura():
  #se nao existir nada la dentro precisa reclamar
  pass

def atualizacao():
  #se nao existir nada la dentro precisa reclamar
  pass

def exclusao():
  #se nao existir nada la dentro precisa reclamar
  pass

