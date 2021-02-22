import input
import solver
import output


INPUT_DIR = "inputs"
OUTPUT_DIR = "outputs"

DATASET = "a_sample"
DATASET_FILE = f"{INPUT_DIR}/{DATASET}"

OUTPUT_FILE = f"{OUTPUT_DIR}/output_{DATASET}"


def run():
    nr_dict, pizzas = input.read_input(DATASET_FILE)
    deliveries = solver.solve(nr_dict, pizzas)
    output.create_output_file(OUTPUT_FILE, deliveries)


if __name__ == "__main__":
num_run()
