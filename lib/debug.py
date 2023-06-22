#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    mocha = Coffee('mocha')
    latte = Coffee('latte')

    joe = Customer('joe')

    order1 = Order(joe, latte, 5)
    order2 = Order(joe, latte, 4)
    order3 = Order(joe, mocha, 10)

    ipdb.set_trace()
