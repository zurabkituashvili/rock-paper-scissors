import sys
import random
from moves_table import MovesTable
from rules import Rules
from hmac_generation import HMACGenerator

class Game:
    def __init__(self, moves):
        self.moves = moves
        self.rules = Rules()
        self.moves_table = MovesTable()
        self.hmac_generator = HMACGenerator()

    def run(self):
        valid_moves = self.moves
        self.rules.validate_moves(valid_moves)
        self.rules.print_valid(valid_moves)
        
        while True:
            key = self.hmac_generator.generate_key()
            print(f"HMAC: {key}")
            print("Available moves:")
            for i, move in enumerate(valid_moves, start=1):
                print(f"{i} - {move}")
            print("0 - Exit")
            print("? - Help")
            player_move = input("Enter your move: ")
            self.rules.exit(player_move)
            if player_move == '?':
                self.moves_table.print_table(valid_moves)
                continue
            player_move = self.rules.valid_input(player_move, valid_moves)
            player_move_str = valid_moves[int(player_move) - 1]
            computer_move_str = random.choice(valid_moves)
            hmac_digest = self.hmac_generator.compute_hmac(key, computer_move_str)
            print(f"Your move: {player_move_str}")
            print(f"Computer move: {computer_move_str}")
            self.rules.game_rules(hmac_digest, valid_moves, player_move_str, computer_move_str)
            print(f"HMAC key: {hmac_digest}\n")

if __name__ == "__main__":
    moves = sys.argv[1:]
    game = Game(moves)
    game.run()
