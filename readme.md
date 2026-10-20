print("\033[33m a world of heroes from strength to flight, who will you be")
while True:
    player = input("What is your name? ")

    print("your name is ", player, "correct?")
    i = input("yes/no: \033[0m")
    if i == "yes":
            break

print("\033[031m Why do you always assume every tale must be yours?\033[0m")
for i in range(5):
        print(" ", end="")
