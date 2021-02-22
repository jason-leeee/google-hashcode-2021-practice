import math

def validate(nr_dict, deliveries, pizzas):
    """
    This piece of code validates the solution and also returns the score
    of the current solution. If it does not meet the requirements the
    score will be -1.
        nr_dict: The amount of teams participating
        deliveries: a list of tuples: (number of people, list of pizza ids)
        pizzas: a dictionary of pizza ids and and a list of its ingredients
    """
    # each pizza must be part of at most one order
    encountered_pizza = set()
    for delivery in deliveries:
        for pizza in delivery[1]:
            if pizza != encountered_pizza:
                encountered_pizza.add(pizza)
            else:
                return -1

    # For all the teams or everybody gets a pizza or nobody in that team.
    for delivery in deliveries:
        if not (delivery[0] == len(delivery[1]) or len(delivery[1]) == 0) :
            return -1

    # The are no more deliveries than the amount of teams.
    # TODO: check if input also contains the first line
    if len(deliveries) > (nr_dict['t2'] + nr_dict['t3'] + nr_dict['t4']):
        return -1

    # the delivery score is the square of the total number of different ingredients of
    # all the pizzas in the delivery. The total score is the sum of the scores for all deliveries.
    score = 0
    
    for delivery in deliveries:
        ingredient_set = set()
        for pizza in delivery[1]:
            ingredient_set |= set(pizzas[pizza])
        score += len(ingredient_set) ** 2

    return score


class Validation:
    def __init__(self, nr_dict, pizzas):
        self.nr_dict = nr_dict
        self.pizzas = pizzas

    def validate(self, deliveries_bool):
        # Transform from the GA input to the actual problem statement
        deliveries = []
        for i in range(self.nr_dict['t2']):
            deliveries.append(('2', []))
        for i in range(self.nr_dict['t3']):
            deliveries.append(('3', []))
        for i in range(self.nr_dict['t4']):
            deliveries.append(('4', []))
        
        nr_groups = self.nr_dict['t2'] + self.nr_dict['t3'] + self.nr_dict['t4']
        for index, elem in enumerate(deliveries_bool):
           group_id = index % nr_groups
           pizza_id = math.floor(index / len(self.pizzas))
           if elem:
               deliveries[group_id][1].append(pizza_id)    
        score = validate(self.nr_dict, deliveries, self.pizzas)
        if score > 0:
            print(score)
        return score

# if __name__ == "__main__":
    