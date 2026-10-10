coffee_menu={
    "Espresso":350,
    "Cappuccino":450,
    "Latte":450,
    "Americano":400,
    "Mocha":600
}

Pastries_n_Snacks={
    "Blueberry-Muffin":350,
    "Chocolate Chip Cookie":300,
    "Croissant":400,
    "Cinnamon Roll":250
}

def display_menu():
    print("=====Coffee Shop Menu=====")
    print("\nCoffee:")
    for item, price in coffee_menu.items():
        print(item, ":", price)
    
    print("\nPastries & Snacks:")
    for item, price in Pastries_n_Snacks.items():
        print(item, ":", price)
    
    print("============================")

display_menu()


def get_coffee_choice():
     while True:
            choice = input("Enter the coffee you want: ").strip()
    
            if choice.isdigit():
                print("Enter a coffee name, not a number.")
    
            elif choice.lower() in [item.lower() for item in coffee_menu]:
    
                for item in coffee_menu:
                    if choice.lower() == item.lower():
                        choice = item
                        break
    
                print("You selected:", choice)
                return choice
    
            else:
                print("Coffee not found.")


def get_coffee_quantity():
      while True:
            try:
                coffee_quantity = int(input("Enter coffee quantity: "))
    
                if coffee_quantity > 0:
                    return coffee_quantity
                else:
                    print("Quantity must be greater than zero.")
    
            except ValueError:
                print("Enter a valid number.")




def take_coffee_order():
    coffee_order = []
    while True:
        choice = get_coffee_choice()
        coffee_quantity = get_coffee_quantity()
        coffee_order.append((choice, coffee_quantity))

        while True:
            add_coffee = input("Would you like to add another coffee (y/n): ").strip().lower()

            if add_coffee == "y":
                break

            elif add_coffee == "n":
                break

            else:
                print("Only enter y or n.")

        if add_coffee == "n":
                break
            
    return coffee_order
coffee_order = take_coffee_order()

    
    
def display_coffee_bill(coffee_order):
    print("\n===== Coffee Order =====")
    for coffee, quantity in  coffee_order:
        price=coffee_menu[coffee]*quantity
        print(coffee,"x",quantity,"=",price)
    print("==========")
display_coffee_bill(coffee_order)


    

def coffee_total(coffee_order):
    coffee_total = 0

    for coffee, quantity in coffee_order:
        coffee_total = coffee_total + coffee_menu[coffee] * quantity

    return coffee_total

coffee_total = coffee_total(coffee_order)



def get_snack_choice():
    while True:
        add_snack = input("Would you like to have pastry or snack? (y/n): ").strip().lower()

        if add_snack == "y":
            return add_snack

        elif add_snack == "n":
            return add_snack

        else:
            print("Only enter y or n.")






def get_snack_item():
    while True:
                snack_choice = input("Enter the snack or pastry you want: ").strip()
    
                if snack_choice.isdigit():
                    print("Enter the pastry or snack name, not a number.")
    
                elif snack_choice.lower() in [item.lower() for item in Pastries_n_Snacks]:
    
                    for item in Pastries_n_Snacks:
                        if snack_choice.lower() == item.lower():
                            snack_choice = item
                            break
    
                    print("You selected:", snack_choice)
                    return snack_choice
    
                else:
                    print("Pastry or snack not found.")


def get_snack_quantity():
    while True:
        try:
            snack_quantity = int(input("Enter snack/pastry quantity: "))
            if snack_quantity > 0:
                    return snack_quantity

            else:
                    print("Quantity must be greater than zero.")

        except ValueError:
                print("Enter a valid number.")



def take_snack_order():
    add_snack = get_snack_choice()

    if add_snack == "n":
        print("No pastry or snack selected.")
        return []

    snack_order = []

    while True:
        snack_choice = get_snack_item()
        snack_quantity = get_snack_quantity()

        snack_order.append((snack_choice, snack_quantity))

        while True:
            add_another_snack = input(
                "Would you like to add another snack (y/n): "
            ).strip().lower()

            if add_another_snack == "y":
                break

            elif add_another_snack == "n":
                break

            else:
                print("Only enter y or n.")

        if add_another_snack == "n":
            break

    return snack_order
snack_order = take_snack_order()




def display_snack_bill(snack_order):
    print("\n===== Snack Bill =====")

    for snack, quantity in snack_order:
        price = Pastries_n_Snacks[snack] * quantity
        print(snack, "x", quantity, "=", price)

    print("======================")
display_snack_bill(snack_order)



def calculate_snack_total(snack_order):
    snack_total = 0

    for snack, quantity in snack_order:
        snack_total = snack_total + Pastries_n_Snacks[snack] * quantity

    return snack_total
snack_total=calculate_snack_total(snack_order)
    


def display_final_bill(coffee_total, snack_total):
    total = coffee_total + snack_total

    print("\n===== Final Bill =====")
    print("Coffee Total:", coffee_total)
    print("Snack Total:", snack_total)
    print("Total:", total)
    print("======================") 
display_final_bill(coffee_total, snack_total)


