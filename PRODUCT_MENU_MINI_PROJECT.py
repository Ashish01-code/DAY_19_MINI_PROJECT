#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import os
class Product:
    def __init__(self,filename):
        self.filename=filename
        self.product={}
        self.load_product()
    def load_product(self):
        if not os.path.exists(self.filename):
            print("FILE NOT FOUND")
            return
        with open(self.filename,"r",newline="") as f:
            reader=csv.reader(f)
            for row in reader:
                if row:
                    product_id,product_name,price,quality=row
                    self.product[product_id]=[product_name,price,quality]
    def save_product(self):
        with open(self.filename,"w",newline="") as f:
            writer=csv.writer(f)
            for product_id,(product_name,price,quality) in self.product.items():
                writer.writerow([product_id,product_name,price,quality])
    def get_valid_product_id(self):
            return input("ENTER PRODUCT ID: ").strip()
    def get_valid_product_name(self):
            return input("ENTER PRODUCT NAME: ").strip()
    def get_valid_price(self):
        try:
            return int(input("ENTER PRICE: "))
        except ValueError:
            print("INVALID PRICE")
            return None
    def add_product(self):
        product_id=self.get_valid_product_id()
        if product_id in self.product:
            print("PRODUCT ID ALREADY EXISTS")
            return
        product_name=self.get_valid_product_name()
        price=self.get_valid_price()
        if price is None:
            return
        quality=input("ENTER QUALITY (GOOD/BAD)").strip()
        self.product[product_id]=[product_name,price,quality]
        self.save_product()
    def view_product(self):
        if not self.product:
            print("NO SUCH PRODUCT_ID EXISTS")
            return
        print("-----PRODUCT LIST----")
        for product_id,(product_name,price,quality) in self.product.items():
            print(f"PRODUCT ID : {product_id}| PRODUCT NAME: {product_name} | PRICE: {price} | QUALITY: {quality}")
    def search_product(self):
        product_id=self.get_valid_product_id()
        if product_id in self.product:
            product_name,price,quality=self.product[product_id]
            print(f"FOUND - {product_id} | {product_name} | {price} | {quality}")
        else:
            print("NO SUCH ID FOUND")
    def update_product(self):
        product_id=self.get_valid_product_id()
        if product_id  not in self.product:
            print("NO SUCH PRODUCT_ID EXISTS")
            return
        product_name=self.get_valid_product_name()
        price=self.get_valid_price()
        if price is None:
            return
        quality=input("ENTER QUALITY (GOOD/BAD)")
        self.product[product_id]=[product_name,price,quality]
        self.save_product()
    def delete_product(self):
        product_id=self.get_valid_product_id()
        if product_id not in self.product:
            print("NO SUCH ID FOUND")
            return
        del self.product[product_id]
        self.save_product()
    def count_product(self):
        print("THE COUNT OF PRODUCT IS : ",len(self.product))
    def open_product(self):
        os.startfile(self.filename)
    def sort_by_price(self):
        if not self.product:
            print("NO PRODUCTS TO SORT")
            return
        temp_list=[]
        for product_id ,(product_name,price,quality) in self.product.items():
            price=int(price)
            temp_list.append([price, product_id, product_name, quality])
        temp_list.sort()
        print("----PRODUCT SORTED BY PRICE----")
        for price, product_id, product_name, quality in temp_list:
            print(f"{product_id} | {product_name} | {price} | {quality}")
    def filter_by_price(self, min_price, max_price):
        if not self.product:
            print("NO PRODUCTS TO FILTER")
            return
        min_price=int(input("ENTER THE STARTING VALUE"))
        max_price=int(input("ENTER THE ENDING VALUE"))
        temp_list = []
        for product_id, (product_name, price, quality) in self.product.items():
            price = int(price)
            if min_price <= price <= max_price:  
                temp_list.append([price, product_id, product_name, quality])
        if not temp_list:
                print("NO PRODUCTS FOUND IN THIS PRICE RANGE")
                return
        print(f"----PRODUCTS FILTERED BY PRICE ({min_price}-{max_price})----")
        for price, product_id, product_name, quality in temp_list:
            print(f"{product_id} | {product_name} | {price} | {quality}")
    def sort_by_quality(self,quality_filter):
        if not self.product:
            print("NO PRODUCTS TO SORT")
            return
        temp_list = []
        for product_id, (product_name, price, quality) in self.product.items():
            temp_list.append([quality.upper(), product_id, product_name, price])
        temp_list.sort()
        print("----PRODUCT SORTED BY QUALITY----")
        for quality, product_id, product_name, price in temp_list:
            print(f"{product_id} | {product_name} | {price} | {quality}")
    def filter_by_quality(self, quality_filter):
        if not self.product:
            print("NO PRODUCTS TO FILTER")
            return
        temp_list = []
        for product_id, (product_name, price, quality) in self.product.items():
            if quality.upper() == quality_filter.upper():
                temp_list.append([product_id, product_name, price, quality])
        if not temp_list:
            print(f"NO PRODUCTS FOUND WITH QUALITY {quality_filter}")
            return
        print(f"----PRODUCTS FILTERED BY QUALITY ({quality_filter})----")
        for product_id, product_name, price, quality in temp_list:
            print(f"{product_id} | {product_name} | {price} | {quality}")
Pro=Product(r"E:\TEST\PRODUCT.csv")
while True:
    print("\n--- PRODUCT MANAGER ---")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Count Products")
    print("7. Open File")
    print("8. Sort Products by Price")
    print("9. Filter Products by Price")
    print("10. Filter Products by Quality")
    print("11. Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Enter a valid number")
        continue

    if choice == 1:
        Pro.add_product()
    elif choice == 2:
        Pro.view_product()
    elif choice == 3:
        Pro.search_product()
    elif choice == 4:
        Pro.update_product()
    elif choice == 5:
        Pro.delete_product()
    elif choice == 6:
        Pro.count_product()
    elif choice == 7:
        Pro.open_product()
    elif choice == 8:
        Pro.sort_by_price()
    elif choice == 9:
        Pro.filter_by_price()
    elif choice == 10:
        quality = input("ENTER QUALITY TO FILTER (GOOD/BAD): ").strip().upper()
        Pro.filter_by_quality(quality)
    elif choice == 11:
        print("Exiting...")
        break
    else:
        print("Invalid choice")



# In[ ]:




