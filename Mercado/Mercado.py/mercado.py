from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: list[Produto] = []
carrinho: list[Dict[Produto, int]]


def main()-> None:
    menu()
    
def menu()-> None:
    print('===============================================')
    print('================== Bem vindo(a) ===============')
    print('=================== Geek Shop ==================')
    
    print('Selecione uma das opções abaixo: \n')
    
    print('1 - Cadastrar Produto')
    print('2 - Listar Produto')
    print('3 - Comprar Produtos')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar Pedido')
    print('6 - Sair do Sistema')
    
    opcao : int = int(input())
    
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte Sempre')
        exit(0)
    else :
        print('Opção inválida')
        sleep(1)
        menu()

def cadastrar_produto()-> None:
    print('Cadastro de Produto \n')
    
    nome: str = input('Informe o nome do produto:')
    preco: float = input('Informe o preço do produto:')
    
    produto: Produto = Produto(nome, preco)
    
    produtos.append(produto)
    
    print(f'O produto {produto.nome} foi cadastrado com sucesso')
    sleep(1)
    menu()

def listar_produto()-> None:
    if len(produtos) > 0:
        print('Listagem dos Produtos')
        for produto in produtos:
         print(produto)
         sleep(1)
    else:
        print('Ainda não existe um produto cadastrado')
    sleep(2)
    menu()

def comprar_produto()-> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho:\n')
        print('------------------------------------------------')
        print('============== Produtos Disponíveis ============')
        for produto in produtos:
            print(produto)
            print('--------------------------------------------')
            sleep(1)
        codigo: int = int(input())
        
        produto: Produto = pega_produto_por_codigo
        
        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool == False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto ] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} no carrinho')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho')
                    sleep(2)
                    menu()
                    
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho')
                sleep(2)
                menu()
        else:
            print(f'O produto com o {codigo} não foi encontrado')
            sleep(1)
            menu()
    else:
        print('Ainda não existem produtos para vender')
    sleep(2)
    menu()

def visualizar_carrinho()-> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------')
                sleep(2)
                menu()
            
    else:
        print('Ainda não existe produtos no carrinho')
    sleep(2)
    menu()
            

def fechar_pedido()-> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        print('Produtos do Carrinho')
        for item in carrinho:
            for dados in item.items():
                
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        carrinho.clear()
        sleep(3)
    else:
        print('Ainda não existe produtos no carrinho')
    sleep(2)
    menu()

def pega_produto_por_codigo(codigo: int)-> Produto:
    p: Produto = None
    
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == "__main__":
    main()