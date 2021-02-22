
def create_output_file(fname, deliveries):
    """
    Args:
        deliveries: a list of tuples: (number of people, list of pizza ids)
    """
    num_pizzas = len(deliveries)

    output_lines = [str(len)]
    for num_people, pizzas in deliveries:
        line = str(num_people) + " " + " ".join(list(map(str, pizzas)))
        output_lines.append(line)
    
    with open(f"outputs/{fname}.txt", "w") as fwrite:
        fwrite.writelines(output_lines)


def test():
    deliveries = [
        (2, [1, 4]),
        (3, [0, 2, 3]),
    ]
    create_output_file("sample", deliveries)


if __name__ == "__main__":
    test()
