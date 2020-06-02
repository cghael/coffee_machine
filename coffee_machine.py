# resources: water, milk, coffee_beans, cups, money
resources = [["water", 400], ["milk", 540], ["coffee beans", 120], ["disposable cups", 9], ["money", 550]]
# coffee: [espresso, latte, cappuccino]
coffee = [[-250, 0, -16, -1, 4], [-350, -75, -20, -1, 7], [-200, -100, -12, -1, 6]]


def status_inf():
    print("\nThe coffee machine has:")
    for i in range(5):
        if i == 4 and resources[i][1] > 0:
            print("$" + str(resources[i][1]), "of", resources[i][0])
        else:
            print(resources[i][1], "of", resources[i][0])


def ft_check_supl(choice):
    errors = 0
    for i in range(4):
        if resources[i][1] < -coffee[choice][i]:
            print("Sorry, not enough", resources[i][0] + "!")
            errors += 1
    return errors


def ft_buy():
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    if choice == "back":
        return
    choice = int(choice) - 1
    if ft_check_supl(choice) == 0:
        for i in range(5):
            resources[i][1] += coffee[choice][i]
        print("I have enough resources, making you a coffee!")


def ft_fill():
    resources[0][1] += int(input("Write how many ml of water do you want to add: "))
    resources[1][1] += int(input("Write how many ml of milk do you want to add: "))
    resources[2][1] += int(input("Write how many grams of coffee beans do you want to add: "))
    resources[3][1] += int(input("Write how many disposable cups of coffee do you want to add: "))


def ft_take():
    print("I gave you $" + str(resources[4][1]))
    resources[4][1] = 0


while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == "buy":
        ft_buy()
    if action == "fill":
        ft_fill()
    if action == "take":
        ft_take()
    if action == "remaining":
        status_inf()
    if action == "exit":
        break
