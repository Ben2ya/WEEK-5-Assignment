# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Child Class with Encapsulation
class Smartphone(Device):
    def __init__(self, brand, model, storage):
        super().__init__(brand, model)  # inheritance
        self.__storage = storage        # encapsulated (private attribute)

    def install_app(self, app_size):
        if app_size <= self.__storage:
            self.__storage -= app_size
            print(f"App installed! Remaining storage: {self.__storage} GB")
        else:
            print("Not enough storage!")

    def get_storage(self):
        return self.__storage

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S25", 128)
phone2 = Smartphone("Apple", "iPhone 16", 256)

print(phone1.device_info())   # Samsung Galaxy S25
phone1.install_app(10)        # App installed! Remaining storage: 118 GB
print("Storage left:", phone1.get_storage())
