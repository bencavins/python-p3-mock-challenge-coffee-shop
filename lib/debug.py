#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    latte = Coffee('latte')
    drip = Coffee('drip')
    joe = Customer('joe')
    anne = Customer('anne')

    Order(joe, latte, 3.50)
    Order(anne, latte, 6.00)
    Order(joe, drip, 1.50)

    print(latte.average_price())