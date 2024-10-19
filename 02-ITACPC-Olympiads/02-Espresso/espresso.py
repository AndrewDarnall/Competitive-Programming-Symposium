menu = {
    "epresso" : 1,
    "espresso-doppio" : 2,
    "cappucino" : 1,
    "affogato" : 2,
    "dead-eye" : 3,
    "irish-coffee": 2
}

def get_optimal_coffee(num_orders):
    for i in range(len(num_orders)):
        if num_orders[i] == 1 and num_orders[i + 1] == 2 and num_orders[i + 2] == 1:
            num_orders.remove(1)
            num_orders[]
    

def convert_orders(orders):
    num_orders = list()
    for order in orders:
        num_orders.append(int(order))
    return num_orders

n_inputs = input("Enter number of inputs: ")
n_inputs = int(n_inputs)

print("Enter the orders: ")
orders = list()


for i in range(n_inputs):
    order = input("")
    orders.append(order)

num_orders = convert_orders(orders)