import sys
class Rules:
    def calculate_winner(self, moves, player_move_str, computer_move_str):
        player_idx = moves.index(player_move_str)
        computer_idx = moves.index(computer_move_str)
        if (player_idx - computer_idx) % len(moves) > len(moves) // 2:
            return 1
        elif player_idx != computer_idx:
            return -1
        else:
            return 0

    def game_rules(self, hmac_digest, moves, player_move_str, computer_move_str):
        if hmac_digest:
            winner = self.calculate_winner(moves, player_move_str, computer_move_str)
            if winner == 1:
                print("You win!")
            elif winner == -1:
                print("Computer wins!")
            else:
                print("It's a tie!")

    def validate_moves(self, moves):
        if len(moves) < 3 or len(moves) % 2 == 0:
            return False
        if len(moves) != len(set(moves)):
            return False
        return True

    def print_valid(self, moves):
        if not self.validate_moves(moves):
            print("Error: The provided moves are incorrect.")
            print("Make sure you provide an odd number of non-repeating strings.")
            sys.exit(1)

    def exit(self, player_move):
        if player_move == '0':
            print("Exiting the game.")
            sys.exit(0)            

    def valid_input(self, player_move, moves):
        while not player_move.isdigit() or int(player_move) not in range(1, len(moves) + 1):
            print("Invalid input! Please choose from the menu.")
            player_move = input("Enter your move: ")
            self.exit(player_move)
        return player_move