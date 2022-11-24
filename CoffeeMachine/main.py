#TODO: Our MENU needs to be added
MENU = { #Our Menu in dictionary to sell to customers
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
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
    }
}

#TODO: After the menu, resources showing how much resources we currently have to make 3 types of coffee need to be added

profit = 0 #The coffee machine has empty box in the biginning
curr_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#TODO: Checking Function if resources are enough to make products
def is_resource_enough(order_ingredients):
    """Returns True when order can be produced, False if the ingredients are not sufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= curr_resources[item]: #When we don't have enough resources to make order from customers
            print(f"Sorry there is not enough {item}")
            is_enough = False
    return is_enough

#TODO: Processing coins Function
def process_coins():
    """Returns the total calculated from inserted coins by a customer """
    print("Please insert your coins.")
    total = int(input("How many quarters ($0.25)?: ")) * 0.25
    total += int(input("How many dimes ($0.10)?: ")) * 0.10
    total += int(input("How many nickles ($0.05)?: ")) * 0.05
    total += int(input("How many pennies ($0.01)?: ")) * 0.01
    return total

#TODO: Checking if transaction successful
def is_transaction_success(money_received, coffee_cost):
    """Return True when the payment is accepted, False if payment is not sufficient to buy coffee"""
    if money_received >= coffee_cost:
        change = round(money_received - coffee_cost,2)
        print(f"Here we go! Your change is ${change}.")
        global profit # access global variable out of the function
        profit += coffee_cost
        return True
    else:
        print(f"Sorry your money is not sufficient for {order}. You get refund this amount: ${money_received}")
        return False

#TODO: Making coffee Function
def make_coffee(coffee_name, order_ingredients):
    """Subtract the required ingredients from the resources"""
    for item in order_ingredients:
        curr_resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee_name} 😘")


is_on = True #program keeps on running, initialized to turn on state

#TODO: The machine asks what type of coffee does a customer want (E/L/C)?
#TODO: Turn off the machine when entering "off" => The program keeps running until "off" entered
while is_on:
    order = input("what coffee would like? Please enter: ")
    if order == "off": #machine turns off when "off" entered
        print("Thank you and See you again 🙂")
        is_on = False
# TODO: Implementing "Print report" showing the current resources
    elif order == "report": # printing the resources values dynamically using fstring
        print(f"Water: {curr_resources['water']}ml")
        print(f"Milk: {curr_resources['milk']}ml")
        print(f"Coffee: {curr_resources['coffee']}g")
        print(f"Money: ${profit}")
#TODO: Checking if resources are enough to make products
    else:
        coffee = MENU[order]
        if is_resource_enough(coffee["ingredients"]): # if our resources are sufficient to make the order
            payment = process_coins()
            if is_transaction_success(payment,coffee["cost"]):
                make_coffee(order, coffee["ingredients"])





