from grokking.ludo.service.BoardMovement import Board


if __name__=="__main__":
    board=Board()
    player_won=board.play_game()
    print(player_won+" wins")