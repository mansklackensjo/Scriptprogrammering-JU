import os
from ConnectFour import ConnectFour

game = ConnectFour(7)

input("Start game by pressing enter...")

while game.get_winner() == " ":

    number_of_moves_made = len(game.moves)
    print(number_of_moves_made)
    # represents a turn
    game.print_game()
    print(f"Player {game.get_next_players_turn()}:s turn")

    col = input(f"In which column do you want to place your move? (0 - {game.number_of_columns - 1}): ")
    
    while col.isdigit() == False or game.does_column_exist(int(col)) == False:
        col = input(f"Invalid move. Enter a valid one: ")
    game.make_move(int(col))
        
        
    

    if number_of_moves_made > 7: # Kolla om columnen är full, säga till att göra ett annat drag
        pass
    


game.print_game()
print(f"Player {game.get_next_players_turn()} wins!!")