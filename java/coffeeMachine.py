# Python : builder object mvc coffeMachine with OOP 


class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.state = "choosing an action"

    def __str__(self):
        return f"""The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.beans} of coffee beans
        {self.cups} of disposable cups
        {self.money} of money"""

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        choice = input()
        if choice == "1":
            if self.water < 250:
                print("[-] Sorry, not enough water!")
            elif self.beans < 16:
                print("[-] Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("[-] Sorry, not enough cups!")
            else:
                print("[+] I have enough resources, making you a coffee!")
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4


        elif choice == "2":
            if self.water < 350:
                print("[-] Sorry, not enough water!")
            elif self.milk < 75:
                print("[-] Sorry, not enough milk!")
            elif self.beans < 20:
                print("[-] Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("[-] Sorry, not enough cups!")
            else:
                print("[+] I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7


        elif choice == "3":
            if self.water < 200:
                print("[-] Sorry, not enough water!")
            elif self.milk < 100:
                print("[-] Sorry, not enough milk!")
            elif self.beans < 12:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("[+] Sorry I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6

        elif choice == "back":
            pass

    def fill(self):
        print("[?] Write how many ml of water do you want to add:")
        self.water += int(input())
        print("[?] Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("[?] Write how many grams of coffee beans do you want to add:")
        self.beans += int(input())
        print("[?] Write how many disposable cups of coffee do you want to add:")
        self.cups += int(input())

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def remaining(self):
        print(self)

    def run(self):
        while True:
            print("Write action -> [1] buy, [2] fill, [3] take, [4] remaining, [5] exit <-")
            action = int(input())
            if action == 1:
                self.buy()
            elif action == 2:
                self.fill()
            elif action == 3:
                self.take()
            elif action == 4:
                self.remaining()
            elif action == 5:
                break


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
coffee_machine.run()
