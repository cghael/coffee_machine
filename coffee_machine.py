def status_inf(water, milk, gr, cups):
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(gr, "of coffee beans")
    print(cups, "of disposable cups")


water = int(input("Write how many ml of water the coffee machine has: "))
milk = int(input("Write how many ml of milk the coffee machine has: "))
gr = int(input("Write how many grams of coffee beans the coffee machine has: "))
cups = int(input("Write how many cups of coffee you will need: "))

status_inf(water, milk, gr, cups)

min_cups = water // 200
if min_cups > milk // 50:
    min_cups = milk // 50
if min_cups > gr // 15:
    min_cups = gr // 15
if min_cups < cups:
    print("No, I can make only", min_cups, "cups of coffee")
elif min_cups == cups:
    print("Yes, I can make that amount of coffee")
else:
    print("Yes, I can make that amount of coffee (and even", min_cups - cups, "more than that)")
