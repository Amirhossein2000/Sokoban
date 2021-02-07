from copy import deepcopy
import utils
import board


def search(b: board):
    stack = []
    stack.append([b])
    explored = set()

    while True:
        if len(stack) == 0:
            print(-1, len(explored))
            return
        else:
            level_nodes = stack.pop()
            for current_node in level_nodes:
                moves = current_node.getPossibleMoves()
                current_node.fboxes = frozenset(current_node.boxes)
                explored.add(hash(current_node))

                deep_level = []

                for move in moves:
                    child = deepcopy(current_node)
                    child.move(move)
                    if hash(child) not in explored:
                        if child.is_win():
                            utils.print_output(child.path, len(explored), child.box_moves, "Iterative Deepening")
                            return
                        deep_level.append(child)

                stack.append(deep_level)
