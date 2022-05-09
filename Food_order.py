import json
import random
import string


class Restaurent:
    fp = open("menu.json", "r+")
    content = fp.read()
    menu_content = json.loads(content)
    menu_data = menu_content["Menu"]

    for type_of_food in menu_data:
        print(type_of_food)
        print("-------------------")
        food_item_counter = 1
        for food_no in menu_data[type_of_food]:
            print(food_item_counter, food_no)
            food_item_counter += 1
        print("\n")

    def __init__(self, name):
        self.restro_name = name
        self.food = {}
        self.food_ID = len(self.food) + 1
        self.admin_details = {}
        self.user_details = {}
        self.ordered_item = []

    def admin_register(self):
        print(f"WELCOME TO {self.restro_name} RESTAURANT\n\n")
        print("Please Enter your details for Admin registration")
        self.name = input("Enter your name : ")
        self.phone_number = int(input("Enter your 10 digits phone number : "))
        self.admin_email = input("Enter your email id : ")
        self.address = input("Enter your address : ")
        self.admin_pass = input("Enter your password : ")
        self.admin_details = {"Name ": self.name, "Phone Number": self.phone_number, "Email ID": self.admin_email,
                              "Address": self.address, "Password": self.admin_pass}
        print("\n!! ACCOUNT CREATED SUCCESSFULLY !!\n")
        print("ADMIN DETAILS: ")
        for i in self.admin_details:
            print(i, ":", self.admin_details[i])

    def autogenerate_foodId():
        foodId = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        return foodId

    def admin_login(self):
        print(f"WELCOME TO {self.restro_name} RESTAURANT\n\n")
        print("Please Enter your details to Admin Log in")
        email = input("Enter Your Email ID : ")
        pas = input("Enter Your Password : ")
        if len(self.admin_details.values()) != 0:
            if email == self.admin_email and pas == self.admin_pass:
                print("\n!! LOGIN SUCCESSFUL !!")
                while True:
                    print("\nEnter the Below Options\n")
                    print(
                        "\t1. ADD FOOD ITEM \n\t2. EDIT FOOD ITEM\n\t3. VIEW FOOD ITEM\n\t4. DELETE FOOD ITEM\n\t5. GO BACK")
                    z = input()
                    if z == "1":
                        self.add_food_item()
                    elif z == "2":
                        self.edit_food_item()
                    elif z == "3":
                        self.view_food_item()
                    elif z == "4":
                        self.delete_food_item()
                    elif z == "5":
                        break
                    else:
                        print("NOT A VALID OPTION ")
            else:
                print("\n!! INCORRECT ADMIN DETAILS !!\n")
        else:
            print("\n!! ADMIN ACCOUNT NOT EXIST !!\n")

    def add_food_item(self):
        name = input("Enter the food name : ")
        quantity = int(input("Enter the quantity in values only : "))
        price = float(input("Enter the price in Rs only : "))
        discount = float(input("Enter the discount in Rs only : "))
        stock = float(input("Enter the available stock in values only : "))
        food_item = {"Name": name, "Quantity": quantity, "Price": price, "Discount": discount, "Stock": stock}
        self.food_ID = len(self.food) + 1
        self.food[self.food_ID] = food_item
        print("\n!! FOOD ITEM ADDED SUCCESSFULLY !!\n")
        print("UPDATED FOOD ITEMS :", self.food, "\n")

    def edit_food_item(self):
        x = int(input("Enter the Food ID you want to update : \n"))
        if x in self.food.keys():
            print(
                "\t1. UPDATE FOOD NAME\n\t2. UPDATE QUANTITY\n\t3. UPDATE PRICE\n\t4. UPDATE DISCOUNT\n\t5. UPDATE STOCK\n")
            y = input("Enter the Number Only : ")
            if y == "1":
                self.food[x]["Name"] = input("Updated Food name : ")
                print("\n!! Food Name Successfully Updated !!\n")
            elif y == "2":
                self.food[x]["Quantity"] = float(input("Updated Quantity in values only : "))
                print("\n!! Quantity Successfully Updated !!\n")
            elif y == "3":
                self.food[x]["Price"] = float(input("Updated Price in Rs only : "))
                print("\n!! Price Successfully Updated !!\n")
            elif y == "4":
                self.food[x]["Discount"] = float(input("Updated Discount in Rs only : "))
                print("\n!! Discount Successfully Updated !!\n")
            elif y == "5":
                self.food[x]["Stock"] = float(input("Updated Stock in values only : "))
                print("\n!! Stock Successfully Updated !!\n")
            else:
                print("!! NOT A VALID OPTION !!\n")
        else:
            print("\n!! INCORRECT FOOD ID !!\n")

    def view_food_item(self):
        print("LIST OF FOOD ITEMS : \n")
        if len(self.food) != 0:
            for i in self.food:
                print(f"Food Id : {i}")
                for j in self.food[i]:
                    print(j, ":", self.food[i][j])
                print()
        else:
            print("!! FOOD ITEMS ARE NOT AVAILABLE !!\n")

    def delete_food_item(self):

        print("!! WARNING !!\nFOOD ITEM WILL DELETE PERMANENTLY\n")
        print("Enter the Food ID ")
        x = int(input())
        if x in self.food.keys():
            del self.food[x]
            print("\n!! FOOD ITEM DELETED SUCCESSFULLY !!\n")
            print("UPDATED FOOD ITEM LIST :\n", self.food)
        else:
            print("!! INCORRECT FOOD ID!!\n")

    def user_register(self):
        user_name = input("Enter your full name : ")
        phone_no = int(input("Enter your 10 digit phone number : "))
        email = input("Enter your email id : ")
        password = input("Enter your password : ")
        address = input("Enter your address with area PIN code ")
        self.user_details = {"User Name": user_name, "Phone No.": phone_no, "Email_ID": email, "Password": password,
                             "Address": address}
        print("\n!! ACCOUNT CREATED SUCCESSFULLY !!\n")
        print("USER DETAILS : ")
        for i in self.user_details:
            print(i, ":", self.user_details[i])

    def user_login(self):

        print(f"WELCOME TO {self.restro_name} RESTAURANT\n\n")
        email = input("Enter Your Email ID : ")
        pas = input("Enter Your Password : ")
        if len(self.user_details.values()) != 0:
            if email == self.user_details["Email_ID"] and pas == self.user_details["Password"]:
                print("\n!! LOGIN SUCCESSFULLY !!")
                while True:
                    print("\nEnter the Below Options\n")
                    print("\t1. PLACE NEW ORDER\n\t2. ORDER HISTORY\n\t3. UPDATE PROFILE\n\t4. GO BACK")
                    z = input()
                    if z == "1":
                        self.place_order()
                    elif z == "2":
                        self.ordered_history()
                    elif z == "3":
                        self.update_details()
                    elif z == "4":
                        break
                    else:
                        print("NOT A VALID OPTION")
            else:
                print("\n!! INCORRECT USER DETAILS!!\n")
        else:
            print("\n! USER ACCOUNT NOT EXIST\n")

    def place_order(self):

        if len(self.food) != 0:
            print("LIST OF AVAILABLE FOOD ITEMS :\n")
            menu = []
            for items in self.food:
                menu.append([self.food[items]["Name"], self.food[items]["Quantity"], self.food[items]["Price"]])
            for i in range(len(menu)):
                print(i + 1, ".", menu[i])
            while True:
                print("\n\t1. CONTINUE ORDER\n\t2. GO BACK\n")
                x = input()
                if x == "1":
                    print("Enter the Food number You want to ordered separated by comma")
                    y = input().split(",")
                    for i in y:
                        z = int(i)
                        if z <= len(menu):
                            self.ordered_item.append(menu[z - 1])
                        else:
                            print("\nFOOD ITEM NOT AVAILABLE  : ", z)
                    print("\nLIST OF FOOD ITEMS SELECTED : \n")
                    for j in self.ordered_item:
                        print(j)
                elif x == "2":
                    break
                else:
                    print("!! NOT A VALID OPTION !!\n")
        else:
            print("\n!! FOOD ITEMS ARE NOT AVAILABLE !!\n")

    def ordered_history(self):
        if len(self.ordered_item) != 0:
            print("\nLIST OF PREVIOUS ORDERED FOOD ITEMS : \n")
            for i in self.ordered_item:
                print(i)
        else:
            print("\n!! ORDER HISTORY NOT AVAILABLE !!")

    def update_details(self):

        for i in self.user_details:
            print(i, ":", self.user_details[i])
        while True:
            print("Select Below Options to Update Your Profile Details\n")
            print(
                "\t1. UPDATE NAME\n\t2. UPDATE PHONE NO\n\t3. UPDATE EMAIL ID\n\t4. UPDATE PASSWORD\n\t5. UPDATE ADDRESS\n\t6. GO BACK\n")
            x = input()
            if x == "1":
                self.user_details["User Name"] = input("Enter your updated full name : ")
                print("\n!! Name Successfully Updated !!\n")
            elif x == "2":
                self.user_details["Phone No."] = int(input("Enter your updated 10 digit phone number : "))
                print("\n!! Phone No Successfully Updated !!\n")
            elif x == "3":
                self.user_details["Email_ID"] = input("Enter your updated email id : ")
                print("\n!! Email ID Successfully Updated!!")

            elif x == "4":
                self.user_details["Password"] = input("Enter your updated password : ")
                print("\n!! Password Successfully Updated !!\n")

            elif x == "5":
                self.user_details["Address"] = input("Enter your updated address with area PIN code ")
                print("\n!! Address Updated Successfully Updated!!\n")

            elif x == "6":
                break
            else:
                print("\n!! NOT A VALID OPTION !!\n")

            if x in ["1", "2", "3", '4', "5"]:
                for i in self.user_details:
                    print(i, ":", self.user_details[i])
            else:
                pass

