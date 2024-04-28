#TODO please keep in mind this is not tested in judge, so could not be 100/100 if submitted directly

data = input()

info = {}


while not data == "Sail":
    city, population, gold = data.split("||")
    population = int(population)
    gold = int(gold)
    if city not in info:
        info[city] = {"population": population, "gold": gold}
    else:
        info[city]["population"] += population
        info[city]["gold"] += gold
    data = input()

data = input()

while not data == "End":

    if data.startswith("Plunder"):
        command, town, people, gold = data.split("=>")
        people = int(people)
        gold = int(gold)
        info[town]['population'] -= people
        info[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if info[town]['gold'] <= 0 or info[town]['population'] <= 0:
            del info[town]
            print(f"{town} has been wiped off the map!")
    elif data.startswith("Prosper"):
        command, town, gold = data.split("=>")
        gold = int(gold)
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            info[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {info[town]['gold']} gold.")

    data = input()


sorted_info = sorted(info.items(), key=lambda tkvp: (-tkvp[1]["gold"], tkvp[0]))

if sorted_info:
    print(f"Ahoy, Captain! There are {len(sorted_info)} wealthy settlements to go to:")
    for key, value in sorted_info:
        print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")