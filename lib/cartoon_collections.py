def roll_call_dwarves(dwarves):
    for n in range(len(dwarves)):         
        print(f"{n+1}. {dwarves[n]}")
    pass

def summon_captain_planet(planeteer_calls):
    call_list = []
    for calls in planeteer_calls:
        call_list.append(f"{calls.capitalize()}!")
    return call_list
    pass

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) >= 5 :
            return True
    return False
    pass

def find_the_cheese(snacks):
    cheeses = ["cheddar", "gouda", "camembert"]
    for cheese in cheeses:
        if cheese in snacks:
            return cheese
    return None        
    pass
