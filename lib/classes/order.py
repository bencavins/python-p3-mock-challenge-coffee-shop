class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        self.customer.orders.append(self)
        self.coffee.orders.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if new_price >= 1 and new_price <= 10:
            self._price = new_price
        else:
            raise ValueError('price must be between 1 and 10')
    
    def __repr__(self) -> str:
        return f"<Order {self.price} {self.coffee.name}>"
