

def fuzzy_match_game_name(name: str) -> str:
    """
    Evaluate name of the game from different kinds of name
    """
    name = name.lower()
    if 'plo' in name :
        if "4" in name:
            return 'plo4'
        elif "5" in name:
            return 'plo5'
        elif "6" in name:
            return 'plo6'
        else:
            # Default to plo4
            return 'plo4'
    elif 'pot' in name:
        if "4" in name:
            return 'plo4'
        elif "5" in name:
            return 'plo5'
        elif "6" in name:
            return 'plo6'
        else:
            # Default to plo4
            return 'plo4'
    elif 'omaha' in name:
        if '4' in name:
            return 'plo4'
        elif '5' in name:
            return 'plo5'
        elif '6' in name:
            return 'plo6'
        else:
            # Default to plo4
            return 'plo4'
    elif 'hold' in name or 'texas' in name:
        return 'nlh'
    else:
        raise ValueError("Unknown game name: {}".format(name))
