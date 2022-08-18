# Project: Franchise
# Author: Joe Fraser
# Description: Demonstration on class building a Menu class, Dictionary and list items.


brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}

dinner_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

arepa_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

class Menu:
  
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return (f"{self.name} menu item will be available from {self.start_time} to {self.end_time}")

  def calculate_bill(self, purchased_items):
    total_cost = 0
    for item in purchased_items:
      if item in self.items:
        total_cost += self.items[item]
    return total_cost

class Franchise:

  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def available_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time < menu.end_time:
        available_menu.append(menu)
    return (available_menu)

  def __repr__(self):
    return (f"Franchise at {self.address}")

class Business:
  
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

if __name__ == '__main__':
    
  brunch = Menu("Brunch", brunch_items, 1100, 1600)
   
  early_bird = Menu("Early Bird",early_bird_items ,1500 ,1800 )

  dinner = Menu("Dinner", dinner_items, 1700, 2300)

  kids = Menu("Kids", kids_items, 1100, 2100)

  brunch_list = ['pancakes', 'espresso', 'mimosa']

  #print(brunch.calculate_bill(brunch_list))

  #print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)' ]))

  flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
  new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

  #print(flagship_store.available_menus(1200))
  #print(new_installment.available_menus(1700))

  basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

  arepas_menu = Menu("Take a’ Arepa", arepa_items, 1000, 2000)

  arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

  take_arepa = Business("Take a' Arepa", arepas_place)