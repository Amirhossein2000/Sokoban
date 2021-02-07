from copy import deepcopy
import utils
import board


def search(b: board):
    stack = []
    stack.append(b)
    explored = set()

    while True:
        if len(stack) == 0:
            print(-1, len(explored))
            return
        else:
            current_node = stack.pop()
            moves = current_node.getPossibleMoves()
            current_node.fboxes = frozenset(current_node.boxes)
            explored.add(hash(current_node))

            for move in moves:
                child = deepcopy(current_node)
                child.move(move)
                if hash(child) not in explored:
                    if child.is_win():
                        utils.print_output(child.path, len(explored), child.box_moves, "DFS")
                        return
                    stack.append(child)
