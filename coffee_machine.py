water = 400
milk = 540
gr = 120
cups = 9
money = 550


def status_inf():
    global water
    global milk
    global gr
    global cups
    global money
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(gr, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")


def find_min_cups(water, milk, gr, cups):
    min_cups = water // 200
    if min_cups > milk // 50:
        min_cups = milk // 50
    if min_cups > gr // 15:
        min_cups = gr // 15
    if min_cups > cups:
        min_cups = cups
    return min_cups


def ft_buy():
    global water
    global milk
    global gr
    global cups
    global money
    choose = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
    if choose == 1:
        water -= 250
        gr -= 16
        cups -= 1
        money += 4
    elif choose == 2:
        water -= 350
        milk -= 75
        gr -= 20
        cups -= 1
        money += 7
    else:
        water -= 200
        milk -= 100
        gr -= 12
        cups -= 1
        money += 6


def ft_fill():
    global water
    global milk
    global gr
    global cups
    global money
    water += int(input("Write how many ml of water do you want to add:"))
    milk += int(input("Write how many ml of milk do you want to add:"))
    gr += int(input("Write how many grams of coffee beans do you want to add:"))
    cups += int(input("Write how many disposable cups of coffee do you want to add:"))


def ft_take():
    global money
    print("I gave you $" + str(money))
    money = 0


status_inf()
action = input("Write action (buy, fill, take): ")
if action == "buy":
    ft_buy()
elif action == "fill":
    ft_fill()
else:
    ft_take()
status_inf()

"""
min_cups = find_min_cups(water, milk, gr, cups)
if min_cups < cups:
    print("No, I can make only", min_cups, "cups of coffee")
elif min_cups == cups:
    print("Yes, I can make that amount of coffee")
else:
    print("Yes, I can make that amount of coffee (and even", min_cups - cups, "more than that)")
"""
