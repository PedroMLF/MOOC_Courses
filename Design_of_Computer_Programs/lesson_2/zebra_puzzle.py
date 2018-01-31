import itertools

def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1 # Your code here.

def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) # 1
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
                if imright(green, ivory)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                if Englishman is red
                if Norwegian is first
                if nextto(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in orderings
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Kools is yellow
                if LuckyStrike is oj
                if Japanese is Parliaments
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )

# ----------------------------------------------------------------------

import time

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result


def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers)) 


def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    # Your code here.

    times = []

    if isinstance(n, int):
        for i in range(n):
            time, _ = timedcall(fn, *args)
            times.append(time)
    
    else:

        while n > sum(times):
            time, _ = timedcall(fn, *args)
            times.append(time)
        
    return min(times), average(times), max(times)d


def average(list):
    """Return the average of a list"""
    return float(sum(list)/len(list))

# ----------------------------------------------------------------------

def zebra_puzzle2():
    "Return a tuple (WATER, ZEBRA indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) # 1
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in c(orderings)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in c(orderings)
                for (coffee, tea, milk, oj, WATER) in c(orderings)
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
                for (dog, snails, fox, horse, ZEBRA) in c(orderings)
               	if imright(green, ivory)
                if Englishman is red
                if Norwegian is first
                if nextto(Norwegian, blue)
                if coffee is green
                if Ukranian is tea
                if milk is middle
                if Kools is yellow
                if LuckyStrike is oj
                if Japanese is Parliaments
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )

def c(sequence):
	c.starts += 1
	for item in sequence:
		c.items += 1
		yield item

def instrument_fn(fn, *args):
	c.starts, c.items = 0, 0
	result = fn(*args)
	print "%s got %s %5d iters over %7d items" % (fn.__name__, result, c.starts, c.items)

# ----------------------------------------------------------------------

def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1
    
def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    # Your code here.
    yield 0
    
    for i in ints(1):
        yield i
        yield -i