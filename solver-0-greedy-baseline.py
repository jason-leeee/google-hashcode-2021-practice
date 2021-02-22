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
    pizza_info = sorted(pizza_info, key=lambda t: t[1])   # sort by num_ings (t[1])
    pizza_info = np.array(pizza_info)
    
    deliveries = []
    idx = 0

    for n_people in [4, 3, 2]:
        for _ in range(nr_dict[f"t{n_people}"]):
            # there's not enough pizzas left for this team
            if idx + n_people >= nr_dict["pizzas"]:
                break

            deliveries.append((n_people, pizza_info[idx:idx + n_people, 0].tolist())) 
            idx += n_people

    return deliveries
