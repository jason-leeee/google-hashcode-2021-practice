import input
import solver
import output


INPUT_DIR = "inputs"
OUTPUT_DIR = "outputs"

DATASET = "a_example"
DATASET_FILE = f"{INPUT_DIR}/{DATASET}"

OUTPUT_FILE = f"{OUTPUT_DIR}/output_{DATASET}.txt"


DATASET_ALL = [
    "a_example",
    "b_little_bit_of_everything.in",
    "c_many_ingredients.in",
    "d_many_pizzas.in",
    "e_many_teams.in"
]
    

def run(input_path, output_path):
    nr_dict, pizzas = input.read_input(input_path)
    deliveries = solver.solve(nr_dict, pizzas)
    output.create_output_file(output_path, deliveries)


def run_all():
    for dset in DATASET_ALL:
        print(f"running {dset}...")
        input_path = f"{INPUT_DIR}/{dset}"
        output_path = f"{OUTPUT_DIR}/output_{dset}.txt"
        run(input_path, output_path)


if __name__ == "__main__":
    #run(DATASET_FILE, OUTPUT_FILE)
    run_all()
