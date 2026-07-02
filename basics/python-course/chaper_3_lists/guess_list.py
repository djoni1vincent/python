people = ["lilia", "nikita", "dima", "nikita", ]

print(f"Hi, come to dinner, {people[0]}!")
print(f"Hi, come to dinner, {people[1]}!")
print(f"Hi, come to dinner, {people[2]}!")
print(f"Hi, come to dinner, {people[3]}!")

print(f"{people[3]} can't join us, we need to find someone else...")

del people[3]

people.append("sanya")
print(f"Hi, come to dinner, {people[0]}!")
print(f"Hi, come to dinner, {people[1]}!")
print(f"Hi, come to dinner, {people[2]}!")
print(f"Hi, come to dinner, {people[3]}!")

print("I find bigger dinner table!!!")

people.insert(0, "oleg")
people.insert(3, "vasya")
people.insert(6, "oleg")

print(people[0])
print(people[1])
print(people[2])
print(people[3])
print(people[4])
print(people[5])
print(people[6])

print("Oh sorry, i have space just for 2")

last_person = people.pop(-1)
print(f"{last_person} Sorry, i don't have dinner for you (")
last_person = people.pop(-1)
print(f"{last_person} Sorry, i don't have dinner for you (")
last_person = people.pop(-1)
print(f"{last_person} Sorry, i don't have dinner for you (")
last_person = people.pop(-1)
print(f"{last_person} Sorry, i don't have dinner for you (")
last_person = people.pop(-1)
print(f"{last_person} Sorry, i don't have dinner for you (")

print(f"{people[0]} and {people[1]} u are still invited")

del people[0]
del people[-1]

print(people)