dect = {}
command = input()
while command != "end":
    course, name = command.split(" : ")
    if course not in dect:
        dect[course] = []
    dect[course].append(name)
    command = input()
for courses in sorted(dect, key = lambda x: len(dect[x]), reverse=True):
    print(f"{courses}: {len(dect[courses])}")
    for contestants in sorted(dect[courses]):
        print(f"-- {contestants}")
