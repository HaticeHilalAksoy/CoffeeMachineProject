
MENU={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.0,},
  
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
        },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
        },
}
profit=0
resources ={
    "water":300,
    "milk":200,
    "coffee":100,
}
def is_resource(order_ingredient):
    is_enough = True
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"sorry there is not enough {item}.")
            is_enough = False
    return is_enough

def process_coins():
    print("please insert coins:")
    total = int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: "))*0.1
    total += int(input("how many nickles?: "))*0.05
    total += int(input("how many pennies?: "))*0.01
    return total
def transaction_succeeded(money_received,drink_cost):
    if money_received>= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"here is the change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"sorry enough money")
        return False
def make_the_drink(drink_name,order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"making {drink_name} ☕ ")

is_on= True
while is_on:
    choice= input("what would you like to (espresso/latte/cappuccino):")
    if choice == "off":
       is_on=False
    elif choice== "report":
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}ml")
        print(f"Total cost: ${profit}")
    else:
        drink =MENU[choice]
        if is_resource(drink["ingredients"]):
            payment=process_coins()
            if transaction_succeeded(payment,drink["cost"]):
                make_the_drink(choice,drink["ingredients"])


