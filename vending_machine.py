'''
Name           : Derin Suer
Date           : 04/11/2025
Goal           : Vending Machine Management Service class
'''

class VendingMachine:

    def __init__(self, product_list : list, ):
        '''
        2d list of products represents the 3 data points needed for the vending machine
        consumables : 2d product list [[name, price, quantity]].
        '''
        self.__product_list = product_list
        self.__revenue = 0
        self.__credit = 0



    def __vend__(self, product_number : int):
        '''
        requests the product number, checks list if item exists, is in stock, and also user has
        enough credits, then vends said item
        '''
        try:
            if self.__product_list[product_number-1][2]>0 and self.__product_list[product_number-1][1]<=self.__credit:
                self.__product_list[product_number-1][2] -= 1
                self.__credit -= self.__product_list[product_number-1][1]
                self.__revenue+= self.__product_list[product_number-1][1]
                return self.__product_list[product_number-1][0]
            else:
                return "Nothing"
        except:
            return "Nothing"


    def add_credit(self, credit : int):
        '''
        asks for an integer number credit to add to the total, only accepts proper denominations
        found in canada
        '''
        try:
            if credit==0.05 or credit==0.1 or credit==0.25 or credit==1 or credit==2 or credit==5 or credit==10 or credit==20: #checks if its a valid denominations
                self.__credit += credit

        except:
            return None




    def return_credit(self):
        '''
        returns all credits to user and makes credit 0
        '''
        returned_credits = self.__credit
        self.__credit = 0
        return f"{returned_credits:.2f}"

    def return_product_list(self):
        return self.__product_list

    def __str__ (self):
        '''
        returns the full report of this Vending Machine, it returns the values of total revenue,
        credit, list of products as well as their data points #Item, (Quantity) : Price
        '''
        for i in range(len(self.__product_list)):
            print(f"{i+1}. {self.__product_list[i][0]:<10} ({self.__product_list[i][2]}) : ${self.__product_list[i][1]:<10}") # prints the list of products

        return f"Credit : ${self.__credit:.2f} | Revenue : ${self.__revenue:.2f}"#returns credit and revenue

