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
        if buscar_contato_email(contato_novo.email):
            return False
        else:
            with open("contatos.txt", "a") as arquivo:
                arquivo.write(f"{contato_novo.nome} - {contato_novo.email} - {contato_novo.telefone} \n")
            return True
    except FileNotFoundError:
        print("Arquivo não encontrado")

def buscar_contato(email_contato):
    try:
        with open("contatos.txt", "r") as arquivo:
            lista_contatos = arquivo.readlines()
            for i, linha in enumerate(lista_contatos):
                dados = (linha.split('-'))
                if dados[1][1:-1] == email_contato:
                    return i
            else:
                return -1
    except FileNotFoundError:
        print("Arquivo não encontrado")

def buscar_contato_email(email_contato):
    try:
        linha = buscar_contato(email_contato)
        if linha >= 0:
            with open("contatos.txt") as arquivo:
                lista_contatos = arquivo.readlines()
                dados = lista_contatos[linha].split('-')
                contato_encontrato = Contato(dados[0][:-1], dados[1][1:-1], dados[2][1:-1])
            return contato_encontrato
    except FileNotFoundError:
        print("Arquivo não encontrado")
