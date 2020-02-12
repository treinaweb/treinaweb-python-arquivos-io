from contato import Contato
from arquivo_service import *

print("-" * 30)
print(("-" *3) + " Agenda de contatos TW " + ("-" *3))
print("-" * 30)
opcao_menu = 1
while(opcao_menu != 0):
    print("1. Listar contatos")
    print("2. Cadastrar contato")
    print("3. Remover contato")
    print("4. Buscar contato")
    print("0. Sair")
    opcao_menu = int(input("Digite a opção desejada: "))

    if opcao_menu == 1:
        contatos = listar_contatos()
        for contato in contatos:
            print(f"nome: {contato.nome} / email: {contato.email} / telefone: {contato.telefone}")
    if opcao_menu == 2:
        nome_contato = input("Digite o nome do contato: ")
        email_contato = input("Digite o email do contato: ")
        telefone_contato = input("Digite o telefone do contato: ")
        contato_novo = Contato(nome_contato, email_contato, telefone_contato)
        if cadastrar_contato(contato_novo):
            print("Contato cadastrado com sucesso")
        else:
            print("Contato já existe")

    elif opcao_menu == 4:
        contato_buscar = input("Digite o email do contato que deseja buscar: ")
        contato_encontrado = buscar_contato_email(contato_buscar)
        if contato_encontrado:
            print(f"nome: {contato_encontrado.nome} / email: {contato_encontrado.email} / telefone: {contato_encontrado.telefone}")
        else:
            print("Contato não encontrado")
    else:
        print("opcao invalida")
else:
    print("Obrigado por usar a agenda de contatos TW")