class Piece:
    def __init__(self, piece_name, composer, key):
        self.piece_name = piece_name
        self.composer = composer
        self.key = key


n = int(input())
pieces = []


for _ in range(n):
    piece_name, composer, key = input().split("|")
    piece = Piece(piece_name, composer, key)
    pieces.append(piece)


data = input()

while not data == "Stop":
    command = data.split("|")
    if command[0] == "Add":
        piece_name, composer, key = command[1:]
        if piece_name in [p.piece_name for p in pieces]:
            print(f"{piece_name} is already in the collection!")
        else:
            piece = Piece(piece_name, composer, key)
            pieces.append(piece)
            print(f"{piece_name} by {composer} in {key} added to the collection!")
    elif command[0] == "Remove":
        piece_name = command[1]
        if piece_name in [p.piece_name for p in pieces]:
            piece_to_remove = [p for p in pieces if piece_name == p.piece_name][0]
            pieces.remove(piece_to_remove)
            print(f"Successfully removed {piece_name}!")
        else:
            print(f"Invalid operation! {piece_name} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        piece_name, new_key = command[1:]
        if piece_name in [p.piece_name for p in pieces]:
            piece = [p for p in pieces if piece_name == p.piece_name][0]
            piece.key = new_key
            print(f"Changed the key of {piece_name} to {new_key}!")
        else:
            print(f"Invalid operation! {piece_name} does not exist in the collection.")
    data = input()

sorted_pieces = sorted(pieces, key=lambda p: (p.piece_name, p.composer))
for piece in sorted_pieces:
    print(f"{piece.piece_name} -> Composer: {piece.composer}, Key: {piece.key}")

