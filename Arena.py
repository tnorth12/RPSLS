
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
        if self.human.choose_starter == "Scissors" and self.ai.choose_starter == "Paper":
            print("Player is the winner!")
        elif self.ai.choose_starter == "Scissors" and self.human.choose_starter == "Paper":
            print("AI is the winner")
        if self.human.choose_starter == "Paper" and self.ai.choose_starter == "Rock":
            print("Player is the winner!")
        elif self.ai.choose_starter == "Paper" and self.human.choose_starter == "Rock":
            print("AI is the winner")
        if self.human.choose_starter == "Rock" and self.ai.choose_starter == "Lizard":
            print("Player is the winner!")
        elif self.ai.choose_starter == "Rock" and self.human.choose_starter == "Lizard":
            print("AI is the winner")
        if self.human.choose_starter == "Lizard" and self.ai.choose_starter == "Spock":
            print("Player is the winner!")
        elif self.ai.choose_starter == "Lizard" and self.human.choose_starter == "Spock":
            print("AI is the winner")
        if self.human.choose_starter == "Spock" and self.ai.choose_starter == "Scissors":
            print("Player is the winner!")
        elif self.ai.choose_starter == "Spock" and self.human.choose_starter == "Scissors":
            print("AI is the winner")
        if self.human.choose_starter == "Scissors" and self.ai.choose_starter == "Lizard":
            print("Player is the winner!")
        elif self.ai.choose_starter == "Scissors" and self.human.choose_starter == "Lizard":
            print("AI is the winner")
        if self.human.choose_starter == "Lizard" and self.ai.choose_starter == "Paper":
            print("Player is the winner!")
        elif self.ai.choose_starter == "Lizard" and self.human.choose_starter == "Paper":
            print("AI is the winner")
        if self.human.choose_starter == "Paper" and self.ai.choose_starter == "Spock":
            print("Player is the winner!")
        elif self.ai.choose_starter == "Paper" and self.human.choose_starter == "Spock":
            print("AI is the winner")
        if self.human.choose_starter == "Spock" and self.ai.choose_starter == "Rock":
            print("Player is the winner!")
        elif self.ai.choose_starter == "Spock" and self.human.choose_starter == "Rock":
            print("AI is the winner")
        if self.human.choose_starter == "Rock" and self.ai.choose_starter == "Scissors":
            print("Player is the winner!")
        elif self.ai.choose_starter == "Rock" and self.human.choose_starter == "Scissors":
            print("AI is the winner")
        else:
            print("Tie game!")
        