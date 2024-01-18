class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) >= 1 and len(new_name) <= 15:
            self._name = new_name
        else:
            raise ValueError('name must be between 1 and 15 chars')
    
    def get_coffees(self):
        result = []
        for order in self.orders:
            result.append(order.coffee)
        return result

    def __repr__(self) -> str:
        return f"<Customer {self.name}>"