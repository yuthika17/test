import datetime 
import bday_messages
today=datetime.date.today()
next_birthday=datetime.date(2026,8,25)
days_away=today-next_birthday
if today==next_birthday :
  print(bday_messages.random_message)
else:
  print(f'My next birthday is {days_away} days away!')