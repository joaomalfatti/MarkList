import os

## Váriaveis para lista de compras
needBy = [
    
]

cart = [
    ("Milk", 5.45),
    ("Eggs", 1.83),
    ("Sugar", 8.05),
    ("Water", 20.03),
    ("Ice Cream", 30.05),
    ("Bread", 2.57)
]


print("<=:=><=:=><=:=><=:=><=:=><=:=>")
print("Vamos à lista de compras")
print("<=:=><=:=><=:=><=:=><=:=><=:=>")

### Function to show what you need to buy.
def show_available_products(cart):
    for code, cart in enumerate(cart):
        print("[{}] {} - R$ {}.".format(code, cart[0], cart[1]))
show_available_products(cart)

### Interface.