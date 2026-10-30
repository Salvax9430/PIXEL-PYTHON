# Python data structures
# This file uses simple shop examples.

print("DATA STRUCTURES IN PYTHON")
print("=========================")

# -------------------------------------------------------------------
# 1. LIST
# A list stores many values in order. Lists can be changed.
# uses a square braces[]
# -------------------------------------------------------------------
products = ["bread", "milk", "eggs", "cheese"]
print("LIST")
print(f"Original products: {products}")
print(f"first element in the list is: {products[0]}")#printing inedex 0(first element)
print(f"first element in the list is: {products[2]}")#printing index 2 element
print(f"first element in the list is: {products[-1]}")#printing the last element
# printing any range of items/elements
print(f"The first 3elements are: {products[0:3]}")
print(f"Printing the first 4 elements iclude: {products[0:4]}")
# adding values/elements at different indexes/positions
products[0]="juice"#adding values at any position by specifying the position
print(f"After adding juice at position 1 the list is now: {products}")

print(f"{products}")
products.append('soda')#adds the element sda at the end of the list
print(f"after adding an elemnt at the end: {products}")
# inserting/adding an element at position 1
products.insert(3,"coffee")
products[0]="Mango"
products.insert(4,"bramuel")
print(f"after adding elemnets at diff positions: {products}")
# extending the list/ adding list on onother list
products.extend(["oranges","tomatoes","Pepper"])
print(f"the new extended list is: {products}")

products.remove("coffee")#removing by name

print(f"after remooving coffee values: {products}")
removed_product=products.pop() #removes the last item
print(f"The removed product is: {removed_product}")
print(f"Here is the list aftre removing the last product: {products}")
# specifying the poping index
removed_product=products.pop(1)
print(f"the removed product at index 1(position 2) is: {removed_product}")
print(f"list is now: {products}")

print("no.of products is: ",len(products))
print("Is milk in the list??", "milk" in products)
print("Is cheese in the list??","cheese" in products)
print("How many juices are in the list: ",products.count("juice"))
# sorting products
products.sort()
print(f"Producta in alpahabetical order iS: {products}")
# reversing the products/list
products.reverse()
print(f"Products in reverse order is: {products}")
# a copy paste of the products
new_products=products.copy()
print(f"A copy paste of the products is: {new_products}")
# clearing the list(deleting everything)
products.clear()
print(f"afer clearing the list, the list is now: {products}")
# 2. TUPLE
# A tuple is like a list, but it cannot be changed after creation.
# it uses the normal braces()
# -------------------------------------------------------------------
print("\nTUPLE")
customers = (
    "John",
    "Mary",
    "Sifuna",
    "Sifuna",
    "Sifuna",
    "Sifuna",
    "Peter",
    "Jane",
    "Bramuel",
    "Sifuna",
    "Simiyu",
    "Samson",
    "Caroline",
    "Freddy",
)
# print range and specified customers
print(f"customers are: {customers}")
print(f"here is the first customer: {customers[0]}")
print(f"here is the 6th customer: {customers[5]}")
print(f"here is the firs to 7th customer: {customers[0:6]}")
print(f"here is the last customer: {customers[-1]}")
# other imporatant operations
print("the no of customers is: ",len(customers))
print("is sifuna in the record: ","Sifuna" in customers)
print("the number of sifuna appers: ",customers.count("Sifuna"))
print("The index os samson is: ",customers.index("Samson"))
## customers[0] = "John" would give an error because tuples are fixed.
# customers[0] = "John"
# print(f"{customers}")
print("Tuples cannot be changed after they are created.")
# joining a tuple to onother tuple
more_customers=customers + ("Brian",'Lukas',"Doreen")
print(f" After adding more customers/joining: {more_customers}")
# 3. SET
# A set stores unique values. Repeated values are removed.
# uses curly braces{}
# -------------------------------------------------------------------
print("\nSET")
customer_names={ "John",
    "Mary",
    "Sifuna",
    "Sifuna",
    "Sifuna",
    "Sifuna",
    "Peter",
    "Jane",
    "Bramuel",
    "Sifuna",
    "Simiyu",
    "Samson",
    "Caroline",
    "Freddy"}
print(f"The set of customers are: {customer_names}")
print("is Sifuna in the set: ","Sifuna" in customer_names)
print("here is the number of customers",len(customer_names))
customer_names.add("Grace")
print(f'After adding grace: {customer_names}')
customer_names.update("Mary","John")
print(f'After adding several names: {customer_names}')
# removing items fro a set
customer_names.remove("Mary")
print(f"after removing mary: {customer_names}")
# discard does not give an error when the item is not present
customer_names.discard("Unknown")
print("After discard of an unknown name:", customer_names)
morning_customers = {"Bramuel", "Caroline", "Brian"}
evening_customers = {"Caroline", "Brian", "Freddy"}
print("Customers in both groups:", morning_customers.intersection(evening_customers))
print("Customers in either group:", morning_customers.union(evening_customers))
print("Morning customers only:", morning_customers.difference(evening_customers))
print("Evening customers only: ",evening_customers.difference(morning_customers))

# -------------------------------------------------------------------
# 4. DICTIONARY
# A dictionary stores data using keys and values.
# -------------------------------------------------------------------
print("\nDICTIONARY")
customer={
    "name":"Bramuel",
    "Age":20,
    "city": "Nairobi",
    "Profession":"compiuter scientist",
}
print(f" the customers are: {customer}")
##reading values
print(f"the name if the customer is: {customer["name"]}")
print(f"the age of the customer is: {customer["Age"]}")
print(f"the city is: {customer["city"]} ")
# adding new values
customer["phone"]="+2547000000000"
customer["Age"]=21
print(f'after adding the phone am dchanging the age: {customer}')
# updating more than one value
customer.update({"name":"Bramuel Sifuna","city":"Nakuru","Memebership":True})
print(f"after updating more than one value: {customer}")
# Dictionary operations
print("the number of items in the dictionary is: ",len(customer))
print(f"the keys in the dictionary are: {customer.keys()}")
print(f"the values in the dictionary are: {customer.values()}")
print("All key-value pairs:", customer.items())
print("Is name a key?", "name" in customer)
print("Number of customer details:", len(customer))

removed_value = customer.pop("phone")
print("Removed phone:", removed_value)
print("Dictionary after pop:", customer)
# -------------------------------------------------------------------
# 5. SHOPPING DATA USING A LIST AND A DICTIONARY
# -------------------------------------------------------------------
print("\nSHOPPING EXAMPLE")
shopping_items=["bread","milk","eggs","cheese"]
shopping_prices=[130,345,334,3434]
print(f"Shopping items are: {shopping_items}")
print(f"Shopping prices include: {shopping_prices}")
total=sum(shopping_prices)
print(f"total shipping cost is: {total}")
shop={
    "braed"
}