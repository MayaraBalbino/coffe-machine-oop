class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, agua, leite, cafe, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "agua": agua,
            "leite": leite,
            "cafe": cafe,
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="ao leite", agua=200, leite=150, cafe=24, cost=2.5),
            MenuItem(name="expresso", agua=50, leite=0, cafe=18, cost=1.5),
            MenuItem(name="cappuccino", agua=250, leite=50, cafe=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Desculpe, item inválido.")
