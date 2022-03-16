# Battleship Game For My Codecadamy CS Course

# Creating ships details and methods
class Ships:
    def __init__(self):
        self.ship_names = ["Carrier", "Battleship", "Destroyer", "Submarine", "Patrol Boat"]
        # Name: [size, is_placed, is_destroyed]
        self.ship_details = {
            "Carrier": [5, False, False],
            "Battleship": [4, False, False],
            "Destroyer": [3, False, False],
            "Submarine": [3, False, False],
            "Patrol Boat": [2,False, False]
            }

    def __repr__(self):
        print(self.ship_details.items())
        description = "It's Ships class which contains ship names, ship sizes and methods."
        return description

    def placed(self, name):
        try:
            if self.ship_details[name][1] == False:
                self.ship_details[name][1] = True
        except KeyError:
            return 0

    def destroyed(self, name):
        try:
            if self.ship_details[name][2] == False:
                self.ship_details[name][2] = True
        except KeyError:
            return 0

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
        

    # ship - name of ship, coords in format "A1"
    def set_ship(self, ship, coords):
        coords_to_nums = []




ships = Ships()
board = Board()
# print(ships)
print(board.coords_to_nums("G2"))