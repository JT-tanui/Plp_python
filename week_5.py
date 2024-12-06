# Base Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, name, price):
        self.brand = brand
        self.model = model
        self.name = name
        self.price = price

    def display_details(self):
        return f"{self.name} ({self.brand} {self.model}) - ${self.price}"

    def make_call(self, number):
        return f"Dialing {number} from {self.name}..."


# Subclass: Smartwatch inheriting from Smartphone
class Smartwatch(Smartphone):
    def __init__(self, brand, model, name, price, strap_material):
        super().__init__(brand, model, name, price)
        self.strap_material = strap_material

    def display_details(self):
        return f"{self.name} (Smartwatch, {self.brand} {self.model}) with {self.strap_material} strap - ${self.price}"

    def track_steps(self, steps):
        return f"{self.name} tracked {steps} steps today."


# Subclass: Tablet inheriting from Smartphone
class Tablet(Smartphone):
    def __init__(self, brand, model, name, price, screen_size):
        super().__init__(brand, model, name, price)
        self.screen_size = screen_size

    def display_details(self):
        return f"{self.name} (Tablet, {self.brand} {self.model}) with a {self.screen_size}\" screen - ${self.price}"

    def watch_movie(self, title):
        return f"Watching '{title}' on {self.name}..."


# Example Usage
phone = Smartphone("Samsung", "Galaxy S22", "S22 Ultra", 1199)
smartwatch = Smartwatch("Apple", "Series 8", "Apple Watch", 399, "Leather")
tablet = Tablet("Microsoft", "Surface Pro 9", "Surface Pro", 999, 13)

print(phone.display_details())
print(phone.make_call("246-34-7890"))
print(smartwatch.display_details())
print(smartwatch.track_steps(5000))
print(tablet.display_details())
print(tablet.watch_movie("Inception"))
