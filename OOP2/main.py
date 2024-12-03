class CoffeeMachine:
    def __init__(self, menu, resources):
        self.menu = menu
        self.resources = resources
        self.profit = 0
        self.is_on = True

    def is_resource_sufficient(self, order_ingredients):
        for item in order_ingredients:
            if order_ingredients[item] > self.resources.get(item, 0):
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        print("Please insert coins:")
        total = int(input("How many quarters?: ")) * 0.25
        total += int(input("How many dimes?: ")) * 0.10
        total += int(input("How many nickles?: ")) * 0.05
        total += int(input("How many pennies?: ")) * 0.01
        return total

    def transaction_succeeded(self, money_received, drink_cost):
        if money_received >= drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is your change: ${change}")
            self.profit += drink_cost
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def make_drink(self, drink_name, order_ingredients):
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name} ☕. Enjoy!")

    def report(self):
        print(f"Water: {self.resources.get('water', 0)}ml")
        print(f"Milk: {self.resources.get('milk', 0)}ml")
        print(f"Coffee: {self.resources.get('coffee', 0)}g")
        print(f"Profit: ${self.profit}")

    def start(self):
        while self.is_on:
            choice = input("What would you like? (espresso/latte/cappuccino): ")
            if choice == "off":
                self.is_on = False
            elif choice == "report":
                self.report()
            else:
                drink = self.menu.get(choice)
                if drink:
                    if self.is_resource_sufficient(drink["ingredients"]):
                        payment = self.process_coins()
                        if self.transaction_succeeded(payment, drink["cost"]):
                            self.make_drink(choice, drink["ingredients"])
                else:
                    print("Invalid selection. Please choose a valid drink.")


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.0,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffee_machine = CoffeeMachine(MENU, RESOURCES)
coffee_machine.start()
