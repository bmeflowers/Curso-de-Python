import csv

new_product = {
    'name': 'Wireless Chatger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '08-09-2025'
}

with open ('products.csv', mode = 'a', newline='') as file:
    file.write('\n')
    csv_writer = csv. DictWriter(file, fieldnames = new_product.keys())
    csv_writer.writerow(new_product)
