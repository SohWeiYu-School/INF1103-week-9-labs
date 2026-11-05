from product import Product


class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight


if __name__ == "__main__":
    guitar = PhysicalProduct("P010", "Guitar", 300.0, 5, 40)
    guitar.display_information()
