class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address
  #devuelve una lista de los objetos menus disponible en ese horario
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus
#Crearemos negocio que venda arepas
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises




class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return self.name + " menu available at " + str(self.start_time) + " - " + str(self.end_time)

    #Devuelve el precio total de todo lo comprado
  def calculate_bill(self, purchased_items):
      bill = 0
      for purchased_item in purchased_items:
        if purchased_item in self.items:
          bill += self.items[purchased_item]
        return bill

brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
} 

early_bird = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
dinner = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kids = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

#Creo obj: El menu del Desayuno: brunch_menu
brunch_menu = Menu("Brunch", brunch_items, 1100, 1600 )
#Creo objeto: El menu del almuerzo early_menu
early_menu = Menu("Early-bird", early_bird, 1500, 1800)
#Creo objeto: El menu de la cena: dinner_menu 
dinner_menu = Menu("Dinner", dinner, 1700, 2300)
#Creo objeto: el menu de niños: kids_menu 
kids_menu = Menu("kids", kids, 1100, 2100)
#Creo objeto: menu de Arepas
arepas_menu = Menu("Take a' Arepa", arepas_items, 1000,2000)

#__repr__() cadenade representación de nuestra instancia 
print(brunch_menu)
#Ordeno desayuno realizando instancia con calculate_bill()
print(brunch_menu.calculate_bill(["pancakes", "home fries", "coffee"]))

print(early_menu.calculate_bill(["salumeria plate", "mushroom ravioli(vegan)"]))


menus = [brunch_menu, early_menu, dinner_menu, kids_menu ]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

print(flagship_store)
#conocer que menus estan disponibles en ese horario
print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

arepa = Business("Take a' Arepa", [arepas_place])
print(arepa.franchises[0].menus[0])


















 
