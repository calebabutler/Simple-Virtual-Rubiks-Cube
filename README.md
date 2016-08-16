# Simple-Virtual-Rubiks-Cube

Needs python to run. https://www.python.org/

To understand the output of this program, the first array gives you information on the edges and the second on the corners. Here's an example output of a solved cube.

    [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0]]
    [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]

So here we can see that the edges and corners start at 0. Also that every position is stored with a second number, the orientation of that piece. A 0 is for correct, a 1 for clockwise and a 2 for counter-clockwise.

    ============
    - C0 E0 C1 -
    - E3 WC E1 -
    - C3 E2 C2 -
    ============
    ============ =============
    - C3 E2 C2 - - C1 E0  C0 -
    - E4 GC E5 - - E6 BC  E7 -
    - C4 E8 C5 - - C7 E10 C6 -
    ============ =============
    ==============
    - C4  E8  C5 -
    - E11 YC  E9 -
    - C7  E10 C6 -
    ==============

Hopefully from this you can get an idea of how all the edges are placed on the cube. You can only do face turns and only on the white green orientation. In the input you put in these face turns or full algorithms. Good luck!
