import logging

logging.basicConfig(filename='ramen.log', format='%(asctime)s-%(levelname)s-%(message)s', datefmt='%Y:%m:%d:%H:%M:%S',level=logging.DEBUG)

class Product:
    def __init__(self, in_type, in_name, in_price):
        self.type = in_type
        self.name = in_name
        self.price = in_price

    def save_to_file(self, file_name):
        f = open(file_name, 'a')
        f.write(str(self.type) + '; ')
        f.write(str(self.name) + '; ')
        f.write(str(self.price) + '\n')
        f.close()

    logging.debug('записан товар в файл')

    def load_from_file(self, file_name):
        f = open(file_name, 'r')
        text = f.readlines()
        el = text[0].split(';')
        self.type = el[0].strip()
        self.name = el[1].strip()
        self.price = float(el[2].strip())
    logging.info('Файл прочитан')    

    def __str__(self):
        return "Продукт " + self.name + " по " + str(self.price) + " тугриков"



class ProductPlus(Product):
    def __init__(self, product, amount):
        Product.__init__(self, product.type, product.name, product.price)
        self.amount = amount
        self.discount = 30 # в процентах

    def __str__(self):
        return "Продукт+ " + self.name + " по " + str(self.price) + " тугриков" +  str(self.amount) + " штук"

    logging.info(f'Установлена цена со скидкой ')     

class ProductStore:
    def __init__(self):
        self.store = []
        self.income = 0


    def add(self, product, amount):
        n = ProductPlus(product, amount)
        for i in self.store:
            if i.name == n.name:
                i.amount = i.amount + n.amount
                break

        else:

            self.store.append(n)
        logging.info(f'Добавлено новое количество продуктов {product} {amount}')

    def show_discount(self, identifier, identifier_type='name'):
        if identifier_type == 'name':
           for i in self.store:
                if i.name == identifier:
                    print(i.name, i.discount)

        elif identifier_type == 'type':
            for i in self.store:
                if i.type == identifier:
                    print(i.name, i.discount)



    def set_discount(self, identifier, percent, identifier_type='name'):

        if identifier_type == 'name':
            for i in self.store:
                if i.name == identifier:
                    i.discount = percent

        elif identifier_type == 'type':
            for i in self.store:
                if i.type == identifier:
                    i.discount = percent

        logging.info(f'предоставлена скидка {percent}')

    def sell_product(self, product_name, amount):

        for i in self.store:
            if i.name == product_name:
                if i.amount >= amount:
                    i.amount = i.amount - amount
                    self.income = amount * (i.price  - (i.price * i.discount / 100.0))

                    #           =   10    * (1.5 * 10 / 100 )

                else:
                    raise ValueError('Недостаточно товара!')

                logging.error(f'Недостаточно товара!{product_name},{amount}')              

        logging.info(f'произведена продажа товара {product_name},{amount}')                

    def get_income(self):
        return self.income

    def get_all_products(self):
        for i in self.store:
            print(i.name, i.price, i.type, i.amount)



    def get_product_info(self, product_name):
        for i in self.store:
            if i.name == product_name:
                return i.name, i.amount

    logging.info('Запрошена информация о товаре')



p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 100)
assert s.get_product_info('Ramen') == ('Ramen', 290)

s.show_discount('Ramen', identifier_type='name')
s.set_discount('Ramen', 40, identifier_type='name')
s.show_discount('Ramen', identifier_type='name')

#print(s)
#print(p)

pp = ProductPlus(p2, 1000)
print(pp)
p.save_to_file('p')
p.load_from_file('p')
print(p)
