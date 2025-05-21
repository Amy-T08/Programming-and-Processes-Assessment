# This is a shopping cart program that the user can add, remove or view the items in the cart

shopping_cart = {}
item_list = {'banana':2.50,
             'apple':0.50,
             'grape':2.00,
             'milk':5.00,
             }
total_price = {}

#using def funtion for different part of the program

def add():#using def funtion to add items to the dictionary
    print('If want to stop just enter finish')
    print('Item List')
    for items,price in item_list.items():#using for loop to print the items and price one after the other
        print(f'{items} - ${price}')
    while True:
        try:
            add_item = input('Enter the item you want to add from the item list: ')
            if add_item == 'finish':#letting user to add how many ever things they want  
                break       
            elif add_item.isalpha():#making sure user only eneter letters not numbers 
                item_q = int(input(f'How many {add_item} do you want?: '))#asking user to enter quantity of item
            else:
                print('invaild input, please enter only letters')#asking user to enter again after a error 
        except ValueError:
            print('Field can not be empty')#friendly reminder to tell the user what to do 
        try:#traping error
            if item_q == '':
                print("This field can't be empty")
            else:
                shopping_cart[add_item] = item_q #storing the item and its quantitiy into a dictionary
        except ValueError:
            print('invaild input, please enter number only')

def remove():#def funtion to remove items from the dictionary
    print('If want to stop just enter finish')
    while True:#loop over and over again until user say to stop
        remove_item = input('Enter the item you want to remove: ')
        if remove_item == 'finish':
            break
        elif remove_item.isalpha():#making user to enter only letters
            if remove_item in shopping_cart:#checking if the item is in the dictionary
                shopping_cart.pop(remove_item)#removing item from the dictionary
            else:
                print('The item is not find in cart')
        else:
            print('invaild input, please enter only letters')
#using funtion for the user to be able to view what is in their cart
def view():
    for items,quantity in shopping_cart.items():#for loop to print each item and their quantity on by one
        print(f'- {items} x{quantity}')

def check_out():# Use zip and a dictionary constructor to create the product dictionary
    total = dict(zip(shopping_cart, (shopping_cart[key] * item_list[key] for key in shopping_cart)))
    for item,price in total.items():
        print(f'{item} = ${price}')
    total_price = sum(total.values())
    print(f'The total price is: ${total_price}')


def main():
    print('Welcome')
    while True:#looping until user say to stop
        print('-----------------')
        print('1.add')
        print('2.remove')
        print('3.view cart')
        print('4.check out')
        print('5.exit')
        print('-----------------')
        choice = int(input('Enter what you want to do (1-5): '))
        if choice == 1:
            add()
        elif choice == 2:
            remove()
        elif choice == 3:
            view()
        elif choice == 4:
            check_out()
            user_input = input('Do you want to continue shopping? (y or n): ')
            if user_input == 'n':
                print('Thank you for using the program')
                break
            else:
                print('Let continue shopping')
        else:
            print('Thank you for using the program')
            break

main()
    
