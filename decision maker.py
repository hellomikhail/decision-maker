import random

def decision_maker():
   short_list = []
   while True:
       item = input("Enter your items")
       if item == 'stop':
           print(random.choice(short_list))
           break
       else:
           short_list.append(item)
           print(short_list)

decision_maker()