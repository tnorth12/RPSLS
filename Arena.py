
from Human import Human
from AI import AI


class Arena:
    def __init__(self):
        self.human = Human()
        self.ai = AI()
        self.AI_wins = 0
        self.player_wins = 0
        pass

    def run_battle (self):
        print("Welcome to the Arena!")        
        self.players_choose_starters()
        self.winner_rpsls()
        self.series_winner()
        
                
    def players_choose_starters(self):
        self.human.choose_starter()
        self.ai.choose_starter()

    def winner_rpsls(self):             
        if self.human.selected_starter == "Scissors" and self.ai.selected_starter == "Paper":
            self.player_wins = self.player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Scissors" and self.human.selected_starter == "Paper":
            self.AI_wins = self.AI_wins + 1
            print("AI is the winner!")
        elif self.human.selected_starter == "Paper" and self.ai.selected_starter == "Rock":
            self.player_wins = self.player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Paper" and self.human.selected_starter == "Rock":
            self.AI_wins = self.AI_wins + 1
            print("AI is the winner!")
        elif self.human.selected_starter == "Rock" and self.ai.selected_starter == "Lizard":
            self.player_wins = self.player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Rock" and self.human.selected_starter == "Lizard":
            self.AI_wins = self.AI_wins + 1
            print("AI is the winner!")
        elif self.human.selected_starter == "Lizard" and self.ai.selected_starter == "Spock":
            self.player_wins = self.player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Lizard" and self.human.selected_starter == "Spock":
            self.AI_wins = self.AI_wins + 1
            print("AI is the winner!")
        elif self.human.selected_starter == "Spock" and self.ai.selected_starter == "Scissors":
            self.player_wins = self.player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Spock" and self.human.selected_starter == "Scissors":
            self.AI_wins = self.AI_wins + 1
            print("AI is the winner!")
        elif self.human.selected_starter == "Scissors" and self.ai.selected_starter == "Lizard":
            self.player_wins = self.player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Scissors" and self.human.selected_starter == "Lizard":
            self.AI_wins = self.AI_wins + 1
            print("AI is the winner!")
        elif self.human.selected_starter == "Lizard" and self.ai.selected_starter == "Paper":
            self.player_wins = self.player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Lizard" and self.human.selected_starter == "Paper":
            self.AI_wins = self.AI_wins + 1
            print("AI is the winner!")
        elif self.human.selected_starter == "Paper" and self.ai.selected_starter == "Spock":
            self.player_wins = self.player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Paper" and self.human.selected_starter == "Spock":
            self.AI_wins = self.AI_wins + 1
            print("AI is the winner!")
        elif self.human.selected_starter == "Spock" and self.ai.selected_starter == "Rock":
            self.player_wins = self.player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Spock" and self.human.selected_starter == "Rock":
            self.AI_wins = self.AI_wins + 1
            print("AI is the winner!")
        elif self.human.selected_starter == "Rock" and self.ai.selected_starter == "Scissors":
            self.player_wins = self.player_wins + 1
            print("Player is the winner!")
        elif self.ai.selected_starter == "Rock" and self.human.selected_starter == "Scissors":
            self.AI_wins = self.AI_wins + 1
            print("AI is the winner!")
        else:
            print("Tie game!")

    def series_winner(self):
        if self.player_wins >= 2:
            print("Player wins best of three!!") 
        elif self.AI_wins >= 2:
            print("AI wins best of three!!")
        else:
            self.players_choose_starters()
            self.winner_rpsls()
            self.series_winner()
            
        
        