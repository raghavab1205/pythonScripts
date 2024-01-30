class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


def get_event_date(events):
    return events.date


def history(events):
    events.sort(key=get_event_date)
    l = {"date": set(), "type": set(), "machine": set(), "user": set()}
    for event in events:
        l["date"].add(event.date)
        l["type"].add(event.type)
        l["machine"].add(event.machine)
        l["user"].add(event.user)
    for i, u in l.items():
        print(i, ":\t", u)

def current_users(events):
    events.sort(key=get_event_date)
    machines1 = {}
    machines2 = {}
    for event in events:
        if (event.machine not in machines1) and (event.machine not in machines2):
            machines1[event.machine] = set()
            machines2[event.machine] = set()
        if event.type == "login":
            if (event.user not in machines1[event.machine]) and (event.user not in machines2[event.machine]):
                machines1[event.machine].add(event.user)
            elif (event.user not in machines1[event.machine]) and (event.user in machines2[event.machine]):
                machines1[event.machine].add(event.user)
                machines2[event.machien].remove(event.machine)
        elif event.type == "logout":
            if (event.user in machines1[event.machine]) and (event.user not in machines2[event.machine]):
                machines1[event.machine].remove(event.user)
                machines2[event.machine].add(event.user)
            elif (event.user in machines1[event.machine]) and (event.user in machines2[event.machine]):
                machines1[event.machine].remove(event.user)
    return machines1, machines2


def generate_report(machines1, machines2):
    print("\nOnline users:\n")
    for machine, users in machines1.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

    print("\nOffline users:\n")
    for machine, users in machines2.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))


events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

history(events)
users1, users2 = current_users(events)
print("ONLINE USERS :", users1, "\nOFFLINE USRERS :", users2)
generate_report(users1, users2)
