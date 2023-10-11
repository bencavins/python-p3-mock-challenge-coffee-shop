class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        # if isinstance(new_name, str) and len(new_name) >= 1 and len(new_name) <= 15:
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise ValueError('name must be between 1 and 15 chars')
    
    def get_coffees(self):
        coffees = []
        for order in self.orders:
            coffees.append(order.coffee)
        return coffees

    def __repr__(self):
        return f'<Customer {self.name}>'