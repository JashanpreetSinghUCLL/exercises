def card_value(string):
    stringed = str(string)
    lowerCased = stringed.lower()
    if lowerCased == "jack":
        return 11
    elif lowerCased == "queen":
        return 12
    elif lowerCased == "king":
        return 13
    elif lowerCased == "ace":
        return 1
    else: 
        return int(stringed)

print(card_value("2"))