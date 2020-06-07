class CoffeeMachine:
    espresso = [-250, 0, -16, -1, 0]
    latte = [-350, -75, -20, -1, 0]
    cappuccino = [-200, -100, -12, -1, 0]
    coffee = [espresso, latte, cappuccino]
    resources = [["water", 0], ["milk", 0], ["coffee beans", 0], ["disposable cups", 0], ["money", 0]]
    fill_status = ["\nWrite how many ml of water do you want to add: ",
                   "Write how many ml of milk do you want to add: ",
                   "Write how many grams of coffee beans do you want to add: ",
                   "Write how many disposable cups of coffee do you want to add: "]

    def __init__(self, water, milk, beans, cups, money):
        self.resources[0][1] = water
        self.resources[1][1] = milk
        self.resources[2][1] = beans
        self.resources[3][1] = cups
        self.resources[4][1] = money
        self.status = "action"
        self.fill_step = 0

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

    def fill(self, action):
        if self.fill_step == 0:
            print(self.fill_status[self.fill_step])
            self.fill_step += 1
        elif self.fill_step < 4:
            self.resources[self.fill_step - 1][1] += int(action)
            print(self.fill_status[self.fill_step])
            self.fill_step += 1
        else:
            self.resources[self.fill_step - 1][1] += int(action)
            self.fill_step = 0
            self.status = "action"
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

    def buy(self, choice):
        if choice == "back":
            self.status = "action"
            return
        choice = int(choice) - 1
        if self.check_supplies(choice) == 0:
            for i in range(5):
                self.resources[i][1] += self.coffee[choice][i]
            print("\nI have enough resources, making you a coffee!\n")
        self.status = "action"

    def choose(self, user_action):
        if user_action == "buy":
            self.status = "buy"
        if user_action == "fill":
            self.status = "fill"
        if user_action == "take":
            self.take()
        if user_action == "remaining":
            self.status_info()

    def user_input(self):
        action = ""
        while True:
            if self.status == "action":
                print("Write action (buy, fill, take, remaining, exit):\n")
            elif self.status == "buy":
                print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
            else:
                self.fill(action)
            action = input()
            if self.status == "action":
                if action == "exit":
                    break
                else:
                    self.choose(action)
            elif self.status == "buy":
                self.buy(action)


my_machine = CoffeeMachine(400, 540, 120, 9, 550)
my_machine.set_prices(4, 7, 6)  # here user can change prices by himself through the interface
my_machine.user_input()
