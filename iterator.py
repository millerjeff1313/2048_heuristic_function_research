from agent import Agent
from game import Game
import json


score_card = {}

def high_score(iter_num):
    scores = []
    top_values = []
    moves = []

    top_value = 0
    most_moves = 0
    highest_score = 0

    for i in range(iter_num):
        agent = Agent(["highest_score"])

        while not agent.get_game_over():
            agent.play()
        
        agent.get_game().display()
        scores.append(agent.get_game().get_score())
        top_values.append(agent.get_game().get_top_value())
        moves.append(agent.get_game().get_moves())

        if agent.get_game().get_top_value() > top_value:
            top_value = agent.get_game().get_top_value()
        if agent.get_game().get_moves() > most_moves:
            most_moves = agent.get_game().get_moves()
        if agent.get_game().get_score() > highest_score:
            highest_score = agent.get_game().get_score()
        print("\n")

    
    average_score = sum(scores) / len(scores)
    average_top_value = sum(top_values) / len(top_values)
    average_moves = sum(moves) / len(moves)

    score_card["highest_score"] = {"highest_score": highest_score, "top_value": top_value, "most_moves": most_moves, "average_score": average_score, "average_top_value": average_top_value, "average_moves": average_moves}


def random(iter_num):
    scores = []
    top_values = []
    moves = []

    top_value = 0
    most_moves = 0
    highest_score = 0

    for i in range(iter_num):
        agent = Agent([])

        while not agent.get_game_over():
            agent.play()
        
        agent.get_game().display()
        scores.append(agent.get_game().get_score())
        top_values.append(agent.get_game().get_top_value())
        moves.append(agent.get_game().get_moves())

        if agent.get_game().get_top_value() > top_value:
            top_value = agent.get_game().get_top_value()
        if agent.get_game().get_moves() > most_moves:
            most_moves = agent.get_game().get_moves()
        if agent.get_game().get_score() > highest_score:
            highest_score = agent.get_game().get_score()
        print("\n")
    
    
    average_score = sum(scores) / len(scores)
    average_top_value = sum(top_values) / len(top_values)
    average_moves = sum(moves) / len(moves)

    score_card["random"] = {"highest_score": highest_score, "top_value": top_value, "most_moves": most_moves, "average_score": average_score, "average_top_value": average_top_value, "average_moves": average_moves}


    # score_card["random"] = {"scores": scores, "top_values": top_values, "moves": moves, "highest_score": highest_score, "top_value": top_value, "most_moves": most_moves}

def weighted_empty_tiles(iter_num):
    scores = []
    top_values = []
    moves = []

    top_value = 0
    most_moves = 0
    highest_score = 0

    for i in range(iter_num):
        agent = Agent(["weighted_empty_tiles"])

        while not agent.get_game_over():
            agent.play()
        
        agent.get_game().display()
        scores.append(agent.get_game().get_score())
        top_values.append(agent.get_game().get_top_value())
        moves.append(agent.get_game().get_moves())

        if agent.get_game().get_top_value() > top_value:
            top_value = agent.get_game().get_top_value()
        if agent.get_game().get_moves() > most_moves:
            most_moves = agent.get_game().get_moves()
        if agent.get_game().get_score() > highest_score:
            highest_score = agent.get_game().get_score()
        print("\n")

    
    average_score = sum(scores) / len(scores)
    average_top_value = sum(top_values) / len(top_values)
    average_moves = sum(moves) / len(moves)

    score_card["weighted_empty_tiles"] = {"highest_score": highest_score, "top_value": top_value, "most_moves": most_moves, "average_score": average_score, "average_top_value": average_top_value, "average_moves": average_moves}


def maximize_empty_tiles(iter_num):
    scores = []
    top_values = []
    moves = []

    top_value = 0
    most_moves = 0
    highest_score = 0

    for i in range(iter_num):
        agent = Agent(["maximize_empty_tiles"])

        while not agent.get_game_over():
            agent.play()
        
        agent.get_game().display()
        scores.append(agent.get_game().get_score())
        top_values.append(agent.get_game().get_top_value())
        moves.append(agent.get_game().get_moves())

        if agent.get_game().get_top_value() > top_value:
            top_value = agent.get_game().get_top_value()
        if agent.get_game().get_moves() > most_moves:
            most_moves = agent.get_game().get_moves()
        if agent.get_game().get_score() > highest_score:
            highest_score = agent.get_game().get_score()
        print("\n")

        
    average_score = sum(scores) / len(scores)
    average_top_value = sum(top_values) / len(top_values)
    average_moves = sum(moves) / len(moves)

    score_card["maximize_empty_tiles"] = {"highest_score": highest_score, "top_value": top_value, "most_moves": most_moves, "average_score": average_score, "average_top_value": average_top_value, "average_moves": average_moves}

def smoothness(iter_num):
    scores = []
    top_values = []
    moves = []

    top_value = 0
    most_moves = 0
    highest_score = 0

    for i in range(iter_num):
        agent = Agent(["smoothness"])

        while not agent.get_game_over():
            agent.play()
        
        agent.get_game().display()
        scores.append(agent.get_game().get_score())
        top_values.append(agent.get_game().get_top_value())
        moves.append(agent.get_game().get_moves())

        if agent.get_game().get_top_value() > top_value:
            top_value = agent.get_game().get_top_value()
        if agent.get_game().get_moves() > most_moves:
            most_moves = agent.get_game().get_moves()
        if agent.get_game().get_score() > highest_score:
            highest_score = agent.get_game().get_score()
        print("\n")

    average_score = sum(scores) / len(scores)
    average_top_value = sum(top_values) / len(top_values)
    average_moves = sum(moves) / len(moves)

    score_card["smoothness"] = {"highest_score": highest_score, "top_value": top_value, "most_moves": most_moves, "average_score": average_score, "average_top_value": average_top_value, "average_moves": average_moves}


