
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
        
        pass

    def players_choose_starters(self):
        self.human.choose_starter()
        self.ai.choose_starter()

    def winner_rpsls(self):
        if self.human.selected_starter == "Scissors" and self.ai.selected_starter == "Paper":
            self.arena_winner = "Player"
            print("Player is the winner!")
        elif self.ai.selected_starter == "Scissors" and self.human.selected_starter == "Paper":
            self.arena_winner = "AI"
            print("AI is the winner!")
        elif self.human.selected_starter == "Paper" and self.ai.selected_starter == "Rock":
            self.arena_winner = "Player"
            print("Player is the winner!")
        elif self.ai.selected_starter == "Paper" and self.human.selected_starter == "Rock":
            self.arena_winner = "AI"
            print("AI is the winner!"))
        elif self.human.selected_starter == "Rock" and self.ai.selected_starter == "Lizard":
            self.arena_winner = "Player"
            print("Player is the winner!")
        elif self.ai.selected_starter == "Rock" and self.human.selected_starter == "Lizard":
            self.arena_winner = "AI"
            print("AI is the winner!")
        elif self.human.selected_starter == "Lizard" and self.ai.selected_starter == "Spock":
            self.arena_winner = "Player"
            print("Player is the winner!")
        elif self.ai.selected_starter == "Lizard" and self.human.selected_starter == "Spock":
            self.arena_winner = "AI"
            print("AI is the winner!")
        elif self.human.selected_starter == "Spock" and self.ai.selected_starter == "Scissors":
            self.arena_winner = "Player"
            print("Player is the winner!")
        elif self.ai.selected_starter == "Spock" and self.human.selected_starter == "Scissors":
            self.arena_winner = "AI"
            print("AI is the winner!")
        elif self.human.selected_starter == "Scissors" and self.ai.selected_starter == "Lizard":
            self.arena_winner = "Player"
            print("Player is the winner!")
        elif self.ai.selected_starter == "Scissors" and self.human.selected_starter == "Lizard":
            self.arena_winner = "AI"
            print("AI is the winner!")
        elif self.human.selected_starter == "Lizard" and self.ai.selected_starter == "Paper":
            self.arena_winner = "Player"
            print("Player is the winner!")
        elif self.ai.selected_starter == "Lizard" and self.human.selected_starter == "Paper":
            self.arena_winner = "AI"
            print("AI is the winner!")
        elif self.human.selected_starter == "Paper" and self.ai.selected_starter == "Spock":
            self.arena_winner = "Player"
            print("Player is the winner!")
        elif self.ai.selected_starter == "Paper" and self.human.selected_starter == "Spock":
            self.arena_winner = "AI"
            print("AI is the winner!")
        elif self.human.selected_starter == "Spock" and self.ai.selected_starter == "Rock":
            self.arena_winner = "Player"
            print("Player is the winner!")
        elif self.ai.selected_starter == "Spock" and self.human.selected_starter == "Rock":
            self.arena_winner = "AI"
            print("AI is the winner!")
        elif self.human.selected_starter == "Rock" and self.ai.selected_starter == "Scissors":
            self.arena_winner = "Player"
            print("Player is the winner!")
        elif self.ai.selected_starter == "Rock" and self.human.selected_starter == "Scissors":
            self.arena_winner = "AI"
            print("AI is the winner!")
        else:
            print("Tie game!")
        