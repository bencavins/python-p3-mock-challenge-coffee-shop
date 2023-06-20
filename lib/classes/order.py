from classes.customer import Customer
from classes.coffee import Coffee

class Order:

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        self.coffee.orders.append(self)
        self.customer.orders.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if 1 <= new_price <= 10:
            self._price = new_price
        else:
            raise Exception(f'invalid price: "{new_price}"')
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, new_customer):
        if isinstance(new_customer, Customer):
            self._customer = new_customer
        else:
            raise Exception(f'invalid customer: {new_customer}')

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, new_coffee):
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee
        else:
            raise Exception(f'invalid coffee: {new_coffee}')