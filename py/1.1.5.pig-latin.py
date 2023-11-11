original = raw_input('Welcome to the English to Pig Latin translator!')

def pig():
    if len(original) > 0:
        return original
    else:
        return "empty"

print pig()