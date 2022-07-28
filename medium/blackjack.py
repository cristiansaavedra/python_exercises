# ---------------------------------------
# [Medium]
# This problem was in Kaggle Course
# We wanted to create a represent hands in blackjack.
# ---------------------------------------

#Solution:

def hand(hand):
    out = []
    num_aces = 0
    for x in hand:
        if (x.isdigit()):
            out.append(int(x))
        elif x == 'A':
            out.append(1)
            num_aces += 1
        else:
            out.append(10)

    total = sum(out)

    while num_aces>0 and total+10 <= 21:
        total += 10
        num_aces -= 1
        
    return total

def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    h1 = hand(hand_1)
    h2 = hand(hand_2)

    if h1 > 21:
        return False
    elif h1 > h2 or h2 > 21:
        return True

#print(blackjack_hand_greater_than(['A', 'A', '9'],['A', 'A', '9', '3']))
print(blackjack_hand_greater_than(['K'], ['3', '4']))
print(blackjack_hand_greater_than(['K'], ['10']))
print(blackjack_hand_greater_than(['K', 'K', '2'], ['3']))