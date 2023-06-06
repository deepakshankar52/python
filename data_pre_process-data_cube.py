# python program to create data cube for product, date, country

class Product:
    def __init__(self,name,category,price):
        self.name = name
        self.category = category
        self.price = price
        
products = [
    Product("Laptop","Electronics",1000),
    Product("T-shirt","Clothing",20),
    Product("Book","Books",15),
    Product("Headphones","Electronics",100),
    Product("Jeans","Clothing",50),
    Product("Smartphone","Electronics",800),
    Product("Sunglasses","Accessories",30),
    Product("Watch","Accessories",50),
    Product("Shoes","Footwear",80),
]

dates = ["2023-05-01","2023-05-02","2023-05-03"]

countries = ["USA","UK","Germany"]

data_cube = {}

for product in products:
    for date in dates:
        for country in countries:
            if product.category not in data_cube:
                data_cube[product.category] = {}
            
            if product.name not in data_cube[product.category]:
                data_cube[product.category][product.name] = {}
                
            if date not in data_cube[product.category][product.name]:
                data_cube[product.category][product.name][date]= {}
                
            data_cube[product.category][product.name][date][country] = product.price
            
for category, products in data_cube.items():
    print("Category:",category)
    for product, dates in products.items():
        print("-Product:",product)
        for date, countries in dates.items():
            print(" Date:",date)
            for country, price in countries.items():
                print(" Country;",country)
                print(" Price:",price)
        
