def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    
    card_dictionary = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    ranks = [r for r,s in cards]
    
    for index,r in enumerate(ranks):
        if r in card_dictionary.keys():
            ranks[index] = card_dictionary[r]
            
    ranks = [int(r) for r in ranks]
    
    ranks.sort(reverse=True)
    return ranks

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for rank in ranks:
        if ranks.count(rank) == n:
            return rank
    else:
        return None

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    
    first_pair = 0
    second_pair = 0
    
    for rank in ranks:
        if ranks.count(rank) == 2:
            if first_pair == 0:
                first_pair = rank
            elif rank != first_pair:
                second_pair = rank

    if first_pair != 0 and second_pair !=0:
        return (first_pair, second_pair)
    else:
        return None

def hand_rank(hand):
    """Return a value indicating the ranking of a hand."""
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    diff_between_cards = [ranks[i]-ranks[i-1] for i in range(1, len(ranks))]

    return (-1 in diff_between_cards and len(set(diff_between_cards)) == 1)
    
def flush(hand):
    "Return True if all the cards have the same suit."

    suits = [s for r,s in hand]
    
    return len(set(suits))==1 
    
# -----------
# User Instructions
# 
# Write a function, deal(numhands, n=5, deck), that 
# deals numhands hands with n cards each.
#

import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n=5, deck=mydeck):
    random.shuffle(deck)
    return [deck[hand:hand+n] for hand in range(0, n*numhands, n)]