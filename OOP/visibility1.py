class Product(object):
    pass

class Inventory(object):
    def __init__(self):
        self.__items = []
    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print("new item added")
        else:
            raise ValueError("Invaild Item")
    def get_number_of_items(self):
        return len(self.__items)
         
my_inventory = Inventory()
my_inventory.add_new_item(Product())

#my_inventory.__items <- 에러
# @property 데코레이터를 사용하면 해당 변수를 외부에서 사용할 수 있다

class Inventory(object):
    def __init__(self):
        self.__items = []

    @property
    def items(self):
        return self.__items