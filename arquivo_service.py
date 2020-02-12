from contato import Contato

def listar_contatos():
    lista_contatos = list()
    try:
        with open("contatos.txt", "r") as arquivo:
            lista_contatos_arquivo = arquivo.readlines()
            for i in lista_contatos_arquivo:
                dados = (i.split('-'))
                contato_arquivo = Contato(dados[0][:-1], dados[1][1:-1], dados[2][1:-1])
                lista_contatos.append(contato_arquivo)
        return lista_contatos
    except FileNotFoundError:
        print("Arquivo não encontrado")

def cadastrar_contato(contato_novo):
    try:
        with open("contatos.txt", "a") as arquivo:
            arquivo.write(f"{contato_novo.nome} - {contato_novo.email} - {contato_novo.telefone} \n")
    except FileNotFoundError:
        print("Arquivo não encontrado")