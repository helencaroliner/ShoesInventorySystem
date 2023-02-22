import os
usage_message = '''
Welcome to the Inventory system. What would you like to do?
1. Read database.
2. Add a new shoe.
3. View all shoes.
4. Re-stock shoes.
5. Search for a shoe.
6. Calculate the total value for each item.
7. Find the product with the highest quantity for sale.
8. Quit.
'''

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        pass
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        pass
        return self.cost


    def get_quantity(self):
        pass
        return self.quantity

    def __str__(self):
        pass
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"

from tabulate import tabulate

#=============Shoe list===========
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    try:
        with open ("inventory.txt", 'r') as file:
            lines = file.readlines()[1:] #Skip header line
            for line in lines:
                country, code, product, cost, quantity = line.strip().split(',')
                cost = float(cost)
                quantity = int(quantity)
                shoe =Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("File not found. Please make sure 'inventory.txt' is the same directory as the script.")
    except Exception as e:
        print(f"Error occured while reading the file: {str(e)}")
    print("Database read.")
    
def capture_shoes():
    try:
        country = input("Enter the country: ")
        code = input("Enter the code: ")
        product = input("Enter the product: ")
        cost = float(input("Enter the cost: "))
        quantity = int(input("Enter the quantity: "))
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)
        print(f"{product} added to inventory")
    except ValueError:
        print("Invalid input. Cost and quantity must be numeric values.")
    except Exception as e:
        print(f"Error occured while capturing shoe: {str(e)}")

def view_all():
    table = []
    try:
        for shoe in shoe_list:
            table.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
        print(tabulate(table, headers=['Country','Code', 'Product', 'Cost', 'Quantity']))
    except Exception as e:
        print("Error occured while trying to view all shoes:", str(e))

def re_stock():
    try:
        min_quantity = float('inf')
        min_shoe = None
        for shoe in shoe_list:
            if shoe.quantity < min_quantity:
                min_quantity = shoe.quantity
                min_shoe = shoe

        print(f"The following shoe needs to be restocked: {min_shoe.product} ({min_shoe.code}), Quantity: {min_quantity}")
        answer = input(f"Do you want to add more shoes for {min_shoe.product}? (y/n)")
        if answer.lower() == "y":
            quantity = int(input("Enter quantity to add: "))
            min_shoe.quantity += quantity
            print("Inventory updated.")

            #Update the file with the new quantity
            with open("inventory.txt",'r') as file:
                lines = file.readlines()
            with open("inventory.txt", 'w') as file:
                file.write(lines[0]) #Write the header line
                for shoe in shoe_list:
                    file.write(f"{shoe.country}, {shoe.code},{shoe.product}, {shoe.cost}, {shoe.quantity}\n")
    except ValueError:
        print("Invalid input. Please try again")
    except Exception as e:
        print(f"Error occured while reestocking shoe: {str(e)}")

def search_shoe(shoe_code):
    pass
    try:
        for shoe in shoe_list:
            if shoe.code == shoe_code:
                return shoe
        return None
    except Exception as e:
        print("Error occurred while trying to search for a shoe:", str(e))

def value_per_item():
    pass
    try:
        for shoe in shoe_list:
            value = shoe.cost * shoe.quantity
            print(f"{shoe.product}: {value}")
    except Exception as e:
        print("Error occured while trying to calculate the value per item:", str(e))

def highest_qty():
    pass
    try:
        highest_quantity_shoe = max(shoe_list, key=lambda shoe:shoe.quantity)
        print(f"{highest_quantity_shoe.product} is for sale with the highest quantity of {highest_quantity_shoe.quantity}")
    except Exception as e:
        print("Error occurred while trying to determine the product with the highest quantity:", str(e))


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:
    print(usage_message)

    try:

        option = int(input("Select an option from the menu above: "))

        if option == 1:
            read_shoes_data()

        elif option == 2:
            capture_shoes()
        
        elif option == 3:
            view_all()
        
        elif option == 4:
            re_stock()
        
        elif option == 5:
            shoe_code = input("Enter the shoe code to search for: ")
            shoe = search_shoe(shoe_code)
            if shoe:
                print(shoe)
            else:
                print("Shoe not found. Please try again.")
                
        elif option == 6:
            value_per_item()
        
        elif option == 7:
            highest_qty()
        
        elif option == 8:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select a number from 1 to 8.")
    except ValueError:
        print("Invalid input. Please select a number from 1 to 8.")
