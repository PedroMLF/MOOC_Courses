#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def floor_puzzle():
    # Your code here
    
    # Define the floors
    floors = list(range(1,6))
    bottom = 1; top = 5
    
    # List with all the possible combinations
    combinations = list(itertools.permutations(floors))

    # Following the same logic than in lectures
    return list(next((Hopper, Kay, Liskov, Perlis, Ritchie)
                for (Hopper, Kay, Liskov, Perlis, Ritchie) in combinations
                if not Hopper is top
                if not Kay is bottom
                if not Liskov is top
                if not Liskov is bottom
                if Perlis > Kay
                if abs(Ritchie-Liskov) != 1
                if abs(Liskov-Kay) != 1
                ))
