# std libs
import random


# funcs
def average_uniform_events(events: int, trials: int) -> float:
    """Presidents Problem from the Introduction of `Digital Dice` by Paul J. Nahin"""
    # setup system of uniform events
    system = [i for i in range(events)]
        
    # capture matches
    matches = 0
    
    # begin trials
    for _ in range(trials):
        # scramble
        random.shuffle(system)
        
        # now check for matches
        for i, element in enumerate(system):
            # check for matches
            if i == element:
                matches += 1
                
    # return average number of matches
    return matches / trials

    
def presidents_problem(pres: int = 24, trials: int = 1000) -> float:
    """Presidents Problem from the Introduction of `Digital Dice` by Paul J. Nahin"""
    # get average events
    return average_uniform_events(pres, trials)

        
    

    