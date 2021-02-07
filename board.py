import copy


class Board:
    def __init__(self, x, y):
        self.possibleMoves = []
        self.boxes = set()
        self.walls = set()
        self.goals = set()
        self.robot = ()
        self.max_x = x
        self.max_y = y
        self.path = ""
        self.fboxes = frozenset()
        self.box_moves = 0

    def __hash__(self):
        ''' hashes by frozenset of box positions '''
        h = hash((self.fboxes, self.robot))
        return h

    def getPossibleMoves(self):
        self.possibleMoves.clear()
        self.scanAll()
        return self.possibleMoves

    def scanAll(self):
        x = self.robot[0]
        y = self.robot[1]

        if x < self.max_x:
            self.scan("R", x + 1, y)
        if x > 0:
            self.scan("L", x - 1, y)
        if y > 0:
            self.scan("U", x, y - 1)
        if y < self.max_y:
            self.scan("D", x, y + 1)

    def scan(self, direction, x, y):
        if (x, y) in self.walls:
            return
        elif (x, y) not in self.boxes:
            self.possibleMoves.append([(x, y), direction])
            return
        elif direction == "L" and x > 0:
            self.boxMovePossible((x, y), (x - 1, y), direction)
        elif direction == "R" and x < self.max_x:
            self.boxMovePossible((x, y), (x + 1, y), direction)
        elif direction == "U" and y > 0:
            self.boxMovePossible((x, y), (x, y - 1), direction)
        elif direction == "D" and y < self.max_y:
            self.boxMovePossible((x, y), (x, y + 1), direction)

    def boxMovePossible(self, src, dst, direction):
        if dst not in self.walls and dst not in self.boxes:
            self.possibleMoves.append([
                src, dst, direction
            ])

    def move(self, m: list):
        # m conditions --> [(a,b)] or [(a,b), (c,d)]
        self.robot = m[0]
        self.path += m.pop()
        if len(m) == 2:
            self.box_moves += 1
            self.boxes.remove(m[0])
            self.boxes.add(m[1])

    def is_win(self):
        if self.goals.issubset(self.boxes):
            return True
        else:
            return False
