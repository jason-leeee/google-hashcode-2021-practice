
def validate(input, deliveries):
    """
    This piece of code validates the solution and also returns the score
    of the current solution. If it does not meet the requirements the
    score will be -1.
        deliveries: a list of tuples: (number of people, list of pizza ids)
    """
    # At least one of every pizza should be delivered.
    pizzas_delivered = set()
    for delivery in deliveries:
        # Union the sets
        pizzas_delivered |= set(delivery[1])
    
    #TODO: check if input also contains the first line
    if len(pizzas_delivered) < len(input):
        return -1

    # For all the teams or everybody gets a pizza or nobody in that team.
    for delivery in deliveries:
        if delivery[0] != len(delivery[1]):
            return -1

    # The are no more deliveries than the amount of teams.
    # TODO: check if input also contains the first line
    if len(deliveries) != len(input):
        return -1

    # the delivery score is the square of the total number of different ingredients of
    # all the pizzas in the delivery. The total score is the sum of the scores for all deliveries.
    score = 0
    for delivery in deliveries:
        
        

    return 


if __main__():
    validate()
