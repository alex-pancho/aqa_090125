from storage import database as db


def display_products(products_queryset: list) -> list:
    final_list = []
    for element in products_queryset:
        product_data = f"Title: {element[0]},\nCategory: {element[3]},\nDescription: {element[1]},\nPrice: {element[2]}\n"
        final_list.append(product_data)
    final_list.append('----------------------------------------')

    return final_list


categories_list = ['Phones', 'Laptops', 'Accessories']
product_list = [
    ('iPhone 13', '8Gb/128Gb', 1200, 1),
    ('iPhone 12 Max', '12Gb/256Gb', 1199, 1),
    ('Samsung Galaxy S22', '8Gb/128Gb', 1050, 1),
    ('Acer Aspire 15', 'Core i7', 980, 2),
    ('ASUS Zen 12', 'Ryzen 5500', 950, 2),
    ('Logitec D14SB', 'Wireless keyboard', 59, None)
]

for category in categories_list:
    db.add_category(category_name=category)

for product in product_list:
    db.add_product(product_data=product)


print(*display_products(db.get_products_by_category_id(1)), sep='\n')
print(*display_products(db.get_products_by_category_id(2)), sep='\n')
print(*display_products(db.get_all_products()), sep='\n')
print(*db.get_all_categories(), sep='\n')


