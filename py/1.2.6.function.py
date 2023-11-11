def shut_down(s):
    if s == "Yes":
        return "Shutting down"
    elif s == "yes":
        return "Shutting down"
    elif s == "YES":
        return "Shutting down"
    elif s == "No":
        return "Shutdown aborted"
    elif s == "no":
        return "Shutdown aborted"
    elif s == "NO":
        return "Shutdown aborted"
    else:
        return "Sorry"