def main():
    obj = Restaurent("Hritu's Kitchen")
    print("" * 30, "WELCOME TO", obj.restro_name, "RESTAURANT", "" * 30, "\n")
    print("-" * 89)
    while True:
        print("-" * 40 + "HOME PAGE" + "-" * 40 + "\n")
        print("\t1. ADMIN \n\t2. USER\n\t3. EXIT\n")
        x = input()
        if x == "1":
            while True:
                print("\n" + "-" * 40 + "ADMIN PAGE" + "-" * 40 + "\n")
                print("\t1. ADMIN REGISTRATION\n\t2. ADMIN LOGIN\n\t3. GO BACK\n")
                y = input()
                if y == "1":
                    obj.admin_register()
                elif y == "2":
                    obj.admin_login()
                elif y == "3":
                    break
                else:
                    print("\nNOT A VALID OPTION\n")

        elif x == "2":
            while True:
                print("\n" + "-" * 40 + "USER PAGE" + "-" * 40 + "\n")
                print("\t1. CREATE ACCOUNT\n\t2. LOGIN\n\t3. GO BACK\n")
                y = input()
                if y == "1":
                    obj.user_register()
                elif y == "2":
                    obj.user_login()
                elif y == "3":
                    break
                else:
                    print("\nNOT A VALID OPTION ")
        elif x == "3":
            break
        else:
            print("NOT A VALID OPTION")

if __name__ == '__main__':
    main()
