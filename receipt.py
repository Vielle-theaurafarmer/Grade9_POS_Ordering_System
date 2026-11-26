class Receipt:

    def __init__(self, store_name):
        self.store_name = store_name
        self.total = 0

    def calculate_total(self, order):
        self.total = 0

        for item in order:
            self.total += item["subtotal"]

        return self.total

    def display_receipt(self, order):

        print("\n================================")
        print("       ", self.store_name)
        print("          ORDER RECEIPT")
        print("================================")

        for item in order:
            print("Product:", item["name"])
            print("Quantity:", item["quantity"])
            print("Price: P", format(item["price"], ".2f"))
            print("Subtotal: P", format(item["subtotal"], ".2f"))
            print("--------------------------------")

        self.calculate_total(order)

        print("TOTAL AMOUNT: P", format(self.total, ".2f"))
        print("================================")
        print("     Thank you for ordering!")
        print("================================")

receipt = Receipt("PSHS SCHOOL CANTEEN")