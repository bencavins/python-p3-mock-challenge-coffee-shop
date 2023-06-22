
class Order:

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        customer.orders.append(self)
        coffee.orders.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if 1 <= new_price <= 10:
            self._price = new_price
        else:
            raise Exception('invalid price')
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, new_coffee):
        from classes.coffee import Coffee
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee
        else:
            raise Exception('invalid coffee')
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, new_customer):
        from classes.customer import Customer
        if isinstance(new_customer, Customer):
            self._customer = new_customer
        else:
            raise Exception('invalid customer')
