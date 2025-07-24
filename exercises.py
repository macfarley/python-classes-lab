# As a user (AAU), I want to see a welcome message at the start of a game.
# AAU, before being prompted for a move, I want to see the board printed in the console to know what moves have been made.
# AAU, at the beginning of each turn, told whose turn it is: It's player X's turn!
# AAU, I should be prompted to enter a move and be provided an example of valid input ('Enter a valid move (example: A1)').
# AAU, I want to be able to enter my move's column letter in upper or lower case (a/A, b/B, or c/C) to make it easier to enter my move.
# AAU, if I enter a move in an invalid format or try to occupy a cell already taken, I want to see a message chastising me and be re-prompted.
# AAU, after entering a move, I should once again be presented with the updated game board, notified of the current turn, and asked to enter a move for the other player. This process should continue until there is a winner or a tie
# AAU, I should see a message at the end of the game indicating the winner or stating that the game ended in a tie.


class Game:
    def __init__(self):
        # Initialize the game state
        # self.current_turn: Tracks whose turn it is ('X' or 'O')
        # self.board_state: Represents the current state of the board as a dictionary
        self.current_turn = "X"
        self.board_state = self.board()
        self.wins = {"X": 0, "O": 0}  # Track wins for each player

    def welcome_message(self):
        # AAU, I want to see a welcome message at the start of a game.
        print("Welcome to the Tic Tac Toe game!")

    def board(self):
        # Create and return the initial empty board as a dictionary
        # Keys represent positions (e.g., 'a1', 'b2') and values are None
        return {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def print_board(self):
        # AAU, before being prompted for a move, I want to see the board printed in the console to know what moves have been made.
        b = self.board_state
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def get_move(self):
        # AAU, I should be prompted to enter a move and be provided an example of valid input ('Enter a valid move (example: A1)').
        # AAU, I want to be able to enter my move's column letter in upper or lower case (a/A, b/B, or c/C) to make it easier to enter my move.
        # AAU, if I enter a move in an invalid format or try to occupy a cell already taken, I want to see a message chastising me and be re-prompted.
        while True:
            move = input(f"Enter a valid move (example: A1): ").lower()
            if move in self.board_state:
                if self.board_state[move] is None:
                    return move
                else:
                    print("Invalid move. Cell already taken.")
            else:
                print("Invalid move format.")

    def move(self):
        # AAU, after entering a move, I should once again be presented with the updated game board, notified of the current turn, and asked to enter a move for the other player.
        move = self.get_move()
        self.board_state[move] = self.current_turn
        self.print_board()

    def check_for_winner(self):
        # AAU, I should see a message at the end of the game indicating the winner or stating that the game ended in a tie.
        winning_combos = [
            # Rows
            ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],
            # Columns
            ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],
            # Diagonals
            ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']
        ]
        for combo in winning_combos:
            if (self.board_state[combo[0]] is not None and
                self.board_state[combo[0]] == self.board_state[combo[1]] == self.board_state[combo[2]]):
                print(f"{self.board_state[combo[0]]} wins the game!")
                self.wins[self.board_state[combo[0]]] += 1
                return True
        return False

    def check_for_tie(self):
        # AAU, I should see a message at the end of the game indicating the winner or stating that the game ended in a tie.
        all_positions_filled = all(value is not None for value in self.board_state.values())
        no_winner = not self.check_for_winner()
        if all_positions_filled and no_winner:
            print("Tie game!")
            return True
        return False

    def switch_turn(self):
        # AAU, at the beginning of each turn, told whose turn it is: It's player X's turn!
        self.current_turn = 'O' if self.current_turn == 'X' else 'X'
        print(f"It's {self.current_turn}'s turn!")

    def play_game(self):
        # AAU, after entering a move, I should once again be presented with the updated game board, notified of the current turn, and asked to enter a move for the other player.
        self.welcome_message()
        while True:
            self.print_board()
            self.move()
            if self.check_for_winner() or self.check_for_tie():
                break
            self.switch_turn()
        self.print_board()
        print(f"Score: X - {self.wins['X']}, O - {self.wins['O']}")

        # AAU, at the end of a game, I should be asked if I would like to play again.
        while True:
            play_again = input("Would you like to play again? (yes/no): ").strip().lower()
            if play_again in {'y', 'ye', 'yeah', 'yes', 'true', '1'}:
                # AAU, if I accept the offer to play again, the game should reset and begin again.
                self.board_state = self.board()
                self.play_game()
                break
            elif play_again in {'n', 'no', 'nah', 'false', '0'}:
                # AAU, if I decline the offer to play again, the program should stop running.
                print("Thanks for playing!")
                break
            else:
                print("Invalid input. Please enter yes or no.")

    def display_scores(self):
        # AAU, I would like the game to record wins and losses and display these records at the end of every game.
        print(f"Final Scores:\nPlayer X: {self.wins['X']}\nPlayer O: {self.wins['O']}")

if __name__ == "__main__":
    game = Game()
    game.play_game()

# If you wish to expand on the functionality of your game, try implementing the following user stories:

# AAU, at the end of a game, I should be asked if I would like to play again.
# AAU, if I accept the offer to play again, the game should reset and begin again.
# AAU, if I decline the offer to play again, the program should stop running.
# AAU, I would like the game to record wins and losses and display these records at the end of every game.