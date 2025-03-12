#!/usr/bin/env python3
import sys
import chess
import chess.engine
import argparse
import os.path

class Game:
    def __init__(self):
        self.fen_file = "fen.txt"
        try:
            with open(self.fen_file, "r") as f:
                fen = f.read().strip()
                self.board = chess.Board(fen)
        except:
            print("Invalid FEN file. The board has been reset.")
            self.reset()
        self.engine = chess.engine.SimpleEngine.popen_uci("../usr/games/stockfish")
    
    def save_position(self):
        with open(self.fen_file, "w") as f:
            f.write(self.board.fen())
    
    def reset(self):
        self.board.reset()
        self.save_position()
    
    def make_move(self, move_str):
        try:
            move = chess.Move.from_uci(move_str)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.save_position()
                print(f"You played: {move_str}")
                print()
                print("Board:")
                print(self.board)
                print()
                if self.check_game_state():
                    return
                
                self.stockfish_move()
            else:
                print(f"Invalid move: {move_str}")
                print()
                print("Board:")
                print(self.board)
                print()
                print("Turn: White")
        except:
            print(f"Invalid move format: {move_str}. Use UCI format (e.g., 'e2e4')")
    
    def stockfish_move(self):
        result = self.engine.play(self.board, chess.engine.Limit(time=1))
        stockfish_move = result.move
        self.board.push(stockfish_move)
        self.save_position()
        print(f"Stockfish played: {stockfish_move.uci()}")
        print()
        print("Board:")
        print(self.board)
        print()
        self.check_game_state()
    
    def check_game_state(self):
        if self.board.is_checkmate():
            winner = "Black" if self.board.turn == chess.WHITE else "White"
            print(f"Checkmate! {winner} wins.")
            print("The board has been reset.")
            self.reset()
            return True
        elif self.board.is_stalemate():
            print("Game ended in stalemate.")
            print("The board has been reset.")
            self.reset()
            return True
        elif self.board.is_insufficient_material():
            print("Game ended due to insufficient material.")
            print("The board has been reset.")
            self.reset()
            return True
        elif self.board.is_fifty_moves():
            print("Game drawn (fifty move rule).")
            print("The board has been reset.")
            self.reset()
            return True
        elif self.board.is_repetition():
            print("Game drawn (threefold repetition).")
            print("The board has been reset.")
            self.reset()
            return True
        elif self.board.is_check():
            print("Check!")
        print("Turn:", "White" if self.board.turn == chess.WHITE else "Black")
        return False
    
    def close(self):
        """Close the chess engine"""
        if hasattr(self, 'engine'):
            self.engine.quit()

def main():
    parser = argparse.ArgumentParser(description="Play chess against Stockfish.")
    subparsers = parser.add_subparsers(dest="command")
    
    move_parser = subparsers.add_parser("move", help="Make a chess move")
    move_parser.add_argument("move_uci", help="Move in UCI format (e.g., 'e2e4')")
    
    args = parser.parse_args()
    game = Game()
    
    if args.command == "move" and hasattr(args, "move_uci"):
        game.make_move(args.move_uci)
    
    game.close()

if __name__ == "__main__":
    main()