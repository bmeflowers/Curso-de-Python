import json

file_path = 'products.json'
new_product = {
    'name': 'Wireless Chatger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '08-09-2025'
}

with open (file_path, mode = 'r') as file:
    products = json.load(file)

products.append(new_product)

with open(file_path, mode='w') as file:
    json.dump(products, file, indent=4)