import numpy as np
import random

from helper import get_distance, get_distance_2


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

    idlist = [i for i in range(len(pizzas))]
    idhash = {i: True for i in range(len(pizzas))}

    MAX_VALIDS = 10

    print("get_distance")
    distances = get_distance_2(nr_dict, pizzas)
    print("sorting")
    diffs = []
    for i in range(len(pizzas)):
        diffs.append(distances[i].argsort()[::-1])
    diffs = np.array(diffs)
    
    deliveries = []
    idx = 0

    for n_people in [4, 3, 2]:
        for iteration in range(nr_dict[f"t{n_people}"]):
            print(f"iteration: {iteration}")

            # there's not enough pizzas left for this team
            if idx + n_people >= nr_dict["pizzas"]:
                break

            pid_prev = random.choice(list(idhash.keys()))
            del idhash[pid_prev]
            pids = {pid_prev: True}
            while len(pids) < n_people:
                #print(f"pids: {pids}")
                maxpid = None
                maxdist = -1
                valids = 0
                for pid in diffs[pid_prev]:
                    if pid in idhash and distances[pid_prev, pid] > maxdist and pid not in pids:
                        maxpid = pid
                        maxdist = distances[pid_prev, pid]
                        valids += 1
                        if valids == MAX_VALIDS:
                            break

                #print(f"maxpid: {maxpid}")
                pids[maxpid] = True
                del idhash[maxpid]
                pid_prev = maxpid
                
            deliveries.append((n_people, list(pids.keys()))) 
            idx += n_people

    return deliveries
