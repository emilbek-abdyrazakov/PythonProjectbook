guests = ['emil', 'ulan', 'aziz', 'talant']
guest_popped1 = guests.pop(0)
#invitation = (f"I would like to invite you {guest_popped.title()} for a dinner tonight!!!")
invitation1 =(f"I would like to invite you {guest_popped1.title()} for a dinner tonight!!! ")

guests.insert( 1,'kuba')
print(guests)
guests.remove('talant')
print(guests)
guests.pop(1)
print(guests)