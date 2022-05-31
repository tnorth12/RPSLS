#Child Class

from Trainer import Trainer

import random

class AI(Trainer):
    def __init__(self):
        super().__init__("AI Player")
        pass

    def choose_starter(self):
        print("AI made a choice!")
        self.selected_starter = random.choice(self.rpsls_list)
        print(f"{self.name} chose {self.selected_starter}")
        
        pass
