import input
import solver
import output


INPUT_DIR = "inputs"

DATASET = "a_sample"
DATASET_FILE = f"{INPUT_DIR}/{DATASET}"


def run():
    num_pizzas, num_teams_2, num_teams_3, num_teams_4, pizzas = input.get_inputs(DATASET_FILE)
    deliveries = solver.solve(num_pizzas, num_teams_2, num_teams_3, num_teams_4, pizzas)
    output.create_output_file("sample", deliveries)


if __name__ == "__main__":
num_run()
