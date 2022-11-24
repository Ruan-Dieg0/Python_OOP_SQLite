#Importar o arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
ruan = Pessoa(1, "Ruan Diego")
print(ruan)

#Mostrar só o nome
print(ruan.nome)

#Chama o objeto de banco de dados
db = Database()

#Instancia o objeto
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#Carregar uma lista que veio do banco de dados
pessoas = pessoaDAO.getAll()
for pessoa in pessoas:
  print(pessoa)



