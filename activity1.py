# Parent Class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self._storage = storage  # Encapsulated attribute (protected)

    def make_call(self, number):
        return f"{self.brand} {self.model} is calling {number}..."

    def take_photo(self):
        return f"{self.brand} {self.model} takes a photo."

    def get_storage(self):
        return f"Storage: {self._storage}GB"

    def device_info(self):
        return f"{self.brand} {self.model} - {self._storage}GB"


# Child Class (Inheritance + Polymorphism)
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, storage, camera_mp):
        super().__init__(brand, model, storage)  # Inherit parent attributes
        self.camera_mp = camera_mp

    # Polymorphism: overriding method
    def take_photo(self):
        return f"{self.brand} {self.model} takes a HIGH-RES {self.camera_mp}MP photo!"

    # New method
    def record_4k_video(self):
        return f"{self.brand} {self.model} is recording 4K video."


# Demonstration
phone1 = Smartphone("Samsung", "A32", 128)
phone2 = SmartphonePro("iPhone", "14 Pro", 256, 48)

print(phone1.device_info())
print(phone1.make_call("0722000000"))
print(phone1.take_photo())

print("\n--- PRO MODEL FEATURES ---")
print(phone2.device_info())
print(phone2.take_photo())        # Overridden method
print(phone2.record_4k_video())
