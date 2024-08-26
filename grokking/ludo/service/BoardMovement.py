from grokking.ludo.service.userService import UserService
from grokking.ludo.service.snakeAndLadderService import SnakeAndLadderService
import random,time

class Board:
    def __init__(self):
        self.snake_and_ladder = SnakeAndLadderService()
        self.user_service = UserService()
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.players = ["alice","bob","charlie",""]

    def add_all_snakes_and_ladders(self, snakes, ladders):
        cnt = 0
        mixed = {**ladders, **snakes}
        for start in mixed:
            self.snake_and_ladder.add_jumps(cnt, start, mixed[start])
            cnt += 1

    def add_players(self, players):
        cnt = 0
        for player in players:
            self.user_service.create_user(player, "", "player" + str(cnt))
            cnt += 1

    def roll_dice(self):
        return random.randint(1, 6)

    def play_game(self):
        self.add_players(self.players)
        self.add_all_snakes_and_ladders(self.snakes,self.ladders)
        players = self.user_service.get_all_users()
        player_deque = []
        for player in players:
            player_deque.append(players[player])
        player_won = ""
        i = 0
        while player_won == "":

            while player_deque:
                curr_player = player_deque[i % len(player_deque)]
                dice_num = self.roll_dice()
                time.sleep(0.1)
                print(curr_player.name, curr_player.current_position, dice_num, i)
                current_pos = self.snake_and_ladder.new_position(curr_player, dice_num)
                print("after", curr_player.name, curr_player.current_position)

                if current_pos == 100:
                    player_won = curr_player.name
                    break

                i += 1
        return player_won
