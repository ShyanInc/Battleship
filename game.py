# Battleship Game For My Codecadamy CS Course

# Creating ships details and methods
class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.is_placed = False
        self.is_destroyed = False

    def placed(self):
        if self.is_placed == False:
            self.is_placed = True

    def destroyed(self):
        if self.is_destroyed == False:
            self.is_destroyed = True

class Fleet:
    carrier = Ship("Carrier", 5)
    battleship = Ship("Battleship", 4)
    destroyer = Ship("Destroyer", 3)
    submarine = Ship("Submarine", 3)
    patrol_boat = Ship("Patrol Boat", 2)

    def __init__(self, owner):
        self.owner = owner

    def __repr__(self):
        description = ""
        return description


# Creating a board to place ships
class Board:
    # Numeric coords to letters
    nums_to_letters_coords = {
        1: "A", 2: "B", 3: "C", 4: "D",5: "E",
        6: "F", 7: "G", 8: "H", 9: "I", 10: "J"
    }
    def __init__(self):
        self.board = []
        # Creating coordinates list
        # Format: [[x, y, is_occupied]...[...]]
        for x in range(10):
            for y in range(10):
                self.board.append([x, y, False])

    def __repr__(self):
        print(self.board)
        description = ""
        return description

    # Checks if given coords are in right format and convert to array[x,y]
    def check_coordinate(self, x, y):
        for key, value in self.nums_to_letters_coords.items():
            if x == value:
                try:
                    if int(y) >= 0 and int(y) <= 9:
                        return key
                    else:
                        print("Wrong y coordinate!")
                        return None
                except ValueError:
                    print("Wrong y coordinate!")
                    return None
        print("Wrong x coordinate!")
        return None

    def coords_to_nums(self, coords):
        result = []
        if len(coords) != 2:
            print("Wrong coordinates!")
            return None
        check = self.check_coordinate(coords[0], coords[1])
        if check != None:
            result.append(check)
            result.append(int(coords[1]))
        return result
        

    # ship - name of ship, coords in format "LetterNumber" "A1"
    def set_ship(self, ship_name, coords, fleet):
        if hasattr(Fleet, ship_name):
            coords = self.coords_to_nums(coords)
            ship = getattr(fleet, ship_name)
            ship_length = ship.length
            print(ship_length)
        else:
            return "Unknown ship!"




fleet = Fleet("player")
board = Board()

board.set_ship("carrier", "G2", fleet)