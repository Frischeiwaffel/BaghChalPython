# BaghChalPython
Bagh Chal (Tiger Moving Game) is a strategic, two-player board game that originates in Nepal. This project deals with the implementation and its AI, impmented in Python using Qt for its GUI.


Rules:
At the start of the game all four tigers are placed on the four corners of the grid, facing the center. All goats start off the board.

The pieces must be put at the intersections of the board lines and moves follow these lines.

The player controlling the goats moves first by placing a goat onto a free intersection on the board. Then it is the tigers' turn. One tiger is then moved to an adjacent position along the lines that indicate the valid moves. Moves are alternate between players.

Tigers capture goats by jumping over them to an adjacent free position (as in checkers, although capturing is not obligatory in Bagh-Chal). Goats can not move until all 20 have been put on the board.

The tigers must move according to these rules:

They can move to an adjacent free position along the lines.
They can start capturing goats any moment after the match has started.
They can capture only one goat at a time.
They can jump over a goat in any direction, but it must be to an adjacent intersection following any of the lines drawn on the board.
A tiger cannot jump over another tiger.
The goats must move according to these rules:

They can move to an adjacent position along the lines after all 20 have been put on the board.
They must leave the board when captured.
They can not jump over the tigers or other goats.
The tigers win once they have captured five goats. Goats try to avoid being captured (jumped over) and they win by blocking the tigers' moves till they are unable to move.

Sometimes the game can fall into a repetitive cycle of positions. Goats especially may use this resort to defend themselves against being captured. To avoid this situation, an additional rule has been established: when all the goats have been placed, no move may return the board to a situation that has already occurred during the game.

From https://en.wikipedia.org/wiki/Bagh-Chal 
