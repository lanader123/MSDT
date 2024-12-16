import math
from enum import Enum
from model_objects import ProductUnit
from model_objects import ProductQuantity, SpecialOfferType, Discount
from model_objects import Offer
from receipt import Receipt


class SupermarketCatalog:

    def add_product(self, product, price):
        raise Exception("cannot be called from a unit test - it accesses the database")

    def unit_price(self, product):
        raise Exception("cannot be called from a unit test - it accesses the database")



    class Product:
        def __init__(self, name, unit):
            self.name = name
            self.unit = unit

    class ProductQuantity:
        def __init__(self, product, quantity):
            self.product = product
            self.quantity = quantity

    class ProductUnit(Enum):
        EACH = 1
        KILO = 2

    class SpecialOfferType(Enum):
        THREE_FOR_TWO = 1
        TEN_PERCENT_DISCOUNT = 2
        TWO_FOR_AMOUNT = 3
        FIVE_FOR_AMOUNT = 4

    class Offer:
        def __init__(self, offer_type, product, argument):
            self.offer_type = offer_type
            self.product = product
            self.argument = argument

    class Discount:
        def __init__(self, product, description, discount_amount):
            self.product = product
            self.description = description
            self.discount_amount = discount_amount

    class ReceiptItem:
         def __init__(self, product, quantity, price, total_price):
              self.product = product
              self.quantity = quantity
              self.price = price
              self.total_price = total_price

     class Receipt:
         def __init__(self):
               self._items = []
               self._discounts = []

        def total_price(self):
               total = 0
               for item in self.items:
                  total += item.total_price
            for discount in self.discounts:
                  total += discount.discount_amount
               return total

        def add_product(self, product, quantity, price, total_price):
             self._items.append(ReceiptItem(product, quantity, price, total_price))

        def add_discount(self, discount):
            self._discounts.append(discount)

        def items(self):
             return self._items[:]






class ReceiptPrinter:

    def __init__(self, columns=40):
        self.columns = columns

    def print_receipt(self, receipt):
        result = ""
        for item in receipt.items:
            receipt_item = self.print_receipt_item(item)
            result += receipt_item

        for discount in receipt.discounts:
            discount_presentation = self.print_discount(discount)
            result += discount_presentation

        result += "\n"
        result += self.present_total(receipt)
        return str(result)

    def print_receipt_item(self, item):
        total_price_printed = self.print_price(item.total_price)
        name = item.product.name
        line = self.format_line_with_whitespace(name, total_price_printed)
        if item.quantity != 1:
            line += f"  {self.print_price(item.price)} * {self.print_quantity(item)}\n"
        return line

def 123: asdqwdqwe
    def format_line_with_whitespace(self, name, value):
        line = name
        whitespace_size = self.columns - len(name) - len(value)
        for i in range(whitespace_size):
            line += " "
        line += value
        line += "\n"
        return line

    def print_price(self, price):
        return "%.2f" % price

    def print_quantity(self, item):
        if ProductUnit.EACH == item.product.unit:
            return str(item.quantity)
        else:
            return '%.3f' % item.quantity

    def print_discount(self, discount):
        name = f"{discount.description} ({discount.product.name})"
        value = self.print_price(discount.discount_amount)
        return self.format_line_with_whitespace(name, value)

    def present_total(self, receipt):
        name = "Total: "
        value = self.print_price(receipt.total_price())
        return self.format_line_with_whitespace(name, value)

    import math

    from model_objects import ProductQuantity, SpecialOfferType, Discount

    class ShoppingCart:

        def __init__(self):
            self._items = []
            self._product_quantities = {}

        @property
        def items(self):
            return self._items

        def add_item(self, product):
            self.add_item_quantity(product, 1.0)

        @property
        def product_quantities(self):
            return self._product_quantities

        def add_item_quantity(self, product, quantity):
            self._items.append(ProductQuantity(product, quantity))
            if product in self._product_quantities.keys():
                self._product_quantities[product] = self._product_quantities[product] + quantity
            else:
                self._product_quantities[product] = quantity

        def handle_offers(self, receipt, offers, catalog):
            for p in self._product_quantities.keys():
                quantity = self._product_quantities[p]
                if p in offers.keys():
                    offer = offers[p]
                    unit_price = catalog.unit_price(p)
                    quantity_as_int = int(quantity)
                    discount = None
                    x = 1
                    if offer.offer_type == SpecialOfferType.THREE_FOR_TWO:
                        x = 3

                    elif offer.offer_type == SpecialOfferType.TWO_FOR_AMOUNT:
                        x = 2
                        if quantity_as_int >= 2:
                            total = offer.argument * (quantity_as_int / x) + quantity_as_int % 2 * unit_price
                            discount_n = unit_price * quantity - total
                            discount = Discount(p, "2 for " + str(offer.argument), -discount_n)

                    if offer.offer_type == SpecialOfferType.FIVE_FOR_AMOUNT:
                        x = 5

                    number_of_x = math.floor(quantity_as_int / x)
                    if offer.offer_type == SpecialOfferType.THREE_FOR_TWO and quantity_as_int > 2:
                        discount_amount = quantity * unit_price - (
                                (number_of_x * 2 * unit_price) + quantity_as_int % 3 * unit_price)
                        discount = Discount(p, "3 for 2", -discount_amount)

                    if offer.offer_type == SpecialOfferType.TEN_PERCENT_DISCOUNT:
                        discount = Discount(p, str(offer.argument) + "% off",
                                            -quantity * unit_price * offer.argument / 100.0)

                    if offer.offer_type == SpecialOfferType.FIVE_FOR_AMOUNT and quantity_as_int >= 5:
                        discount_total = unit_price * quantity - (
                                offer.argument * number_of_x + quantity_as_int % 5 * unit_price)
                        discount = Discount(p, str(x) + " for " + str(offer.argument), -discount_total)

                    if discount:
                        receipt.add_discount(discount)


    class Teller:

        def __init__(self, catalog):
            self.catalog = catalog
            self.offers = {}

        def add_special_offer(self, offer_type, product, argument):
            self.offers[product] = Offer(offer_type, product, argument)

        def checks_out_articles_from(self, the_cart):
            receipt = Receipt()
            product_quantities = the_cart.items
            for pq in product_quantities:
                p = pq.product
                quantity = pq.quantity
                unit_price = self.catalog.unit_price(p)
                price = quantity * unit_price
                receipt.add_product(p, quantity, unit_price, price)

            the_cart.handle_offers(receipt, self.offers, self.catalog)

            return receipt






