class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise Exception(f'invalid name: "{new_name}"')
    
    def get_coffees(self):
        return [o.coffee for o in self.orders]