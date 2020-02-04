from contato import Contato

print("-" * 30)
print(("-" *3) + " Agenda de contatos TW " + ("-" *3))
print("-" * 30)

opcao_menu = 1
lista_contatos = list()

while(opcao_menu != 0):
    print("1. Listar contatos")
    print("2. Cadastrar contato")
    print("3. Remover contato")
    print("4. Buscar contato")
    print("0. Sair")
    opcao_menu = int(input("Digite a opção desejada: "))

    if opcao_menu == 1:
        for i in lista_contatos:
            print(f"nome: {i.nome} / email: {i.email} / telefone: {i.telefone}")
    elif opcao_menu == 2:
        nome_contato = input("Digite o nome do contato: ")
        email_contato = input("Digite o email do contato: ")
        telefone_contato = input("Digite o telefone do contato: ")
        contato_novo = Contato(nome_contato, email_contato, telefone_contato)
        lista_contatos.append(contato_novo)
    elif opcao_menu == 3:
        contato_remover = input("Digite o email do contato que deseja remover: ")
        contato_encontrado = False
        for i in lista_contatos:
            if i.email == contato_remover:
                lista_contatos.remove(i)
                print("Contato removido")
                contato_encontrado = True
                continue
        if not contato_encontrado:
            print("Contato não encontrado")
    elif opcao_menu == 4:
        contato_buscar = input("Digite o email do contato que deseja buscar: ")
        contato_encontrado = False
        for i in lista_contatos:
            if i.email == contato_buscar:
                print(f"nome: {i.nome} / email: {i.email} / telefone: {i.telefone}")
                contato_encontrado = True
                continue
        if not contato_encontrado:
            print("Contato não encontrado")

    else:
        print("opcao invalida")
else:
    print("Obrigado por usar a agenda de contatos TW")