class Coffee:
    def __init__(self, name):
        self.name = name
        self.orders = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise ValueError('name must be a string!')
    
    def get_customers(self):
        result = []
        for order in self.orders:
            result.append(order.customer)
        return result
    
    def num_orders(self):
        return len(self.orders)
    
    def average_price(self):
        # total = 0
        # for order in self.orders:
        #     total += order.price
        # return total / self.num_orders()
        return sum([order.price for order in self.orders]) / self.num_orders()

    def __repr__(self) -> str:
        return f"<Coffee {self.name}>"