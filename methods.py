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
    file = open("people.txt", "r", encoding="utf-8")
    data = file.readlines()
    file.close()
    for i in range(len(data)):
        data[i] = data[i].strip()
    return data

def readEvents():
    file = open("events.txt", "r", encoding="utf-8")
    raw = file.readlines()
    file.close()
    data = []

    for i in raw:
        attributes = i.split(';')
        name = attributes[0]
        workers = attributes[1].split(',')
        for i in range(len(workers)):
            workers[i] = workers[i].strip()
        date = attributes[2]
        date.strip()
        data.append(event(name, workers, date))

    return data

def readMissing():
    file = open("missing.txt", "r", encoding="utf-8")
    raw = file.readlines()
    file.close()
    data = []
    for i in range(len(raw)):
        capsule = raw[i].split(' ')
        date = capsule[1].strip()
        data.append(missing(capsule[0].replace('_', ' '), date))

    return data

def conflicts(events, missing):
    conflicts = []
    for i in events:
        for j in i.workers:
            #print(f"Checking fella: {j} at {i.date}", end="")
            for k in missing:
                #print(f"  Missing name: {k.name}  date: {k.date}")
                if j == k.date:
                    print("dates match")
                    if i.name == k.name:
                        print("names match")
                        conflicts.append(conflict(name=events[i].name, worker=missing[k].name, date=missing[k].date))
    return conflicts
