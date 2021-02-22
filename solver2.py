import numpy as np
from scipy.spatial.distance import cdist

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

    print(nr_dict)

    pizzas = list(enumerate(pizzas))
    pizzas = sorted(pizzas, key=lambda x: -x[1][0])

    from helper import get_encoding

    encoding = get_encoding([elm[1] for elm in pizzas])

    from sklearn.neighbors import NearestNeighbors

    nbrs = NearestNeighbors(n_neighbors=min(max(int(len(pizzas)/10), 2), 500),
                            algorithm='kd_tree',
                            leaf_size=min(max(int(len(pizzas)/10), 2), 500)).fit(encoding)
    print('knn fitted')


    taken = np.zeros(len(pizzas), dtype=np.bool)
    def team_deliveries(team_size, nr_teams):
        deliveries = []
        for _ in range(nr_teams):
            neighbors = []
            t4_pizzas = []
            for i, (ids, pizza) in enumerate(pizzas):
                if taken[i]:
                    continue
                if len(t4_pizzas) == 0:
                    t4_pizzas.append(ids)
                    taken[i] = True
                    extended = False
                else:
                    if not extended:
                        neighbors.extend(nbrs.kneighbors([encoding[i,:]], return_distance=False)[0,:].tolist())

                    if i in neighbors:
                        extended = True
                        continue
                    else:
                        t4_pizzas.append(ids)
                        taken[i] = True
                        extended = False

                        if len(t4_pizzas) == team_size:
                            break

            if len(t4_pizzas) == team_size:
                deliveries.append((team_size, t4_pizzas))

        return deliveries
    deliveries = []

    deliveries.extend(team_deliveries(4, nr_dict['t4']))
    deliveries.extend(team_deliveries(3, nr_dict['t3']))
    deliveries.extend(team_deliveries(2, nr_dict['t2']))

    return deliveries


