
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
        self.winner_rpsls()
        self.series_winner()
        
        pass

    def players_choose_starters(self):
        self.human.choose_starter()
        self.ai.choose_starter()

    def winner_rpsls(self):
        if self.human.selected_starter == "Scissors" and self.ai.selected_starter == "Paper":
            player_wins = player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Scissors" and self.human.selected_starter == "Paper":
            AI_wins = AI_wins + 1
            print("AI is the winner!")
        elif self.human.selected_starter == "Paper" and self.ai.selected_starter == "Rock":
            player_wins = player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Paper" and self.human.selected_starter == "Rock":
            AI_wins = AI_wins + 1
            print("AI is the winner!")
        elif self.human.selected_starter == "Rock" and self.ai.selected_starter == "Lizard":
            player_wins = player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Rock" and self.human.selected_starter == "Lizard":
            AI_wins = AI_wins + 1
            print("AI is the winner!")
        elif self.human.selected_starter == "Lizard" and self.ai.selected_starter == "Spock":
            player_wins = player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Lizard" and self.human.selected_starter == "Spock":
            AI_wins = AI_wins + 1
            print("AI is the winner!")
        elif self.human.selected_starter == "Spock" and self.ai.selected_starter == "Scissors":
            player_wins = player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Spock" and self.human.selected_starter == "Scissors":
            AI_wins = AI_wins + 1
            print("AI is the winner!")
        elif self.human.selected_starter == "Scissors" and self.ai.selected_starter == "Lizard":
            player_wins = player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Scissors" and self.human.selected_starter == "Lizard":
            AI_wins = AI_wins + 1
            print("AI is the winner!")
        elif self.human.selected_starter == "Lizard" and self.ai.selected_starter == "Paper":
            player_wins = player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Lizard" and self.human.selected_starter == "Paper":
            AI_wins = AI_wins + 1
            print("AI is the winner!")
        elif self.human.selected_starter == "Paper" and self.ai.selected_starter == "Spock":
            player_wins = player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Paper" and self.human.selected_starter == "Spock":
            AI_wins = AI_wins + 1
            print("AI is the winner!")
        elif self.human.selected_starter == "Spock" and self.ai.selected_starter == "Rock":
            player_wins = player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Spock" and self.human.selected_starter == "Rock":
            AI_wins = AI_wins + 1
            print("AI is the winner!")
        elif self.human.selected_starter == "Rock" and self.ai.selected_starter == "Scissors":
            player_wins = player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Rock" and self.human.selected_starter == "Scissors":
            AI_wins = AI_wins + 1
            print("AI is the winner!")
        else:
            print("Tie game!")

        def series_winner(self):
            if self.arena.winner
        