import sys
import bfs
import dfs
import ucs
import Iterative_Deepening
import utils

algorithm = sys.argv[1]
if algorithm == "1":
    bfs.search(utils.getBoard())
elif algorithm == "2":
    dfs.search(utils.getBoard())
elif algorithm == "3":
    Iterative_Deepening.search(utils.getBoard())
elif algorithm == "5":
    ucs.search(utils.getBoard())
elif algorithm == "all":
    b = utils.getBoard()
    dfs.search(b)
    Iterative_Deepening.search(b)

    bfs.search(b)
    ucs.search(b)
else:
    print("Not Implemented")
