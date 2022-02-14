from methods import *

running = True
people = readPeople()
events = readEvents()
missings = readMissing()

while running:
    line = input("digiHetes$")
    args = line.split(' ')
    command = 0
    try:
        command = args[0]
    except:
        print("Please enter a command")
        continue
    if command == "exit":
        running = False

    elif command == "events":
        for i in range(len(events)):
            print(f"\nEvent number {i}:\n", "Event name: ", events[i].name, "\nWorkers: ", events[i].workers, "\nDate: ", events[i].date, sep="", end="\n")

    elif command == "people":
        for i in range(len(people)):
            print(people[i], end="\n")

    elif command == "missing":
        for i in range(len(missings)):
            print(f"name: {missings[i].name},    missing date: {missings[i].date}", sep='', end="")
        print()

    elif command == "new":
        which = 0
        try:
            which = args[1]
        except:
            print("Necessary argument: \'type\' not added")
            continue
        if which == "person":
            name = 0
            try:
                name = args[2]
            except:
                print("Neccessary argument: \'name\' not added")
                continue
            people.append(name.replace('_', ' '))
        elif which == "event":
            date = 0
            name = 0
            workers = []
            try:
                name = args[2]
            except:
                print("Neccessary argument: \'name\' not supplied")
            try:
                date = args[3]
            except:
                print("Neccessary argument: \'date\' not supplied")
            if len(args) > 4:
                for i in range(len(args)-4):
                    workers.append(args[4+i].replace('_', ' '))
            else:
                print("No personel were added, operation aborted")
            capsule = event(name, workers, date)
            print(f"\nEvent number {len(events)}:\n", "Event name: ", capsule.name, "\nWorkers: ",
                  capsule.workers, "\nDate: ", capsule.date, sep="", end="\n")
            events.append(capsule)
            print("Added event to temporary event list, update to save")
        elif which == "missing":
            name = 0
            date = 0
            try:
                name = args[2]
            except:
                print("Neccessary argument: \'name\' not added")
                continue
            try:
                date = args[3]
            except:
                print("Neccessary argument: \'date\' not added")
            print(f"New missing: name: {name},   date: {date}")
            print("Added to temporary missing list, update to save")
            missings.append((missing(name.strip().replace('_', ' '), date.strip())))

        else:
            print(f"Bad argument: {which}")

    elif command == "conflict":
        conflicts = conflicts(events, missings)
        print("\n", len(conflicts), "conflicts were found")
        for i in conflicts:
            print(f"fella: {i.worker} is missing from event: {i.name} at {i.date}")

    else:
        print(f"command: \'{command}\' not found")




print("Exiting digiHetes...")