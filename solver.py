import numpy as np


def solve(nr_dict, pizzas):
    """
    Args:
        nr_dict:
            'pizzas'
            't2'
            't3'
            't4'
        pizzas: a list of tuples: (number of ingredients, a list of ingredient names)

    Returns:
        deliveries: a list of tuples: (number of people, list of pizza ids)
    """

    ids = [i for i in range(len(pizzas))]
    num_ings = [num_ingredients for num_ingredients, _ in pizzas]
    
    pizza_info = zip(ids, num_ings)
    pizza_info = sorted(pizza_info, key=lambda id, n: n)
    pizza_info = np.array(pizza_info)
    
    deliveries = []
    idx = 0

    for team in [4, 3, 2]:
        for _ in nr_dict[f"t{team}"]:
            delivery = 

            idx += team

    


    return deliveries
