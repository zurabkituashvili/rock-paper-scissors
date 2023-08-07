from tabulate import tabulate

class MovesTable:
    def create_moves_table(self, moves):
        table_data = []
        header = ["v PC\\User >"] + moves
        for move1 in moves:
            row = [move1]
            for move2 in moves:
                if move1 == move2:
                    row.append("Draw")
                else:
                    idx1 = moves.index(move1)
                    idx2 = moves.index(move2)
                    if (idx1 - idx2) % len(moves) > len(moves) // 2:
                        row.append("Win")
                    else:
                        row.append("Lose")
            table_data.append(row)
        return tabulate(table_data, headers=header, tablefmt="grid")

    def print_table(self, moves):
        moves_table = self.create_moves_table(moves)
        print(moves_table)