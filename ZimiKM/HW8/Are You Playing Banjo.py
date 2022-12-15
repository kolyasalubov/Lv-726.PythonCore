def are_you_playing_banjo(name) -> str:
    '''
    You plays banjo if ou name start with "R" or "r"
    else you don't play banjo
    
    Variable:
    name - string inputed by juser as argument
    
    Result:
    String: -name- play banjo or name does not plaj banjo
    '''
    if name[0].lower() == "r":
        return f'{name} plays banjo'
    return f'{name} does not play banjo'