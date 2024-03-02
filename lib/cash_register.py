class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        item_cost = price * quantity
        self.total += item_cost
        self.items.append({"title": title, "price": price, "quantity": quantity})
        self.last_transaction = item_cost

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            message = f"After the discount, the total comes to ${self.total:.2f}.\n"
            print(message)
            return message
        else:
            return "There is no discount to apply.\n"

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            self.total -= last_item["price"] * last_item["quantity"]
            self.last_transaction = -last_item["price"] * last_item["quantity"]
            return "Last transaction voided.\n"
        else:
            return "No transactions to void.\n"

    def get_items(self):
        return [item["title"] for item in self.items]

    def reset_register(self):
        self.total = 0
        self.items = []
        self.last_transaction = 0
        return "Register reset. Total is now $0.00.\n"
