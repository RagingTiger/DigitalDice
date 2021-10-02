# std libs
import random


# funcs
def average_random_matches(events: int, trials: int) -> float:
    """Return average number of random matches for a given number of trials."""
    # setup model system of all possible events
    system = [i for i in range(events)]
        
    # capture matches
    matches = 0
    
    # begin trials
    for _ in range(trials):
        # scramble
        random.shuffle(system)
        
        # iterate over index/element pairs
        for i, element in enumerate(system):
            # check for matching pairs
            if i == element:
                # increase running total of random matches
                matches += 1
                
    # return average number of random matches
    return matches / trials

    
def presidents_problem(pres: int = 24, trials: int = 1000) -> float:
    """Presidents Problem from the introduction of `Digital Dice` by Paul J. Nahin."""
    # get average matches
    return average_random_matches(pres, trials)

        
    

    