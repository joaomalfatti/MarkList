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
                needBy.append(cart.pop(cod_prod))
                print("Produto {} Adicionado ao carrinho.".format(cart[cod_prod][0]))
            else:
                print("Produto {} não adicionado ao carrinho.".format(cart[cod_prod][0]))
            
            print("\nDeseja continuar comprando? ( 0 - SIM | 1 - NÃO)")
            proceed = int(input())
            if proceed != 0:
                break
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
            
    ### <=:=><=:=><=:=>AINDA FALTA MEXER<=:=><=:=><=:=>  ###        
    elif op == 3:
        if len(needBy) == 0:
            print("Escolha o código que você deseja devolver: ")
            code = int(input())
            if code == 0:
                print("Obrigado por devolver o produto {}.".format(needBy[code][0]))
                needBy.append(cart.pop(code))

    print("")
    print("<=:=><=:=><=:=><=:=><=:=><=:=>")
    print("0 - RETORNAR AO MENU | 1 - FINALIZAR O SISTEMA")
    if int(input()) == 1:
        break