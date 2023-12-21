from game import Game
import random
import numpy as np

class Agent:
    def __init__(self, modes, verbose = True): # Initialize the agent and relevant variables
        self.modes = modes
        self.game = Game()
        self.game.start()
        self.move_options = ["w", "a", "s", "d"]
        self.game_over = False
        self.score = 0
        self.top_value = 0
        self.verbose = verbose


    def play(self):
        while not self.game.check_game_over():
            best_move = self.analyze(self.game.get_board())
            self.act(best_move)
            if self.verbose:
                self.game.display()

        self.game_over = True
        print("Game over")

        return

    # Analyze which move is best, make the action
    def act(self, best_move):
        self.game.move(best_move)
        return
    
    # Find which move is best
    def analyze(self, state):
        if self.modes == []:
            return random.choice(self.move_options)
        else:
            return self.minimax(state, self.modes)
        
    ############################################################
    # Use minimax algorithm to find the best move, evaluates based on weights for the corner and edge tiles
    def minimax(self, mat, modes):
        best_score, best_move = self.max_value(mat, 0, None, modes)
        return best_move
    
    def max_value(self, mat, prev_score, prev_action, modes, depth = 0):
        val = 0
        max_move = self.move_options[0]

        if depth == 5:
            return prev_score, prev_action

        for action in self.move_options:
            new_check = self.check_move(action)[0]
            
            move_score = 0

            for mode in modes:
                if mode == "highest_score":
                    move_score += self.highest_score(new_check)
                elif mode == "maximize_empty_tiles":
                    move_score += self.maximize_empty_tiles(new_check)
                elif mode == "smoothness":
                    move_score += self.smoothness(new_check)
                elif mode == "edge_weight":
                    move_score += self.edge_weight(new_check)
                elif mode == "weighted_empty_tiles":
                    move_score += self.weighted_empty_tiles(new_check)

            if new_check != mat:
                min_score, min_move = self.min_value(new_check, move_score, action, modes, depth + 1)
                if min_score > val:
                    val = min_score
                    max_move = action
            
        return val, max_move

    def min_value(self, mat, prev_score, prev_action, modes, depth = 0):
        val = np.inf
        min_move = self.move_options[-1]

        if depth == 5:
            return prev_score, prev_action

        for action in self.move_options:
            new_check = self.check_move(action)[0]
            
            move_score = 0

            for mode in modes:
                if mode == "highest_score":
                    move_score += self.highest_score(new_check)
                elif mode == "maximize_empty_tiles":
                    move_score += self.maximize_empty_tiles(new_check)
                elif mode == "smoothness":
                    move_score += self.smoothness(new_check)
                elif mode == "edge_weight":
                    move_score += self.edge_weight(new_check)
                elif mode == "weighted_empty_tiles":
                    move_score += self.weighted_empty_tiles(new_check)

            if new_check != mat:
                max_score, max_move = self.max_value(new_check, move_score, action, modes, depth + 1)

                if max_score < val:
                    val = max_score
                    min_move = action
                
        return val, min_move

    ############################################################
    # Find the move that will result in the highest score with weight towards the top left corner
    def edge_weight(self, check_board = None):
        if check_board == None:
            check_board = self.game.get_board()

        weight_matrix = [[8, 6, 4, 4], 
                        [6, 2, 1, 1], 
                        [4, 1, 1, 1], 
                        [4, 1, 1, 1]]
        score = 0

        for i in range(4):
            for j in range(4):
                score += check_board[i][j] * weight_matrix[i][j]

        return score
        
    ############################################################
    # Find the move that will result in the smoothest board
    def smoothness(self, check_board = None):
        if check_board == None:
            check_board = self.game.get_board()
        score = 0

        for i in range(4):
            for j in range(4):
                if j <= 2:
                    if check_board[i][j] == check_board[i][j+1]:
                        score += check_board[i][j]
                    if (check_board[i][j] == check_board[i][j+1] / 2) or (check_board[i][j] == check_board[i][j+1] * 2):
                        score += check_board[i][j] / 2

                if i <= 2:
                    if check_board[i][j] == check_board[i+1][j]:
                        score += check_board[i][j]
                    if (check_board[i][j] == check_board[i+1][j] / 2) or (check_board[i][j] == check_board[i+1][j] * 2):
                        score += check_board[i][j] / 2

                if j >= 1:
                    if check_board[i][j] == check_board[i][j-1]:
                        score += check_board[i][j]
                    if (check_board[i][j] == check_board[i][j-1] / 2) or (check_board[i][j] == check_board[i][j-1] * 2):
                        score += check_board[i][j] / 2
                
                if i >= 1:
                    if check_board[i][j] == check_board[i-1][j]:
                        score += check_board[i][j]
                    if (check_board[i][j] == check_board[i-1][j] / 2) or (check_board[i][j] == check_board[i-1][j] * 2):
                        score += check_board[i][j] / 2

        return score
    ############################################################
    # Find the move that will push empty tiles towards bottom right when possible
    def weighted_empty_tiles(self, check_board = None):
        if check_board == None:
            check_board = self.game.get_board()
        score = 0

        for i in range(4):
            for j in range(4):
                if check_board[i][j] == 0:
                    score += i + j     
        

        return score
    ############################################################
        
    ############################################################
    # Find the move that will result in the highest number of empty tiles
    def maximize_empty_tiles(self, check_board = None):
        if check_board == None:
            check_board = self.game.get_board()
        score = 0

        for i in range(4):
            for j in range(4):
                if check_board[i][j] == 0:
                    score += 1
        
        return score
    ############################################################
    
    ############################################################
    # Find the move that will result in the highest score
    def highest_score(self, check_board = None):
        if check_board == None:
            check_board = self.game.get_board()
        score = 0

        for i in range(4):
            for j in range(4):
                if check_board[i][j] > score:
                    score = check_board[i][j]

        return score
    ############################################################
    def check_move(self, move, check_board = None):
        if move == "w":
            return self.check_move_up(check_board)
        elif move == "a":
            return self.check_move_left(check_board)
        elif move == "s":
            return self.check_move_down(check_board)
        elif move == "d":
            return self.check_move_right(check_board)
    ############################################################
    def check_move_up(self, check_board = None):
        if check_board == None:
            check_board = self.game.get_board()

        new_check = self.game.transpose(check_board)
        new_check = self.game.compress(new_check)
        new_check, score = self.game.merge(new_check)
        new_check = self.game.compress(new_check)
        new_check = self.game.transpose(new_check)

        return new_check, score            

    def check_move_left(self, check_board = None):
        if check_board == None:
            check_board = self.game.get_board()

        new_check = self.game.compress(check_board)
        new_check, score = self.game.merge(new_check)
        new_check = self.game.compress(new_check)

        return new_check, score
    
    def check_move_down(self, check_board = None):
        if check_board == None:
            check_board = self.game.get_board()

        new_check = self.game.transpose(check_board)
        new_check = self.game.reverse(new_check)
        new_check = self.game.compress(new_check)
        new_check, score = self.game.merge(new_check)
        new_check = self.game.compress(new_check)
        new_check = self.game.reverse(new_check)
        new_check = self.game.transpose(new_check)

        return new_check, score
    
    def check_move_right(self, check_board = None):
        if check_board == None:
            check_board = self.game.get_board()

        new_check = self.game.reverse(check_board)
        new_check = self.game.compress(new_check)
        new_check, score = self.game.merge(new_check)
        new_check = self.game.compress(new_check)
        new_check = self.game.reverse(new_check)

        return new_check, score

    def get_game_over(self):
        return self.game_over
    
    def get_game(self):
        return self.game
        

if __name__ == "__main__":
    agent = Agent(["smoothness"])
    agent.play()


    # Modes:
    # highest_score
    # maximize_empty_tiles
    # weighted_empty_tiles
    # smoothness
    # edge_weight