
from Human import Human
from AI import AI


class Arena:
    def __init__(self):
        self.human = Human()
        self.ai = AI()
        pass

    def run_battle (self):
        print("Welcome to the Arena!")        
        self.players_choose_starters()        
        pass

    def players_choose_starters(self):
        self.human.choose_starter()
        self.ai.choose_starter()

    def winner_rpsls(self):
        self.rpsls_table = [[-1, 1, 0, 0, 4],[1, -1, 2, 3, 1],[0, 2, -1, 2, 4],[0, 3, 2, -1, 3],[4, 1, 4, 3, -1]]
        self.winner = self.rpsls_table[self.human.choose_starter][self.ai.choose_starter]
        print()
        if self.winner == self.human.choose_starter:
            print("Player wins that game!!")
        elif self.winner == self.ai.choose_starter:
            print("AI wins that game!!")
        else:
            print("Tie game")
        