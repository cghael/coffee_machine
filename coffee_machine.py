class CoffeeMachine:
    espresso = [-250, 0, -16, -1, 0]
    latte = [-350, -75, -20, -1, 0]
    cappuccino = [-200, -100, -12, -1, 0]
    coffee = [espresso, latte, cappuccino]
    resources = [["water", 0], ["milk", 0], ["coffee beans", 0], ["disposable cups", 0], ["money", 0]]

    def __init__(self, water, milk, beans, cups, money):
        self.resources[0][1] = water
        self.resources[1][1] = milk
        self.resources[2][1] = beans
        self.resources[3][1] = cups
        self.resources[4][1] = money

    def set_prices(self, espresso_price, latte_price, cappuccino_price):
        self.coffee[0][4] = espresso_price
        self.coffee[1][4] = latte_price
        self.coffee[2][4] = cappuccino_price

    def status_info(self):
        print("\nThe coffee machine has:")
        for i in range(5):
            if i == 4:
                print("$" + str(self.resources[i][1]), "of", self.resources[i][0] + "\n")
            else:
                print(self.resources[i][1], "of", self.resources[i][0])

    def fill(self):
        self.resources[0][1] += int(input("\nWrite how many ml of water do you want to add: "))
        self.resources[1][1] += int(input("Write how many ml of milk do you want to add: "))
        self.resources[2][1] += int(input("Write how many grams of coffee beans do you want to add: "))
        self.resources[3][1] += int(input("Write how many disposable cups of coffee do you want to add: "))
        print()

    def take(self):
        print("\nI gave you $" + str(self.resources[4][1]) + "\n")
        self.resources[4][1] = 0

    def check_supplies(self, choice):
        errors = 0
        for i in range(4):
            if self.resources[i][1] < -self.coffee[choice][i]:
                print("Sorry, not enough", self.resources[i][0] + "!")
                errors += 1
        return errors

    def buy(self):
        choice = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if choice == "back":
            return
        choice = int(choice) - 1
        if self.check_supplies(choice) == 0:
            for i in range(5):
                self.resources[i][1] += self.coffee[choice][i]
            print("\nI have enough resources, making you a coffee!\n")

    def action(self, user_action):
        if user_action == "buy":
            self.buy()
        if user_action == "fill":
            self.fill()
        if user_action == "take":
            self.take()
        if user_action == "remaining":
            self.status_info()


my_machine = CoffeeMachine(400, 540, 120, 9, 550)
my_machine.set_prices(4, 7, 6)  # here user can change prices by himself through the interface
while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == "exit":
        break
    else:
        my_machine.action(action)
