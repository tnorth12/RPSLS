#Child Class

from Trainer import Trainer


class Human(Trainer):
    def __init__(self):
        super().__init__("Player")
        
        pass

    def choose_starter(self):
        for rpsls in self.rpsls_list:
            print(f"Press {self.rpsls_list.index(rpsls) + 1} for {rpsls}")
        
        user_input = int(input("Make your choice:  "))
        self.selected_starter = self.rpsls_list[user_input -1]

        
        
        pass