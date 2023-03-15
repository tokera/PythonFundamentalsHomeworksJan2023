contact = input()
contacts = {}
while not contact.isdigit():
    name, num = contact.split("-")
    contacts[name] = num

    contact = input()

for _ in range(int(contact)):
    searched_contact = input()
    if searched_contact in contacts:
        print(f"{searched_contact} -> {contacts[searched_contact]}")
    else:
        print(f"Contact {searched_contact} does not exist.")
