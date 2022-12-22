def are_you_playing_banjo(name):
    for i in name:
        if i =='R' or i=='r':
            return name + " plays banjo"
        else:
            return name + " does not play banjo"