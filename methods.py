class event:
    name = 0
    workers = 0
    date = 0

    def __init__(self, name, workers, date):
        self.name = name
        self.date = date
        self.workers = workers

class missing:
    name = 0
    date = 0

    def __init__(self, name, date):
        self.name = name
        self.date = date

class conflict:
    name = 0
    worker = 0
    date = 0

    def __init__(self, name, worker, date):
        self.name = name
        self.worker = worker
        self.date = date

def readPeople():
    file = open("people.txt", "r")
    data = file.readlines()
    file.close()
    for i in range(len(data)):
        data[i] = data[i].strip()
    return data

def readEvents():
    file = open("events.txt", "r")
    raw = file.readlines()
    file.close()
    data = []

    for i in raw:
        attributes = i.split(';')
        name = attributes[0]
        workers = attributes[1].split(',')
        date = attributes[2]
        data.append(event(name, workers, date))

    return data

def readMissing():
    file = open("missing.txt", "r")
    raw = file.readlines()
    file.close()
    data = []
    for i in range(len(raw)):
        capsule = raw[i].split(' ')
        data.append(missing(capsule[0].replace('_', ' '), capsule[1]))

    return data

def conflicts(events, missing):
    conflicts = []
    for i in events:
        for j in i.workers:
            print(f"Checking fella: {j} at {i.date}", end="")
            for k in missing:
                print(f"  Missing name: {k.name}  date: {k.date}")
                if j == k.name and i.date == k.date:
                    print("conflict found")
                    conflicts.append(conflict(name=events[i].name, worker=missing[k].name, date=missing[k].date))
                else:
                    print(f"name: {j}, {k.name}  date: {i.date}, {k.date}")
    return conflicts
