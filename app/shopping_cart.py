# shopping_cart.py
#Code Climate
#SETUP

import datetime # Used https://stackabuse.com/how-to-format-dates-in-python/ for datetime
import os
from dotenv import load_dotenv # Used https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/dotenv.md for .env variables
load_dotenv()
date = datetime.date.today()
time = datetime.datetime.now()
Tax = float(os.getenv("Tax", default = ".0875"))

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

def human_friendly_timestamp(time):
    """
    Converts raw time data to standard 12-hour time, for printing and display purposes.
    """
    return time.strftime("%I:%M %p")

def find_product(UserID, products):
    """
    Matches the inputed product identifier and matches it to an existing product.
    """
    MatchedID = [p for p in products if str(p["id"]) == str(UserID)]
    MatchedID = MatchedID[0]
    return MatchedID

# PROCESS USER INPUTED IDS

if __name__ == "__main__":

    print("Please input a product identifier.  Enter 'DONE' when finished.")
    condition = True
    SelectedIDs = []
    while condition == True:
        try:
            UserID = input("Product ID:  ")
            if UserID.lower() == "done":
                condition = False
            else:
                MatchedID = find_product(UserID, products)
                SelectedIDs.append(MatchedID)
        except:
            Error = "Invalid Product ID - Enter Valid"
            print(Error, end = " ")

    # OUTPUT RECEIPT

    print("---------------------------------")
    print("FOSTER QUICKMART")
    print("WWW.FOSTER-QUICKMART.COM")
    print("---------------------------------")
    print("CHECKOUT AT: ", date, human_friendly_timestamp(time))
    print("---------------------------------")
    print("SELECTED PRODUCTS:")
    Prices = []
    for MatchedID in SelectedIDs:
        print(" ... " + MatchedID["name"], " (" + to_usd(MatchedID["price"]) + ")")
        Prices.append(MatchedID["price"])
    print("---------------------------------")
    Subtotal = sum(Prices)
    print("SUBTOTAL: ", to_usd(Subtotal))
    print("TAX: ", to_usd(Subtotal * Tax))
    print("TOTAL: ", to_usd(Subtotal * (1 + Tax)))
    print("---------------------------------")
    print("THANKS, SEE YOU AGAIN SOON!")
    print("---------------------------------")