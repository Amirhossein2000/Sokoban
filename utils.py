import board


def getBoard():
    strInput = input().split(" ")
    row_len = int(strInput[0])
    col_len = int(strInput[1])
    b = board.Board(col_len - 1, row_len - 1)

    for n in range(0, row_len):
        strInput = input()
        for m, item in enumerate(strInput):
            if item == "X":
                b.goals.add((m, n))
            if item == "#":
                b.walls.add((m, n))
            elif item == "@":
                b.boxes.add((m, n))
            elif item == "S":
                b.robot = (m, n)

    return b


def print_output(path, nodes_generated, box_moves, algorithm_name):
    print(f"Solved by {algorithm_name} algorithm")
    print(len(path), box_moves, nodes_generated)
    print(path)
