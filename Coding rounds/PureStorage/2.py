def check_log_history(events):

    numEvents = 0
    eventStack = []
    lockSet = set()

    for event in events:
        numEvents += 1
        lockAction, lockNumber = event.split(" ")
        if (lockAction == "ACQUIRE" and lockNumber in lockSet) or (
            lockAction == "RELEASE" and lockSet and lockNumber != eventStack[-1]
        ):
            return numEvents
        elif lockAction == "RELEASE":
            lockSet.remove(eventStack.pop())
        else:
            eventStack.append(lockNumber)
            lockSet.add(lockNumber)

    return 0 if not lockSet else numEvents + 1


print(check_log_history(["ACQUIRE 364", "ACQUIRE 84", "RELEASE 84", "RELEASE 364"]))
