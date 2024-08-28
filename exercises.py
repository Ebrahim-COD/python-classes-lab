class Game():
    def __init__(self, turn = "X", tie = False, winner = None):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
        

    def play_game(self, move = None): 
        print("Welcome to Tic Tac Toe Game!")
        while True:
            self.render()
            move = input("Enter your position: ").lower()
            if move not in self.board:
                print("Invalid move! Try again.")
                continue
            if self.board[move]:
                print("Position already taken! Try again.")
                continue
            self.board[move] = self.turn
            if self.turn == "X":
                self.turn = "O"
            else:
                self.turn = "X"
            self.winner = self.check_winner()
            if self.winner:
                self.render()
                break
            self.tie = self.check_tie()
            if self.tie:
                self.render()
                break             
        
    
    def print_board(self):
        b = self.board
        print(f"""
        A   B   C
    1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
    2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
    3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """) 
    
    def print_message(self):
        if self.tie:
            print("Tie Game!")
        elif self.winner:
            print(f"Player {self.winner} wins the game!")
        else:
            print(f"It's players {self.turn} turn!")
    
    def render(self):
        self.print_board()
        self.print_message()
    
    def check_winner(self):
        if self.board['a1'] and (self.board['a1'] == self.board['a2'] == self.board['a3']):
            return self.board['a1']
        if self.board['b1'] and (self.board['b1'] == self.board['b2'] == self.board['b3']):
            return self.board['b1']
        if self.board['c1'] and (self.board['c1'] == self.board['c2'] == self.board['c3']):
            return self.board['c1']
        if self.board['a1'] and (self.board['a1'] == self.board['b2'] == self.board['c3']):
            return self.board['a1']
        if self.board['c1'] and (self.board['c1'] == self.board['b2'] == self.board['a3']):
            return self.board['c1']
        if self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1']):
            return self.board['a1']
        if self.board['a2'] and (self.board['a2'] == self.board['b2'] == self.board['c2']):
            return self.board['a2']
        if self.board['a3'] and (self.board['a3'] == self.board['b3'] == self.board['c3']):
            return self.board['a3']
    
    def check_tie(self):
        if all(self.board.values()):
            return True
        else:
            return False

game_instance = Game()
game_instance.play_game()
