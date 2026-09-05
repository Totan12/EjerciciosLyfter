class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            print(f"Producto: {product.name} | Precio: {product.price} | Cantidad: {product.quantity}")

    def total_value(self) -> float:
        total = 0 

        for product in self.products:
            total += (product.price * product.quantity)
        return total


# Ejemplo de uso:
product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)

inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)

print(inventory.total_value())