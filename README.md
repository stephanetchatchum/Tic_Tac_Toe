# Tic Tac Toe — CLI Version 🎮

A two-player Tic Tac Toe game that runs in the terminal, built in Python.

## How to Play

Run the game:
```bash
python Tic_Tac_Toe.py
```

A reference board will show the position numbers at the start of each turn:
```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

Each player types a number (1–9) to place their mark on the board.

- **Player 1** plays ✖️
- **Player 2** plays ⭕

The game ends when a player wins or all cells are filled (draw).

## Win Conditions

A player wins by filling:
- Any full row
- Any full column
- Any diagonal

## Features

- 2-player mode
- Invalid move detection (can't play on a taken cell)
- Win detection for rows, columns, and both diagonals
- Draw detection

## What I Learned Building This

- Representing a grid as a 2D list in Python
- Using `divmod()` to convert a 1–9 input into `(row, col)`
- Game loops with turn switching using `player % 2`
- Nested loops for checking win conditions and counting empty cells

## Coming Soon

- Tkinter GUI version
- vs Computer mode