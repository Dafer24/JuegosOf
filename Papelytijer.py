class Teory:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.valid_options = {
            "1": "rock",
            "2": "paper",
            "3": "scissors",
            "4": "lizard",
            "5": "spock"
        }

    def play(self):
        if self.player1 not in self.valid_options or self.player2 not in self.valid_options:
            print("Invalid options. Please enter one of the valid numbers: 1, 2, 3, 4, 5.")
            return

        if self.player1 == self.player2:
            print("It's a tie!")
        elif self.valid_options[self.player1] == self.getWinnerChoice(self.valid_options[self.player2]):
            print(f"Player 1 ({self.valid_options[self.player1]}) wins!")
        else:
            print(f"Player 2 ({self.valid_options[self.player2]}) wins!")

    def getWinnerChoice(self, choice):
        rules = {
            "rock": {"scissors", "lizard"},
            "paper": {"rock", "spock"},
            "scissors": {"paper", "lizard"},
            "lizard": {"paper", "spock"},
            "spock": {"rock", "scissors"}
        }
        return [c for c in rules if choice in rules[c]][0]


def wantToPlayAgain():
    choice = input("Do you want to play again? (yes/no): ").lower()
    return choice == "yes"


if __name__ == "__main__":
    while True:
        player_1 = input("Player 1, enter your choice (1 - rock, 2 - paper, 3 - scissors, 4 - lizard, 5 - spock): ")
        player_2 = input("Player 2, enter your choice (1 - rock, 2 - paper, 3 - scissors, 4 - lizard, 5 - spock): ")

        game = Teory(player_1, player_2)
        game.play()

        if not wantToPlayAgain():
            print("Thanks for playing!")
            break
