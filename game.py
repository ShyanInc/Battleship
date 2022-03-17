# Battleship Game For My Codecadamy CS Course

# Creating ships details and methods
class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.health = length
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
        0: "A", 1: "B", 2: "C", 3: "D", 4: "E",
        5: "F", 6: "G", 7: "H", 8: "I", 9: "J"
    }
    def __init__(self):
        self.board = []
        # Creating coordinates list
        # Format: [[x, y, is_occupied, ship_name]...[...]]
        for x in range(10):
            for y in range(10):
                self.board.append([x, y, False, ""])

    def __repr__(self):
        print(self.board)
        description = ""
        return description

    # Checks if given coords are in right format and convert to array[x,y]
    def check_coordinates(self, x, y):
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

    # Converts coords in "LetterNumber" format to [x, y]
    def coords_to_nums(self, coords):
        result = []
        if len(coords) != 2:
            print("Wrong coordinates!")
            return None
        checked = self.check_coordinates(coords[0], coords[1])
        if checked != None:
            result.append(checked)
            result.append(int(coords[1]))
        return result
        
    def coords_to_index(self, coords):
        return (coords[0] * 10 + coords[1])

    def get_coords(self, index):
        return self.board[index]

    # Changes coordinate directionaly
    def move_placement(self, current_coords, direction):
        if direction == "up":
            if current_coords - 1 < 0:
                current_coords += 10
            current_coords -= 1
            
        elif direction == "down":
            if current_coords + 1 >= len(self.board):
                current_coords -= 10
            current_coords += 1
            
        elif direction == "right":
            if current_coords + 10 >= len(self.board):
                current_coords -= 100
            current_coords += 10
        elif direction == "left":
            current_coords -= 10
        else:
            print("Wrong direction!")
            return None

        return current_coords

    # Verifies if place is available and occupy it
    def place_on_board(self, start_coords_index, direction, ship):
        current_coords = start_coords_index
        occupied_coords = []
        for temp in range(ship.length, 0, -1):
            if self.board[current_coords][2] == False:
                occupied_coords.append(current_coords)
                print(f"x:{self.board[current_coords][0]} y:{self.board[current_coords][1]}")
                current_coords = self.move_placement(current_coords, direction)
                if current_coords == None:
                    return None
            else:
                print("Coordinates are occupied!")
                return None
        for index in occupied_coords:
            self.board[index][2] = True
            self.board[index][3] = ship.name
        print("Ship is placed!")

    # coords in format "LetterNumber" "A1"
    def place_ship(self, ship_name, start_coords, direction, fleet):
        if hasattr(Fleet, ship_name):
            start_coords = self.coords_to_nums(start_coords)
            if start_coords == None:
                return None

            start_coords_index = self.coords_to_index(start_coords)

            ship = getattr(fleet, ship_name)
            self.place_on_board(start_coords_index, direction, ship)

        else:
            return "Unknown ship!"

class Player:
    def __init__(self, name):
        self.name = name
        self.fleet = Fleet(self.name)

    def __repr__(self):
        description = ""
        return description

    def shoot(self, coords, board):
        coords = board.coords_to_nums(coords)
        coords_index = board.coords_to_index(coords)
        print(board.get_coords(coords_index))
        
        


board = Board()

player_1 = Player("Alex")
player_1.shoot("A1", board)

# board.place_ship("carrier", "A1", "up", player_1.fleet)
# board.place_ship("carrier", "A6", "up", player_1.fleet)