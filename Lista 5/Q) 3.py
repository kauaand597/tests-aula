def who_won(game_board: list):
    player_1_pieces = 0
    player_2_pieces = 0

    for row in game_board:
        for cell in row:
            if cell == 1:
                player_1_pieces += 1
            elif cell == 2:
                player_2_pieces += 1

    if player_1_pieces > player_2_pieces:
        return 1
    if player_2_pieces > player_1_pieces:
        return 2
    return 0