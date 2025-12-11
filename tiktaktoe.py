# Tic-Tac-Toe Game

# Function to print the game board
def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print("\n")

# Function to check if there is a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    return all([board[i][j] != " " for i in range(3) for j in range(3)])

# Main game function
def play_game():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    # Game loop
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        # Get the player's move
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            
            # Check if the move is valid
            if board[row][col] != " ":
                print("This spot is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column values between 0 and 2.")
            continue

        # Place the move on the board
        board[row][col] = current_player
        
        # Check if the current player won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the board is full (tie game)
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
