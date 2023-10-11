class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        customer.orders.append(self)
        self.coffee = coffee
        coffee.orders.append(self)
        self.price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if new_price >= 1 and new_price <= 10:
            self._price = new_price
        else:
            raise ValueError('price must be between 1 and 10')
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, new_customer):
        from classes.customer import Customer
        if isinstance(new_customer, Customer):
            self._customer = new_customer
        else:
            raise ValueError('invalid customer obj')
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, new_coffee):
        from classes.coffee import Coffee
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee
        else:
            raise ValueError('invalid coffee obj')
    
    def __repr__(self) -> str:
        return f'<Order {self.customer.name} {self.coffee.name} {self.price}>'
