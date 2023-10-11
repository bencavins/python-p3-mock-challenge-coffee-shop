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
        customers = []
        for order in self.orders:
            customers.append(order.customer)
        return customers
    
    def num_orders(self):
        # count = 0
        # for order in self.orders:
        #     count += 1
        # return count
        return len(self.orders)
    
    def average_price(self):
        # count = 0
        # total = 0
        # for order in self.orders:
        #     count += 1
        #     total += order.price
        # return total / count
        return sum([o.price for o in self.orders]) / self.num_orders()

    def __repr__(self):
        return f'<Coffee {self.name}>'