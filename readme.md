# Documentação – Case Técnico dti
## Sistema de Cadastro de Contatos
**Autor:** Gabriel Campos Amaral Ribeiro

## Descrição  
Este projeto é um **CRUD** (Create, Read, Update, Delete) de um sistema de cadastro de contatos, desenvolvido como parte do **case técnico para estágio na DTI Digital**.  
O sistema permite cadastrar, listar, atualizar e excluir contatos, armazenando os dados em um **banco SQLite** local.  

> A aplicação deve ser executada a partir do arquivo **main.py**, que está dentro da pasta **public**.

---

## Funcionalidades  
- **Cadastrar contato**: Nome, número de celular e data de nascimento (com validação).  
- **Listar contatos**: Exibe todos os contatos cadastrados.  
- **Atualizar contato**: Permite localizar por **nome** ou **ID** e atualizar **nome, celular ou data de nascimento**.  
- **Excluir contato**: Permite localizar por **nome** ou **ID** e excluir o contato.  

---

## Requisitos  
- Python 3.x  
- Bibliotecas inclusas no Python:  
  - `sqlite3`  
  - `datetime`  

> Caso necessário, instale via terminal do VSCode:  
> `pip install sqlite3`  

---

## Uso do Sistema  

### 1. Cadastrar Contato  
Solicita ao usuário: nome, número de celular e data de nascimento (opcional).  

**Validações:**  
- Nome único  
- Celular com 11 dígitos  
- Data válida (se informada)  

### 2. Listar Contatos  
Exibe todos os contatos cadastrados no banco.  

### 3. Atualizar Contato  
Permite localizar pelo **nome** ou **ID**.  

**Campos que podem ser atualizados:**  
- Nome  
- Número de celular  
- Data de nascimento (opcional)  

### 4. Excluir Contato  
Permite localizar pelo **nome** ou **ID** e excluir o registro.  

---

## Estrutura do Projeto  
| Arquivo            | Descrição                                         |  
|-------------------|---------------------------------------------------|  
| **public/main.py**   | Menu principal e execução da aplicação           |  
| **public/database.py** | Funções CRUD e criação do banco de dados (`criaBanco()`) |  

> Observação: Não foi possível colocar o banco de dados dentro de uma pasta separada (`db`) devido à complexidade de acessar o arquivo SQLite corretamente; ele permanece na raiz do projeto.

O banco de dados (**database.db**) e a tabela **CONTATOS** são criados automaticamente na primeira execução.  

---

## Observações Técnicas  
- O projeto é modularizado, separando responsabilidades entre arquivos, facilitando manutenção e expansão futura.  
- A função `criaBanco()` cria automaticamente o banco e a tabela caso não existam.  
- O campo **data_nascimento** é opcional e, caso não seja informado, será exibido como “Não informado” ao listar contatos.  
- Todas as entradas do usuário são validadas para garantir a integridade dos dados.  
- Para desenvolvimento e consulta de informações, foram utilizadas as seguintes fontes:  
  - **DevMedia**  
  - **Documentação oficial Python**  
  - **Documentação SQL**  
  - **Documentação SQLite para Python**  
- Durante o desenvolvimento, também utilizei **IA** para resolução de problemas como erros de compilação e para tirar dúvidas técnicas.  
