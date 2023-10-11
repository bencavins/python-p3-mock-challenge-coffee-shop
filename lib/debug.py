#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    joe = Customer('joe')
    anne = Customer('anne')
    latte = Coffee('latte')

    o1 = Order(joe, latte, 5)
    o2 = Order(anne, latte, 5)

    ipdb.set_trace()
