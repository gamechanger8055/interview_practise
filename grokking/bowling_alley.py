class Player:
    def __init__(self, name):
        self.name = name
        self.scores = [[] for _ in range(10)]  # 10 sets, each set has rolls
        self.current_set = 0
        self.current_roll = 0

    def roll(self, pin_count):
        self.scores[self.current_set].append(pin_count)
        self.current_roll += 1

    def calculate_score(self):
        total_score = 0
        for set_index in range(10):
            set_score = sum(self.scores[set_index])
            if self.is_spare(set_index):
                set_score += self.bonus_for_spare(set_index)
            elif self.is_strike(set_index):
                set_score += self.bonus_for_strike(set_index)
            total_score += set_score
        return total_score

    def is_strike(self, set_index):
        return len(self.scores[set_index]) == 1 and sum(self.scores[set_index]) == 10

    def is_spare(self, set_index):
        return len(self.scores[set_index]) == 2 and sum(self.scores[set_index]) == 10

    def bonus_for_strike(self, set_index):
        if set_index == 9:
            if len(self.scores[9]) == 3:
                return self.scores[9][1] + self.scores[9][2]
            elif len(self.scores[9]) == 2:
                return self.scores[9][1]
        elif set_index < 9:
            next_set = self.scores[set_index + 1]
            return sum(next_set[:2])

    def bonus_for_spare(self, set_index):
        if set_index == 9:
            return self.scores[9][2]
        elif set_index < 9:
            next_set = self.scores[set_index + 1]
            return next_set[0]


class Game:
    def __init__(self, players):
        self.players = players
        self.current_player_index = 0
        self.current_set = 0

    def start_game(self):
        self.current_set = 0
        self.current_player_index = 0

    def next_turn(self, pin_count):
        current_player = self.players[self.current_player_index]
        current_player.roll(pin_count)

        if current_player.current_roll == 2 or current_player.is_strike(self.current_set):
            self.current_player_index += 1
            current_player.current_roll = 0

            if self.current_player_index == len(self.players):
                self.current_set += 1
                self.current_player_index = 0

    def end_game(self):
        for player in self.players:
            print(f"{player.name}'s score: {player.calculate_score()}")

    def is_game_over(self):
        return self.current_set == 10

    def update_scores(self):
        pass


# Example usage:
players = [Player("Player1"), Player("Player2")]
game = Game(players)
game.start_game()
import random
while not game.is_game_over():
    pin_count = random.randint(1,10)

    game.next_turn(pin_count)

game.end_game()
