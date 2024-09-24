from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = str(name) # название/ строка
        self.weight = float(weight) # вес товара/ дробное число
        self.category = str(category) # категория/ строка
    def __str__(self):
        product_ = f'{self.name}, {self.weight}, {self.category}'
        return product_
class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        str_ = file.read()
        # pprint(file.read())
        file.close()
        return str_
    def add(self, *products):
        current_products = self.get_products()
        file = open(self.__file_name, 'a')
        for product in products:
            if str(product) in current_products:
                file.write(f'{product}\n')

            else:
                print(f'Продукт {str(product)} уже есть в магазине')
        file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1, p2, p3)

print(s1.get_products())