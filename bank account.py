# Write code below 💖
class bankaccount :
  def __init__(self , first_name , last_name , account_id , account_type , pin , balance ):
   self.first_name = first_name
   self.last_name = last_name
   self.account_id =account_id
   self.account_type = account_type
   self.pin = pin
   self.balance = balance
  def deposit(self) :
    self.balance+=float(input('add the money .'))
    return self.balance 
  def withdraw (self):
    a=float(input('how much money you take ? '))
    self.balance-=a
    return a
  def display_balance(self):
    print('balance: ', self.balance)
someone=bankaccount('gojo','saturo',123,'normal',4,100.0)
someone.deposit()
someone.withdraw()
someone.display_balance()