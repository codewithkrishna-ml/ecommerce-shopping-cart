#PROJECT-E-Commerce Shopping Cart System
class Product:
    def __init__(self , name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class ShoppingCart:
    def __init__(self):
        self.cart_items = {}

    def add_to_cart(self, product_obj, quantity): 
        if product_obj.stock >= quantity:
            product_obj.stock -= quantity
            if product_obj.name in self.cart_items:
                self.cart_items[product_obj.name] +=quantity
            else:
                self.cart_items[product_obj.name] = quantity
            print(f"{quantity} x '{product_obj.name}' added to cart successfully!")
        else:
             print(f"Sorry! '{product_obj.name}' is out of stock or insufficient stock available")

    def view_cart(self):
        if len(self.cart_items) == 0:
            print("Your cart is currently empty!")
        else:
            print("\n------your shopping cart-------")
            for item_name, qty in self.cart_items.items():
                print(f"{item_name} - Quantity:{qty}")

    def calculate_bill(self,product_list):
        total_price = 0
        print("\n--------Bill summary-------")
        for item_name, qty in self.cart_items.items():
            for product in product_list:
                if product.name == item_name:
                    item_cost = qty * product.price
                    total_price += item_cost
                    print(f"{item_name}: {qty} x {product.price} = {item_cost}")
                    print("---------------------------------")
                    print(f"Total Amount Payable: {total_price}")

if __name__ == "__main__":
    laptop = Product("Laptop" , 50000,5)
    phone = Product("Mobile" , 15000,10)
    store_products = [laptop,phone]

    my_cart = ShoppingCart()
    my_cart.add_to_cart(laptop,2)
    my_cart.add_to_cart(laptop,1)
    my_cart.add_to_cart(phone,20)
    my_cart.view_cart()
    my_cart.calculate_bill(store_products )
