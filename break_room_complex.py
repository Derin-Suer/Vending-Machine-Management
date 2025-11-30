'''
Name           : Derin Suer
Date           : 04/11/2025
Goal           : Vending Machine Management Service program to run
'''

##IMPORTS

import time
import vending_machine


##VARIABLES

running = True
big_sep = '='*40
sep = '-'*40
vm_list = []

##PROGRAM

while running:

    #INTRO

    print(f"\n{big_sep}\n{'Welcome to the':^40}\n{'Vending Machine Management Service':^40}\n\n{'Choose one of the following options:':^40}\n\t1) Make Vending Machine \n\t2) Use Vending Machines \n\t3) Quit\n")

    while True:#repeats code till correct input is given
        try:
            option = int(input())
            if option==1 or option ==2 or option ==3:
                break
            else:
                print("incorrect input, only 1, 2 and 3 is accepted")
        except:
            print("incorrect output, must be an integer 1, 2 or 3")


    #OPTIONS

    if option==1:
        time.sleep(0.5) #for user usability
        print(f"{sep}\n{'Making a Vending Machine':^40}\nWhat is the name of your VM?\n")
        name = input()

        print(f"\nHow many items in {name}")
        while True:
            try:
                count = int(input())
                if count<=0:
                    print("There must be at least 1 item in VM")
                else:
                    break
            except:
                print("Only integers bigger than 0 are accepted")

        product_list = []

        for i in range(count):
            product = input(f"\nWhat is product {i+1}?\n") #product name

            print(f"\nHow many of {product} is there?")
            while True: #getting quantity of product
                try:
                    quantity = int(input().strip())
                    if quantity<=0:
                        print("Smallest accepted quantity is 1")
                    else:
                        break
                except:
                    print("Must be an integer")

            print(f"\nHow much is the {product}?")
            while True: #getting price for product
                try:
                    price = float(input().strip())
                    if price<0:
                        print("Smallest accepted price is 0")
                    else:
                        break
                except:
                    print("Must be a number")

            product_list.append([product, price, quantity])
        vm = vending_machine.VendingMachine(product_list)
        vm_list.append([name, vm])






    elif option==2:
        time.sleep(0.5)
        if len(vm_list)==0:
            print("\nNo vending machines created yet!\n")
        else:
            while True:#while user wants to use vending machine
                print(sep)
                print("\nAvailable Vending Machines:")
                for i in range(len(vm_list)):
                    print(f"\n{i+1}) {vm_list[i][0]}")
                    print(vm_list[i][1])

                print("\n1. Add Money\t2. Vend\t3. Refund\t4.Return")

                try:
                    vm_selection = int(input("Choice: "))
                    if vm_selection==1 or vm_selection==2 or vm_selection==3:


                        while True:
                            try:
                                vm_machine = int(input("Which Machine? "))
                                if vm_machine>len(vm_list) or vm_machine<1:
                                    print("Must be a valid vending machine")
                                else:
                                    break
                            except:
                                print("Only the number associated to the machines can be chosen")

                        if vm_selection ==1:
                            while True:
                                try:
                                    amount = float(input("How Much? "))
                                    vm_list[vm_machine-1][1].add_credit(amount)
                                    print("Processed")
                                    break

                                except:
                                    print("please input a denomination from a nickel up to $20")


                        if vm_selection ==2: #vend
                            while True:#Makes sure its a valid item in stock
                                try:
                                    item = int(input("Which Item? "))
                                    if item<=len(vm_list[vm_machine-1][1].return_product_list()) and 0<item:
                                        returned = vm_list[vm_machine-1][1].__vend__(item)
                                        print(f"You got {returned}!")
                                        break
                                    else:
                                        print("must be a valid item number")

                                except:
                                    print("Must be a valid integer")

                        if vm_selection ==3:
                            returned = vm_list[vm_machine-1][1].return_credit()
                            print(f"You got ${returned}")



                    elif vm_selection ==4:
                        print("Returning to main menu!\n")
                        break

                    else:
                        print("Only numbers 1, 2, 3, and 4 are accepted")
                except:
                    print("Must be an integer between 1 and 4")



    elif option==3:
        time.sleep(0.5)
        print(f"\n{'THANK YOU FOR YOUR VISIT!':^40}")
        running = False #Quit







