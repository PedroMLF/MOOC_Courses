# -----------------
# User Instructions
# 
# In this problem, you will complete the code for the hold_at(x) 
# function. This function returns a strategy function (note that 
# hold_at is NOT the strategy function itself). The returned 
# strategy should hold if and only if pending >= x or if the 
# player has reached the goal.

goal = 50

def hold_at(x):
    """Return a strategy that holds if and only if 
    pending >= x or player reaches goal."""
    def strategy(state):
        # your code here
        if state[3] >= x or state[1]+state[3] >= goal:
            return "hold"
        else:
            return "roll"
    strategy.__name__ = 'hold_at(%d)' % x
    return strategy

def test():
    assert hold_at(30)((1, 29, 15, 20)) == 'roll'
    print("Passed test 1")
    assert hold_at(30)((1, 29, 15, 21)) == 'hold'
    print("Passed test 2")
    assert hold_at(15)((0, 2, 30, 10))  == 'roll'
    print("Passed test 3")
    assert hold_at(15)((0, 2, 30, 15))  == 'hold'
    return 'tests pass'

print test()