def edge_weight(iter_num):
    scores = []
    top_values = []
    moves = []

    top_value = 0
    most_moves = 0
    highest_score = 0

    for i in range(iter_num):
        agent = Agent(["edge_weight"])

        while not agent.get_game_over():
            agent.play()
        
        agent.get_game().display()
        scores.append(agent.get_game().get_score())
        top_values.append(agent.get_game().get_top_value())
        moves.append(agent.get_game().get_moves())

        if agent.get_game().get_top_value() > top_value:
            top_value = agent.get_game().get_top_value()
        if agent.get_game().get_moves() > most_moves:
            most_moves = agent.get_game().get_moves()
        if agent.get_game().get_score() > highest_score:
            highest_score = agent.get_game().get_score()
        print("\n")

    average_score = sum(scores) / len(scores)
    average_top_value = sum(top_values) / len(top_values)
    average_moves = sum(moves) / len(moves)

    score_card["edge_weight"] = {"highest_score": highest_score, "top_value": top_value, "most_moves": most_moves, "average_score": average_score, "average_top_value": average_top_value, "average_moves": average_moves}

def smooth_weighted_empty(iter_num):
    scores = []
    top_values = []
    moves = []

    top_value = 0
    most_moves = 0
    highest_score = 0

    for i in range(iter_num):
        agent = Agent(["smoothness", "weighted_empty_tiles"])

        while not agent.get_game_over():
            agent.play()
        
        agent.get_game().display()
        scores.append(agent.get_game().get_score())
        top_values.append(agent.get_game().get_top_value())
        moves.append(agent.get_game().get_moves())

        if agent.get_game().get_top_value() > top_value:
            top_value = agent.get_game().get_top_value()
        if agent.get_game().get_moves() > most_moves:
            most_moves = agent.get_game().get_moves()
        if agent.get_game().get_score() > highest_score:
            highest_score = agent.get_game().get_score()
        print("\n")

    average_score = sum(scores) / len(scores)
    average_top_value = sum(top_values) / len(top_values)
    average_moves = sum(moves) / len(moves)

    score_card["smooth_weighted_empty"] = {"highest_score": highest_score, "top_value": top_value, "most_moves": most_moves, "average_score": average_score, "average_top_value": average_top_value, "average_moves": average_moves}


def smooth_weighted_empty_high_score(iter_num):
    scores = []
    top_values = []
    moves = []

    top_value = 0
    most_moves = 0
    highest_score = 0

    for i in range(iter_num):
        agent = Agent(["smoothness", "weighted_empty_tiles", "highest_score"])

        while not agent.get_game_over():
            agent.play()
        
        agent.get_game().display()
        scores.append(agent.get_game().get_score())
        top_values.append(agent.get_game().get_top_value())
        moves.append(agent.get_game().get_moves())

        if agent.get_game().get_top_value() > top_value:
            top_value = agent.get_game().get_top_value()
        if agent.get_game().get_moves() > most_moves:
            most_moves = agent.get_game().get_moves()
        if agent.get_game().get_score() > highest_score:
            highest_score = agent.get_game().get_score()
        print("\n")

    average_score = sum(scores) / len(scores)
    average_top_value = sum(top_values) / len(top_values)
    average_moves = sum(moves) / len(moves)

    score_card["smooth_weighted_empty_high_score"] = {"highest_score": highest_score, "top_value": top_value, "most_moves": most_moves, "average_score": average_score, "average_top_value": average_top_value, "average_moves": average_moves}


def smooth_weighted_empty_max_empty(iter_num):
    scores = []
    top_values = []
    moves = []

    top_value = 0
    most_moves = 0
    highest_score = 0
    max_empty = 0

    for i in range(iter_num):
        agent = Agent(["smoothness", "weighted_empty_tiles", "maximize_empty_tiles"])

        while not agent.get_game_over():
            agent.play()
        
        agent.get_game().display()
        scores.append(agent.get_game().get_score())
        top_values.append(agent.get_game().get_top_value())
        moves.append(agent.get_game().get_moves())
        # max_empty += agent.get_game().get_max_empty()

        if agent.get_game().get_top_value() > top_value:
            top_value = agent.get_game().get_top_value()
        if agent.get_game().get_moves() > most_moves:
            most_moves = agent.get_game().get_moves()
        if agent.get_game().get_score() > highest_score:
            highest_score = agent.get_game().get_score()

        print("\n")

    average_score = sum(scores) / len(scores)
    average_top_value = sum(top_values) / len(top_values)
    average_moves = sum(moves) / len(moves)

    score_card["smooth_weighted_empty_max_empty"] = {"highest_score": highest_score, "top_value": top_value, "most_moves": most_moves, "average_score": average_score, "average_top_value": average_top_value, "average_moves": average_moves}


if __name__ == "__main__":
    iter_num = 50
    random(iter_num)
    high_score(iter_num)
    maximize_empty_tiles(iter_num)
    weighted_empty_tiles(iter_num)
    smoothness(iter_num)
    edge_weight(iter_num)

    smooth_weighted_empty(iter_num) # top two
    smooth_weighted_empty_max_empty(iter_num) # top three


    score_card = json.dumps(score_card, indent=4)

    with open("scores.json", "a") as f:
        f.write(score_card)

    