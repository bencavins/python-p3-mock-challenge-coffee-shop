class Coffee:
    all = [] # <- not required

    def __init__(self, coffee_name):
        self.name = coffee_name
        self.orders = []
        Coffee.all.append(self) # not required
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    def get_customers(self):
        return [order.customer for order in self.orders]
    
    def num_orders(self):
        return len(self.orders)
    
    def average_price(self):
        total = sum([order.price for order in self.orders])
        return total / self.num_orders()

    # @classmethod
def all_avg():
    total = 0
    for c in Coffee.all:
        for o in c.orders:
            total += o.price
    return total / len(Coffee.all)