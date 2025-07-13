# Write code below 💖
food=['🍔 Cheeseburger','🍟 Fries','🥤 Soda','🍦 Ice Cream','🍪 Cookie']
def get_item(a):
  return food[a-1]
def welcome():
  print('hi ! what would you like to eat today ?')
  print('1 for 🍔 Cheeseburger')
  print ('2 for 🍟 Fries')
  print ('3 for 🥤 Soda')
  print ('4 for 🍦 Ice Cream')
  print('5 for 🍪 Cookie')
welcome()
a=int(input('enter your choice : '))
print(get_item(a))