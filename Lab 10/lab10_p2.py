# Problem 2

guests = {'Grace Hopper': 2, 'Richard Tapia': 3,'Timnit Gebru': 1,'Radia Perlman': 4, 'Ada Lovelace': 2,'Ruzena Bajcsy': 1}

more_than_1 = []
# Add your code below
for guest, additional_guests in guests.items():
    if additional_guests > 1:
        more_than_1.append(guest)
print (more_than_1)