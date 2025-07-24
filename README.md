# Tic Tac Toe Game

This repository contains a Python implementation of a **Tic Tac Toe** game. The game is designed to be played in the terminal and supports two players taking turns.

## Features

- **Welcome Message**: Displays a welcome message at the start of the game.
- **Interactive Gameplay**: Players are prompted to enter their moves, and the game board updates dynamically.
- **Input Validation**: Ensures that moves are valid and that players cannot overwrite existing moves.
- **Win Detection**: Checks for winning conditions (rows, columns, diagonals) and announces the winner.
- **Tie Detection**: Detects when the game ends in a tie.
- **Replay Option**: Players can choose to play again after a game ends.
- **Score Tracking**: Keeps track of wins for both players across multiple games.

## How to Play

1. Run the `exercises.py` file using Python:
   ```bash
   python3 exercises.py
   ```
2. Follow the prompts to enter your moves. Use the format `A1`, `B2`, etc., to specify your move.
3. The game will announce the winner or a tie at the end of each round.
4. Choose whether to play again or exit the game.

## Future Stretch Goal

As a future enhancement, a **Connect 4** game has been scaffolded in the `connect4.py` file. This game will feature:

- A 6x6 grid.
- Gravity mechanics where pieces drop to the lowest available row in a column.
- Win detection for 4 consecutive pieces horizontally, vertically, or diagonally.
- Similar interactive gameplay and replay options.

Stay tuned for updates!

## Possible Improvements

If you wish to revisit and enhance the game in the future, here are some ideas:

1. **Enhanced User Experience**:
   - Allow players to choose custom symbols.
   - Add colors to the board and messages using libraries like `colorama`.

2. **AI Opponent**:
   - Implement a single-player mode with AI difficulty levels (easy, medium, hard).

3. **Game Modes**:
   - Add a "best of N" mode for competitive play.
   - Introduce a timed mode where players have limited time to make a move.

4. **Persistent Scores**:
   - Save scores to a file or database to track progress across sessions.

5. **Replay Feature**:
   - Save game moves and allow players to replay games step by step.

6. **Multiplayer Over Network**:
   - Enable two players to play over a network using sockets or a web interface.

7. **Graphical Interface**:
   - Build a GUI using:
     - **`tkinter`**: Simple and built into Python.
     - **`pygame`**: Great for interactive games with animations.
     - **`PyQt` or `PySide`**: For a polished and professional look.

These improvements can make the game more engaging and versatile for players.
