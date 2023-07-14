MTA_FARE = 2.90

def subway_fare(number_of_swipes):
    """This function takes the number of times a person has used the MTA subway system
    and provides a dollar value of how much money this person has spent given the number of rides
    they took that week (using the MTA values/new policy from 2023)
    >>> subway_fare(13)
    'You spent $37.70 this week'
    >>> subway_fare(14)
    'You spent $37.70 this week'
    >>> subway_fare(10)
    'You spent $29.00 this week'
    """
    if number_of_swipes >= 13:
        return f"You spent ${MTA_FARE*13:.2f} this week"
    return f"You spent ${number_of_swipes*MTA_FARE:.2f} this week"

print(subway_fare(int(input("How many times did you swipe your card to use the MTA this week? "))))