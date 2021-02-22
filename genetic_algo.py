from geneticalgorithm import geneticalgorithm as ga
from validate import Validation

def genetic_algo(nr_dict, pizzas):
    """
    The matrix representing the solution of this problem is 
    on the column the pizza_id and on the row the group_id.
    If an entry = true then that pizza_id will get delivered 
    to that group_id. 
    """

    val = Validation(nr_dict, pizzas)
    dimensions = (nr_dict['t2'] + nr_dict['t3'] + nr_dict['t4']) * len(pizzas)
    print(dimensions)
    model=ga(function=val.validate,dimension=dimensions,variable_type='bool')
    
    model.run()

if __name__ == "__main__":
    nr_dict = {'pizzas': 5, 't2': 1, 't3': 2, 't4': 1}
    pizzas = [(3, {'pepper', 'olive', 'onion'}), (3, {'mushroom', 'basil', 'tomato'}), (3, {'mushroom', 'chicken', 'pepper'}), (3, {'tomato', 'mushroom', 'basil'}), (2, {'chicken', 'basil'})]
    genetic_algo(nr_dict, pizzas)
