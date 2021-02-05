class Stonk():
    def __init__(self, buy, sell, option):
        self.buy = buy
        self.sell = sell
        self.option = option

    def print(self):
        print("Buy price: " + str(self.buy))
        print("Sell price: " + str(self.sell))
        print("Option type: " + str(self.option))


sams_account = Stonk(100, 200, "put")

sams_account.print()

