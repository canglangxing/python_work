guests = ['Einstein','Bohr','Planck']
# print(f"Dear {guests[0]}, it's my honor to invite you to dinner.")
# print(f"Dear {guests[1]}, it's my honor to invite you to dinner.")
# print(f"Dear {guests[2]}, it's my honor to invite you to dinner.")

absent_guest = guests.pop(1)
# print(f"I am sorry {absent_guest} won't be able to keep the appointment.")

guests.insert(1,'Dirac')
# print(f"Dear {guests[0]}, it's my honor to invite you to dinner.")
# print(f"Dear {guests[1]}, it's my honor to invite you to dinner.")
# print(f"Dear {guests[2]}, it's my honor to invite you to dinner.")

# print("Fortunately, I just found a bigger table")

guests.insert(0,'Newton')
guests.insert(2,'Guass')
guests.append('Maxwell')

# print(f"Dear {guests[0]}, it's my honor to invite you to dinner.")
# print(f"Dear {guests[1]}, it's my honor to invite you to dinner.")
# print(f"Dear {guests[2]}, it's my honor to invite you to dinner.")
# print(f"Dear {guests[3]}, it's my honor to invite you to dinner.")
# print(f"Dear {guests[4]}, it's my honor to invite you to dinner.")
# print(f"Dear {guests[5]}, it's my honor to invite you to dinner.")

print("Unfortunately, I can only invite two guests.")
absent_guest = guests.pop()
print(f"Dear {absent_guest}, I am sorry I can't invite you to dinner.")
absent_guest = guests.pop()
print(f"Dear {absent_guest}, I am sorry I can't invite you to dinner.")
absent_guest = guests.pop()
print(f"Dear {absent_guest}, I am sorry I can't invite you to dinner.")
absent_guest = guests.pop()
print(f"Dear {absent_guest}, I am sorry I can't invite you to dinner.")
print(f"Dear {guests[0]}, it's my honor to invite you to dinner.")
print(f"Dear {guests[1]}, it's my honor to invite you to dinner.")
del guests[0]
del guests[0]
print(guests)