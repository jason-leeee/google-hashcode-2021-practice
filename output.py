
def create_output_file(filepath, deliveries):
    """
    Args:
        deliveries: a list of tuples: (number of people, list of pizza ids)
    """
    num_pizzas = len(deliveries)

    output_lines = [str(num_pizzas) + "\n"]
    for num_people, pizzas in deliveries:
        line = str(num_people) + " " + " ".join(list(map(str, pizzas))) + "\n"
        output_lines.append(line)
    
    with open(f"{filepath}", "w") as fwrite:
        fwrite.writelines(output_lines)


def test():
    deliveries = [
        (2, [1, 4]),
        (3, [0, 2, 3]),
    ]
    create_output_file("outputs/sample.txt", deliveries)


if __name__ == "__main__":
    test()
