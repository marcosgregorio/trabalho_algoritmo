codigoProd = [2323, 2324, 2325]
nomeProd = ["Leite de pedra", "Sal de Pão", "Bixcoito"]
# listas globais para o uso do programa
precoProd = [20.5, 1.0, 4.0]
quantProd = [2, 4, 20]


class Produto:  # classe para o produto
    codigo = 0
    nome = ""
    preco = 0.0
    quant = 0


def lin():  # função de printar linhas
    print("-" * 30)


def lin2():  # função de printar linhas secundária
    print("-" * 35)


def relatorio():
    print("")
    lin2()
    print("|\033[1;32mCódigo\033[m")
    print(f"|\033[;32m{codigoProd}\033[m")  # relatório com cores!
    lin2()
    print("|\033[1;33mNome\033[m")
    print(f"|\033[;33m{nomeProd}\033[m")
    lin2()
    print("|\033[1;34mPreço\033[m")
    print(f"|\033[;34m{precoProd}\033[m")
    lin2()
    print(f"|\033[1;35mQuantidade\033[m")
    print(f"|\033[;35m{quantProd}\033[m")
    lin2()

    print("")


def verif_posicao(codigo):
    for i in range(len(codigoProd)):
        # verifica a posição e me retorna ela. Caso não ache, me retorna -1!
        if codigo == codigoProd[i]:
            return i
    return -1


def verif_nome(nome):
    for i in range(len(codigoProd)):
        if nome == nomeProd[i]:
            return i
    return -1


def cadastrar():  # função de cadastrar um produto
    prod = Produto()
    while True:
        prod.codigo = int(input("Digite o código que quer cadastrar: "))
        valor = verif_posicao(prod.codigo)
        if valor != -1:
            print(
                f"\033[0;31mO código \"{prod.codigo}\" já está cadastrado!\033[m")
        else:
            if prod.codigo <= 0:
                print(
                    "\033[0;31mInsira um número válido para o cadastramento!\033[m")
            else:
                break

    while True:
        prod.nome = str(input("Digite o nome que quer cadastrar: "))
        valor = verif_nome(prod.nome)
        if valor != -1:
            print(
                f"\033[0;31mO nome \"{prod.nome}\" já está cadastrado\033[m ")
        else:
            break

    while True:
        prod.preco = float(input("Digite o preço que quer cadastrar: R$"))
        if prod.preco <= 0:
            print("\033[0;31mInsira um valor maior que zero!\033[m")
        else:
            break
    while True:
        prod.quant = int(input("Digite a quantidade que queira cadastrar: "))
        if prod.quant <= 0:
            print("\033[0;31mInsira uma quantidade maior que zero!\033[m")
        else:
            break

    codigoProd.append(prod.codigo)
    nomeProd.append(prod.nome)
    precoProd.append(prod.preco)
    quantProd .append(prod.quant)
    return codigoProd, nomeProd, precoProd, quantProd


def atualizarProd():  # função para atualizar o produto
    while True:
        codigoProduto = int(
            input("Insira o Código do produto que deseja alterar ou -9 para sair: "))
        if codigoProduto == -9:
            return
        pos = verif_posicao(codigoProduto)
        if pos == -1:
            print("\033[1;31mCódigo inválido! Digite novamente.\033[1;31m")
        else:
            break
    while True:
        precoNovo = float(input("Digite o novo preço:R$ "))
        if precoNovo <= 0:
            print(
                "\033[1;31mValor invalido, insira um valor maior que zero!\033[m")
        else:
            break
    while True:
        quantNova = int(input("Digite uma nova quantidade: "))
        if quantNova <= 0:
            print("Quantidade inválida! Digite novamente.")
        else:
            precoProd[pos] = precoNovo
            quantProd[pos] = quantNova
            return precoProd, quantProd


def consultarProd():  # função para consultar um produto pelo codigo
    while True:
        codigoProduto = int(input(
            "\n Digite o código de produto que deseja consultar ou digite -1 para sair: "))
        for i in range(len(codigoProd)):
            if codigoProduto == -1:
                return
            else:
                if codigoProduto == codigoProd[i]:
                    lin2()
                    print('\033[1;33m|código|', codigoProd[i], 'nome|', nomeProd[i], '|preço|',
                          'R$', precoProd[i], '|Quantidade|', quantProd[i], '|\033[m')
                    lin2()


def registrarCompra():  # função para efetuar uma compra
    total = 0
    compraCodigo = []
    compraNome = []
    compraPreco = []
    compraQuant = []
    while True:
        # \033[m é uma função de mudar cor!
        codigoProduto = int(input(
            "Insira o Código do produto que deseja \033[1;30;40mCOMPRAR:\033[m ou -9 para sair: "))
        pos = verif_posicao(codigoProduto)
        if codigoProduto == -9:
            break
        if pos == -1:
            print("Código inválido! Digite novamente.")
        else:
            print(f"Você selecionou \033[0;94m{nomeProd[pos]}\033[m")
            quantidadeUser = int(input("Quantas unidades quer?: "))
            if quantidadeUser <= 0:
                print(
                    "\033[31mQuantidade inválida! Selecione uma quantidade maior que 0!\033[m")
            else:
                q = quantProd[pos] - quantidadeUser
                if q <= -1:
                    print(
                        "\033[1;31m\nQuantidade superior a quantidade em estoque!\033[m")
                    print(
                        f"\033[1;33mTemos {quantProd[pos]} em estoque.\033[m")
                else:
                    total += quantidadeUser * precoProd[pos]
                    quantProd[pos] = q
        compraCodigo.append(codigoProd[pos])
        compraNome.append(nomeProd[pos])
        compraPreco.append(precoProd[pos])
        compraQuant.append(quantidadeUser)

    while True:
        if quantidadeUser <= 0:
            print("\n\33[31mNenhuma compra efetuada!\033[m")
            return
        else:
            print("\n|Código---------Descrição-----Preço(R$)----Quant(UN)----Total(R$)|")

            for i in range(len(compraCodigo)):
                print(
                    f"| {compraCodigo[i]:<7}{compraNome[i]:<10}       {compraPreco[i]:<10}     {compraQuant[i]:<4}            {compraPreco[i] * compraQuant[i]}|")

            print(f"\nValor total:R${total:>7}")
            return


def menu():

    lin()
    print(' \033[1;31;47m    MERCADO DO MARCOLA      \033[m')
    lin()
    print(" ")
    lin2()
    print("|\tCadastrar Produto, digite: 1|")
    lin2()
    print("|\tAtualizar Produto, digite: 2|")
    lin2()
    print("|\tComprar, digite: 3\t    |")
    lin2()
    print("|\tConsultar Produto, digite: 4|")
    lin2()
    print("|\tRelatório, digite: 5        |")
    lin2()
    print("|\tSair do Programa, digite: -1|")
    lin2()
    return int(input('\n O que deseja fazer? '))


while True:
    opcao = menu()
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        atualizarProd()

    elif opcao == 3:
        registrarCompra()

    elif opcao == 4:
        consultarProd()

    elif opcao == 5:
        relatorio()

    elif opcao == -1:
        break
