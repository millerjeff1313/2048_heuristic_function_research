# simple 2048 game in python
import random
from pprint import pprint

class Game:
    def __init__(self, player_mode = "bot"): # initialize the game, default to bot mode
        self.board = [[0 for i in range(4)] for j in range(4)]
        self.score = 0
        self.moves = 0
        self.changed = False
        self.game_over = False
        self.top_value = 0
        self.player_mode = player_mode
        self.won = False
    
    def start(self): # begin the game
        self.add_tile()
        self.add_tile()
        
        if self.player_mode == "human":
            self.display()
            while not self.game_over: 
                move = input("Enter move: ") 
                self.move(move)
                self.display()
                self.game_over = self.check_game_over()
    
    def add_tile(self): # add a tile to the board
        x = random.randint(0, 3)
        y = random.randint(0, 3)

        while self.board[x][y] != 0:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        
        self.board[x][y] = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
        return
    
    def display(self):
        board_string = ""
        for i in range(4):
            board_string += "+----------" * 4 + "+\n"
            for j in range(4):
                board_string += "|{:10}".format(str(self.board[i][j]))
            board_string += "\n"

        print(board_string + "+----------" * 4 + "+")
        return

    def move(self, move = None):
        if move == "w":
            self.move_up()
        elif move == "a":
            self.move_left()
        elif move == "s":
            self.move_down()
        elif move == "d":
            self.move_right()
        else:
            print("Invalid move")
            self.move()
        
        if self.check_game_over():
            self.game_over = True
            return False
        
        if self.check_win():
            self.won = True
        
        if self.changed:
            self.add_tile()
            self.moves += 1
            self.changed = False
        return True
    
    def reverse(self, new_board): # https://github.com/yangshun/2048-python/blob/master/logic.py
        reversed = []
        for i in range(4):
            reversed.append([])
            for j in range(4):
                reversed[i].append(new_board[i][3-j])
        return reversed
    
    def transpose(self, new_board):
        transposed = []
        for i in range(4):
            transposed.append([])
            for j in range(4):
                transposed[i].append(new_board[j][i])

        return transposed
    
    def compress(self, new_board): # https://www.geeksforgeeks.org/2048-game-in-python/
        compressed = []
        for i in range(4):
            compressed.append([0] * 4)

        for i in range(4):
            pos = 0

            for j in range(4):
                if(new_board[i][j] != 0):
                    compressed[i][pos] = new_board[i][j]
                    pos += 1

        return compressed

    def merge(self, new_board):
        score = 0
        for i in range(4):
            for j in range(3):
                if new_board[i][j] == new_board[i][j+1] and new_board[i][j] != 0:
                    new_board[i][j] *= 2
                    score += new_board[i][j]
                    new_board[i][j+1] = 0
        return new_board, score
    
    def move_up(self):
        new_board = self.transpose(self.board)
        new_board = self.compress(new_board)
        new_board, score = self.merge(new_board)
        new_board = self.compress(new_board)
        new_board = self.transpose(new_board)

        if new_board != self.board:
            self.changed = True
            self.board = new_board
            self.score += score
        return
    
    def move_down(self):
        new_board = self.reverse(self.transpose(self.board))
        new_board = self.compress(new_board)
        new_board, score = self.merge(new_board)
        new_board = self.compress(new_board)
        new_board = self.transpose(self.reverse(new_board))

        if new_board != self.board:
            self.changed = True
            self.board = new_board
            self.score += score
        return
    
    def move_left(self):
        new_board = self.compress(self.board)
        new_board, score = self.merge(new_board)
        new_board = self.compress(new_board)

        if new_board != self.board:
            self.changed = True
            self.board = new_board
            self.score += score
        return
    
    def move_right(self):
        new_board = self.reverse(self.board)
        new_board = self.compress(new_board)
        new_board, score = self.merge(new_board)
        new_board = self.compress(new_board)
        new_board = self.reverse(new_board)

        if new_board != self.board:
            self.changed = True
            self.board = new_board
            self.score += score
        return

    def check_moves_available(self):
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    return True

        for i in range(4):
            for j in range(3):
                if self.board[i][j] == self.board[i][j+1]:
                    return True
                if self.board[j][i] == self.board[j+1][i]:
                    return True

        return False

    def check_game_over(self):
        if self.check_moves_available():
            return False
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    return False
        
        print("Game over!")
        print("Score: " + str(self.score))
        print("Moves: " + str(self.moves))
        print("Top value: " + str(self.top_value))
        return True
    
    def check_win(self):
        for i in range(4):
            for j in range(4):
                if self.board[i][j] > self.top_value:
                    self.top_value = self.board[i][j]

                if self.board[i][j] == 2048:
                    return True

        return False
    
    def get_score(self):
        return self.score
    
    def get_moves(self):
        return self.moves
    
    def get_board(self):
        return self.board
    
    def get_top_value(self):
        return self.top_value


if __name__ == "__main__":
    game = Game(player_mode="human")
    game.start()