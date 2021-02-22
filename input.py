from pathlib import Path

def read_input(filepath):
    with open(filepath, 'r') as f:
        nr_pizzas, nr_t2, nr_t3, nr_t4 = map(int, f.readline().strip().split(' '))
        nr_dict = {
            'pizzas': nr_pizzas,
            't2': nr_t2,
            't3': nr_t3,
            't4': nr_t4,
        }

        pizzas = []
        for line in f.readlines():
            line_list = line.strip().split(' ')
            nr_ingredients = int(line_list[0])
            ingredients = set(line_list[1:])
            pizzas.append((nr_ingredients, ingredients))

        return nr_dict, pizzas



if __name__ == "__main__":
    filename = "a_example"

    print(read_input(filename))
