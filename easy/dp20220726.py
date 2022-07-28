# ---------------------------------------
# [Easy]
# This problem was asked by Facebook.
# Given a list of integers, return the largest product that can be made by multiplying any three integers.
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
# You can assume the list has at least three integers.
# ---------------------------------------

def fn(l):
    """
    Parameters:
    -----------
    l:int list

    Solution:
    ---------

    Using asumption of you can get it by:
    1. product of bigger two negatives times the bigger positive number
    2. product of 3 biggers positives numbers

    Return:
    -------
    Largest product get it by 3 elements

    """

    print("input:",l)
    if len(l)>=3:
        l.sort()
        s1 = l[:2]
        s1.append(l[-1])
        print("s1:",s1)

        s2 = l[-3:]
        print("s2:",s2)

        r1=1
        for i in s1:
            r1=r1*i

        r2=1
        for i in s2:
            r2=r2*i
        
        return max(r1,r2)
    else:
        return None

print(fn([-10, -10, 5, 2]))
print(fn([-10, 1, 2, 2, 100]))
print(fn([-1, -1, 2, 2, 100]))
print(fn([1, 1, 1]))
print(fn([1, 1]))