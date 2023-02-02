note = input().split("-")

notes = [0 for x in range(10)]

while not note[0] == "End":
    notes.pop(int(note[0]) - 1)
    notes.insert(int(note[0]) - 1, note[1])

    #notes[int(note[0]) - 1] = note[1]

    note = input().split("-")

result = [el for el in notes if not el == 0]
print(result)
