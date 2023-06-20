class Coffee:
    def __init__(self, name):
        self.name = name
        self.orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    def get_customers(self):
        return [o.customer for o in self.orders]
    
    def num_orders(self):
        return len(self.orders)
    
    def average_price(self):
        return sum([o.price for o in self.orders]) / self.num_orders()