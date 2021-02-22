from itertools import chain
import numpy as np
from scipy.spatial.distance import cdist

def get_distance(nr_dict, pizzas, metric='cityblock'):
    """"
    info on cdist supported distances:
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cdist.html
    """

    pizzas = list(enumerate(pizzas))

    ids = [elm[0] for elm in pizzas]
    num_ings = [elm[1][0] for elm in pizzas]
    ings_list = [elm[1][1] for elm in pizzas]

    ings_unique = list(set(chain.from_iterable(ings_list)))
    ings_ids = range(len(ings_unique))

    ings_map = dict(zip(ings_unique, ings_ids))

    encoding = np.zeros((len(pizzas), len(ings_unique)), dtype=np.bool)
    for i, ings in enumerate(ings_list):
        indices = list(map(lambda ing: ings_map[ing], ings))
        encoding[i, indices] = len(indices) * [1]

    out = cdist(encoding, encoding, metric=metric)

    return out

from itertools import chain

def get_encoding(pizzas):

    nr_ings, ings_list = zip(*pizzas)


    ings_unique = list(set(chain.from_iterable(ings_list)))
    ings_ids = range(len(ings_unique))

    ings_map = dict(zip(ings_unique, ings_ids))

    encoding = np.zeros((len(pizzas), len(ings_unique)), dtype=np.bool)
    for i, ings in enumerate(ings_list):
        indices = list(map(lambda ing: ings_map[ing], ings))
        encoding[i, indices] = len(indices) * [1]

    print('encoding success')

    return encoding
