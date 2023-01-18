class Storage:
    storage = []

    def __init__(self, capacity: int):
        self.capacity = capacity

    def add_product(self, product: str):
        if self.capacity > len(Storage.storage):
            Storage.storage.append(product)

    @staticmethod
    def get_products():
        return Storage.storage


storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())
