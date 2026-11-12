class Player():
    def __init__(self,name,UID):
        self.name=name
        self.UID=UID

class Piece():
    def __init__(self,owner:Player|None,effect=[]):
        self.owner=owner

class Cell():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.piece:Piece|None=Piece(None)
    
    def get_piece(self):
        return self.piece
    

class Board():
    def __init__(self,length:int,width:int):
        self.length=length
        self.width=width
        # Create length x width board
        self.board:list[list[Cell]]=[[Cell(_x,_y) for _x in range(length)] for _y in range(width)]
    
    def get_cell(self,x:int,y:int):
        """Return the cell at (x, y). Raise IndexError if out of bounds."""
        if x >= self.length or y >= self.width or x < 0 or y < 0:
            raise IndexError(f"Coordinates ({x}, {y}) are out of bounds.")
        return self.board[y][x]
    
    def get_piece(self,x:int,y:int):
        """Return the piece at (x, y). Raise IndexError if out of bounds."""
        return self.get_cell(x,y).piece
    
    def remove_piece(self,x:int,y:int):
        """Remove the piece at (x, y). Raise IndexError if out of bounds."""
        cell=self.get_cell(x,y)
        cell.piece=None
        return
    
    def place_piece(self,x:int,y:int,player:Player):
        """Place the piece into (x, y). Return piece,Raise IndexError if out of bounds,ValueError if (x,y) has piece ."""
        cell=self.get_cell(x,y)
        if cell.piece != None:
            raise ValueError(f"Coordinates ({x}, {y}) have a piece")
        cell.piece=Piece(player)
        return cell.piece
    
    