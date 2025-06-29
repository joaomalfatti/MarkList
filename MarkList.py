import os

## Váriaveis para lista de compras
needBy = [
    
]

cart = [
    ("Leite", 5.00),
    ("Ovos", 1.00),
    ("Açucar", 8.00),
    ("Água", 20.00),
    ("Sorvete", 30.00),
    ("Pão", 2.00)
]


print("<=:=><=:=><=:=><=:=><=:=><=:=>")
print("Vamos à lista de compras")
print("<=:=><=:=><=:=><=:=><=:=><=:=>")
print("")

### Function to show what you need to buy.
def show_available_products(cart):
    for code, cart in enumerate(cart):
        print("[{}] {} - R$ {:.2f}.".format(code, cart[0], cart[1]))
show_available_products(cart)

### Interface.

while True:
    os.system("cls")
    print("<=:=><=:=><=:=><=:=><=:=><=:=>")
    print("Vamos à lista de compras")
    print("<=:=><=:=><=:=><=:=><=:=><=:=>")
    print("")
    
    print("0 - Mostrar Produtos Disponíveis | 1 - Fazer às compras | 2 - Visualizar o carrinho. | 3 - Devolver Produtos")
    op = int(input())
    os.system("cls")

    ### <=:=><=:=><=:=>OK<=:=><=:=><=:=>  ###
    if op == 0:
        show_available_products(cart)
        
    elif op == 1:
        while True:
            show_available_products(cart)
            print("")
            print("<=:=><=:=><=:=><=:=><=:=><=:=>")
            print("Escolha o código do produto: ")
            cod_prod = int(input())
            os.system("cls")

            print("Você escolheu o {}.".format(cart[cod_prod][0]))
            print("0 - SIM | 1 - NÃO")
            conf = int(input())

            if conf == 0:
                print("Produto {} Adicionado ao carrinho.".format(cart[cod_prod][0]))
                needBy.append(cart.pop(cod_prod))
            else:
                print("Produto {} não adicionado ao carrinho.".format(cart[cod_prod][0]))
            
            print("\nDeseja continuar comprando? ( 0 - SIM | 1 - NÃO)")
            proceed = int(input())
            if proceed != 0:
                break
            os.system("cls")

    elif op == 2:
        if len(needBy) == 0:
            print("Carrinho vazio")
        else:
            print("Carrinho Atual")
            show_available_products(needBy)
            print("")
            print("O valor do carrinho atual está: ")
            total = sum([cart[1] for cart in needBy])
            print("O Total atual é: R$ {:.2f}.".format(total))
    
    elif op == 3:
        total = 0.0
        print("Produtos no carrinho:")
        show_available_products(needBy)
        total = sum([cart[1] for cart in needBy])
        print("Total do carrinho é: R$ {:.2f}".format(total))

        if len(needBy) == 0:
            print("Não a produtos para devolver.")
        else:
            print("")
            print("Escolha o código do produto para devolver: ")
            cod = int(input())

            if 0 <= cod < len(needBy):
                print("<=:=><=:=><=:=><=:=><=:=><=:=>")
                item = needBy[cod]
                print("Você devolveu o produto {}".format(item[0]))             
                cart.append(needBy.pop(cod))
                total = sum([cart[1] for cart in needBy])
                print("Com a devolução do produto, valor do carrinho é: R$ {:.2f}.".format(total))
            else:
                print("Código inválido.")

    print("")
    print("<=:=><=:=><=:=><=:=><=:=><=:=>")
    print("0 - RETORNAR AO MENU | 1 - FINALIZAR O SISTEMA")
    if int(input()) == 1:
        break