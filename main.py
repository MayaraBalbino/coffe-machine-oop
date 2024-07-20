from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    money_machine = MoneyMachine()
    coffe_maker = CoffeeMaker()
    menu = Menu()

    while True:
        cafe = input(f'Escolha um tipo de cafe: {menu.get_items()}\n')
        if cafe == "off":
            break
        elif cafe == 'report':
            coffe_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(cafe)
            if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)






if __name__ == '__main__':
    main()
