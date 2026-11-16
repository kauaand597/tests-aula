def play_turn(game_board: list, x: int, y: int, piece: str):
    # Verifica se as coordenadas são válidas
    if not (0 <= x <= 2 and 0 <= y <= 2):
        return False
    # Verifica se a casa está vazia
    if game_board[y][x] != "":
        return False
    # Verifica se a peça é válida
    if piece not in ("X", "O"):
        return False
    game_board[y][x] = piece
    return True