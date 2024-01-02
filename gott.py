def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("--" * 6)

def my_function(player, symbol_selected):
    symbol = input(f"{player}, only enter symbol X/O: ").upper()
    while symbol != symbol_selected:
        print(f"Invalid input. Please enter '{symbol_selected}'.")
        symbol = input(f"{player}, only enter symbol X/O: ").upper()
    return symbol

def check_winner(board, player_1, player_2):
    # Check rows
    for row in board:
        if all(cell == row[0] and cell != ' ' for cell in row):
            return player_1 if row[0] == 'X' else player_2

    # Check columns
    for col in range(3):
        if all(board[row][col] == board[0][col] and board[row][col] != ' ' for row in range(3)):
            return player_1 if board[0][col] == 'X' else player_2

    # Check diagonals
    if all(board[i][i] == board[0][0] and board[i][i] != ' ' for i in range(3)) or \
       all(board[i][2 - i] == board[0][2] and board[i][2 - i] != ' ' for i in range(3)):
        return player_1 if board[0][0] == 'X' else player_2

    return None

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def G_O_T_T():
    while True:
        print("""Select option for Game
                 S. Start 
                 E. Exit""")
        option = input("Enter option (S/E): ").upper()

        if option == 'E':
            print("Exiting the Game.")
            break
        elif option == 'S':
            player_1 = input("Enter Player_1 Name: ")
            player_1_choice = my_function(player_1, 'X')
            
            # Automatically assign the remaining symbol to Player 2
            player_2 = input("Enter Player_2 Name: ")
            if player_1_choice == 'X':
                player_2_choice = 'O'
            else:
                player_2_choice = 'X'
            
            board = [[' ' for _ in range(3)] for _ in range(3)]
            player = player_1_choice

            while True:
                print_board(board)
                try:
                    move = int(input(f"{player}, enter your move (1-9): ")) - 1
                    if not 0 <= move <= 8:
                        print("Invalid input. Please enter a number between 1 and 9.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                row, col = move // 3, move % 3

                if board[row][col] == ' ':
                    board[row][col] = player
                    winner = check_winner(board, player_1, player_2)
                    if winner:
                        print_board(board)
                        print(f"{winner} wins!")
                        break
                    elif is_board_full(board):
                        print_board(board)
                        print("It's a tie!")
                        break
                    else:
                        player = player_2_choice if player == player_1_choice else player_1_choice
                else:
                    print("Cell already occupied or invalid move. Try again.")

            play_again = input("Do you want to play again? (Y/N): ").upper()
            if play_again != 'Y':
                print("Exiting the Game.")
                break

if __name__ == "__main__":
    G_O_T_T()
