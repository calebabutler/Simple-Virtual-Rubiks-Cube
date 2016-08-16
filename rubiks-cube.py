
class Cube:

    o_cycles = {
        'edge': (1, 0),
        'corner-c': (1, 2, 0),
        'corner-cc': (2, 0, 1),
    }

    def __init__(self,
                 scramble = None,
                 edges = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0],
                          [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0]],
                 corners = [[0, 0], [1, 0], [2, 0], [3, 0],
                            [4, 0], [5, 0], [6, 0], [7, 0]]):
        self.edges = edges
        self.corners = corners
        if scramble is not None:
            self.algorithm(scramble)

    def cycle_four_ins(self, array, four_ins, cycle_function):
        const_array = [None, None, None, None]
        for i, index in enumerate(four_ins):
            const_array[i] = array[index]
        for i, index in enumerate(four_ins):
            cycle = cycle_function(i)
            while cycle > 3:
                cycle -= 4
            while cycle < 0:
                cycle += 4
            array[index] = const_array[cycle]

    def gen_basic_turn(self, edge_pos, corner_pos, turn_type):
        if turn_type == 'c':
            self.cycle_four_ins(self.edges, edge_pos, lambda x: x - 1)
            self.cycle_four_ins(self.corners, corner_pos, lambda x: x - 1)
        elif turn_type == 'cc':
            self.cycle_four_ins(self.edges, edge_pos, lambda x: x + 1)
            self.cycle_four_ins(self.corners, corner_pos, lambda x: x + 1)
        elif turn_type == 'h':
            self.cycle_four_ins(self.edges, edge_pos, lambda x: x + 2)
            self.cycle_four_ins(self.corners, corner_pos, lambda x: x + 2)

    def gen_o_turn(self, edge_pos, corner_pos, turn_type, edge_o, corner_o):
        if edge_o == True:
            for pos in edge_pos:
                if self.edges[pos] is not None:
                    self.edges[pos][1] = (self.o_cycles['edge']
                      [self.edges[pos][1]])
        if corner_o == True:
            for pos_index, pos in enumerate(corner_pos):
                if self.edges[pos] is not None:
                    if pos_index == 0 or pos_index == 2:
                        self.corners[pos][1] = (self.o_cycles['corner-c']
                          [self.corners[pos][1]])
                    elif pos_index == 1 or pos_index == 3:
                        self.corners[pos][1] = (self.o_cycles['corner-cc']
                          [self.corners[pos][1]])
        self.gen_basic_turn(edge_pos, corner_pos, turn_type)

    def face_turn(self, turn):
        self.gen_o_turn(*{
            'U'  : ((0, 1, 2, 3), (0, 1, 2, 3), 'c', False, False),
            'U\'': ((0, 1, 2, 3), (0, 1, 2, 3), 'cc', False, False),
            'U2' : ((0, 1, 2, 3), (0, 1, 2, 3), 'h', False, False),
            'D'  : ((8, 9, 10, 11), (4, 5, 6, 7), 'c', False, False),
            'D\'': ((8, 9, 10, 11), (4, 5, 6, 7), 'cc', False, False),
            'D2' : ((8, 9, 10, 11), (4, 5, 6, 7), 'h', False, False),
            'R'  : ((1, 6, 9, 5), (2, 1, 6, 5), 'c', False, True),
            'R\'': ((1, 6, 9, 5), (2, 1, 6, 5), 'cc', False, True),
            'R2' : ((1, 6, 9, 5), (2, 1, 6, 5), 'h', False, False),
            'L'  : ((3, 4, 11, 7), (0, 3, 4, 7), 'c', False, True),
            'L\'': ((3, 4, 11, 7), (0, 3, 4, 7), 'cc', False, True),
            'L2' : ((3, 4, 11, 7), (0, 3, 4, 7), 'h', False, False),
            'F'  : ((2, 5, 8, 4), (3, 2, 5, 4), 'c', True, True),
            'F\'': ((2, 5, 8, 4), (3, 2, 5, 4), 'cc', True, True),
            'F2' : ((2, 5, 8, 4), (3, 2, 5, 4), 'h', False, False),
            'B'  : ((0, 7, 10, 6), (1, 0, 7, 6), 'c', True, True),
            'B\'': ((0, 7, 10, 6), (1, 0, 7, 6), 'cc', True, True),
            'B2' : ((0, 7, 10, 6), (1, 0, 7, 6), 'h', False, False),
        }[turn])

    def algorithm(self, alg):
        for turn in alg.split():
            self.face_turn(turn)

def main():
    cube = Cube('B F2 D B2 U2 F2 U2 F2 R2 D\' F2 R2 F R2 U\' B2 D\' R D U B')
    while (1):
        print(cube.edges)
        print(cube.corners)
        moves = input('> ')
        cube.algorithm(moves)

if __name__ == '__main__':
    main()
