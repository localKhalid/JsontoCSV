import json
import csv
with open('products.json.txt', 'r') as file:
    products_json_file = json.load(file)

for product in products_json_file:
    product_name = product['name']
    product_price = product['price']
    print("Product name:", product_name)
    print("Product price:", product_price)

with open('products.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for product in products_json_file:
        writer.writerow({'name': product['name'], 'price': product['price']})

print("Product data has been written to products.csv")
