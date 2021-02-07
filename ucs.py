from copy import deepcopy
import utils
import board


def search(b: board):
    board_list = [b]
    explored = set()
    while True:
        if len(board_list) == 0:
            print(-1, len(explored))
            return
        else:
            board_list.sort(key=lambda b: len(b.path))
            current_node = board_list[0]
            del board_list[0]

            moves = current_node.getPossibleMoves()
            current_node.fboxes = frozenset(current_node.boxes)
            explored.add(hash(current_node))

            for move in moves:
                child = deepcopy(current_node)
                child.move(move)
                if hash(child) not in explored:
                    if child.is_win():
                        utils.print_output(child.path, len(explored), child.box_moves, "UCS")
                        return
                    board_list.append(child)
