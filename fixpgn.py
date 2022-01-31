import chess.pgn
import glob

def fix_names(game: chess.pgn.Game):
    if 'White' not in game.headers or 'Black' not in game.headers:
        return

    game.headers['White'] = game.headers['White'].upper()
    game.headers['Black'] = game.headers['Black'].upper()


for fname in glob.glob('*.pgn'):
    with open(fname) as pgn:
        while True:
            game = chess.pgn.read_game(pgn)
            if game is None:
                break

            fix_names(game)
            print(game, end="\n\n")
