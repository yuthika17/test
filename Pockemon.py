# Write code below 💖
class pockemon :
  def __init__(self,entry,name,types,description,is_caught):
    self.entry=entry
    self.name=name
    self.types=types
    self.description=description
    self.is_caught=is_caught
  def speak(self):
    print(self.name)
    print(self.name)
  def display_details(self):
    print('Entry Number : ',self.entry)
    print('Name : ',self.name)
    print('Type : ',self.types)
    print('Description : ',self.description)
    if self.is_caught== False :
      print(self.name,'has already been caught !')
    else :
      print(self.name,'is desponible !')
Pokemon=pockemon(25,'Pikachu','Electric','It has small electric sacs on both its cheeks .',False)
Pokemon.speak()
Pokemon.display_details()