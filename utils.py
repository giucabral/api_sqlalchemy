from models import Pessoas


# insere um registro na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Giuliano', idade=43)
    print(pessoa)
    pessoa.save()


# Faz uma consulta geral na tabela pessoa
def consulta():
    pessoas = Pessoas.query.all()
    # for i in pessoa:
    #     print(i.nome)
    print(pessoas)


# Consulta um registro específico na tabela pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.filter_by(nome="Giuliano").first()
    print(pessoa.nome)
    print(pessoa.idade)


# Altera um registro específico na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Giuliano').first()
    pessoa.idade = 40
    # pessoa.nome = "Giuliano"
    pessoa.save()


# Exclui um registro específico na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Giuliano').first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_pessoas()
    # altera_pessoa()
    exclui_pessoa()
    consulta()
    #consulta_pessoas()