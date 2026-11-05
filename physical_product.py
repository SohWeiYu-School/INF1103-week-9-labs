from product import Product


class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.get_weight()} kg")

    def get_fulfilment_info(self):
            return "Requires physical shipping"

if __name__ == "__main__":
    guitar = PhysicalProduct("P010", "Guitar", 300.0, 5, 40)
    guitar.display_information()
    
