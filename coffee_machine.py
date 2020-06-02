# resources: water, milk, coffee_beans, cups, money
resources = [["water", 400], ["milk", 540], ["coffee beans", 120], ["disposable cups", 9], ["money", 550]]
# coffee: [espresso, latte, cappuccino]
coffee = [[-250, 0, -16, 4], [-350, -75, -20, 7], [-200, -100, -12, +6]]


def status_inf():
    print("\nThe coffee machine has:")
    for i in range(5):
        if i == 4:
            print("$" + str(resources[i][1]), "of", resources[i][0])
        else:
            print(resources[i][1], "of", resources[i][0])


def find_min_cups(water, milk, gr, cups):
    min_cups = water // 200
    if min_cups > milk // 50:
        min_cups = milk // 50
    if min_cups > gr // 15:
        min_cups = gr // 15
    if min_cups > cups:
        min_cups = cups
    return min_cups


def ft_check_supl(choose):
    errors = 0
    if resources[0][1] < -coffee[choose][0]:
        print("Sorry, not enough", resources[0][0] + "!")
        errors += 1
    elif resources[1][1] < -coffee[choose][1]:
        print("Sorry, not enough", resources[1][0] + "!")
        errors += 1
    elif resources[2][1] < -coffee[choose][2]:
        print("Sorry, not enough", resources[2][0] + "!")
        errors += 1
    elif resources[3][1] < 1:
        print("Sorry, not enough", resources[3][0] + "!")
        errors += 1
    return errors


def ft_buy():
    global resources
    choose = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    if choose == "back":
        return
    choose = int(choose) - 1
    if ft_check_supl(choose) == 0:
        resources[0][1] += coffee[choose][0]
        resources[1][1] += coffee[choose][1]
        resources[2][1] += coffee[choose][2]
        resources[3][1] += -1
        resources[4][1] += coffee[choose][3]
        print("I have enough resources, making you a coffee!")


def ft_fill():
    global resources
    resources[0][1] += int(input("Write how many ml of water do you want to add: "))
    resources[1][1] += int(input("Write how many ml of milk do you want to add: "))
    resources[2][1] += int(input("Write how many grams of coffee beans do you want to add: "))
    resources[3][1] += int(input("Write how many disposable cups of coffee do you want to add: "))


def ft_take():
    global resources
    print("I gave you $" + str(resources[4][1]))
    resources[4][1] = 0


action = input("Write action (buy, fill, take, remaining, exit): ")
while action != "exit":
    if action == "buy":
        ft_buy()
    elif action == "fill":
        ft_fill()
    elif action == "take":
        ft_take()
    elif action == "remaining":
        status_inf()
    action = input("\nWrite action (buy, fill, take, remaining, exit): ")
