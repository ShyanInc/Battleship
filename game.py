# Battleship Game For My Codecadamy CS Course

# Creating ships details and methods
from types import NoneType


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
    ship_names = ["Carrier", "Battleship", "Destroyer", "Submarine", "Patrol Boat"]

    def __init__(self, owner):
        self.ships_alive = 5
        self.owner = owner
        self.carrier = Ship("Carrier", 5)
        self.battleship = Ship("Battleship", 4)
        self.destroyer = Ship("Destroyer", 3)
        self.submarine = Ship("Submarine", 3)
        self.patrol_boat = Ship("Patrol Boat", 2)
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
        if len(coords) == 0:
            return None
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
                    return False
            else:
                print("Coordinates are occupied!")
                return False
        for index in occupied_coords:
            self.board[index][2] = True
            self.board[index][3] = ship.name
        print("Ship is placed!")
        return True

    # coords in format "LetterNumber" "A1"
    def place_ship(self, ship_name, start_coords, direction, fleet):
        if ship_name == "patrol boat":
            ship_name = "_".join(ship_name.split())
        if hasattr(fleet, ship_name):
            ship = getattr(fleet, ship_name)
            if ship.is_placed == True:
                print("Ship is already placed!")
                return None

            start_coords = self.coords_to_nums(start_coords)
            if start_coords == None:
                return None

            start_coords_index = self.coords_to_index(start_coords)
            if start_coords_index == None:
                return None

            if self.place_on_board(start_coords_index, direction, ship):
                return True
        else:
            return "Unknown ship!"

class Player:
    
    def __init__(self, name):
        self.name = name
        self.fleet = Fleet(name)
        self.board = Board()

    def __repr__(self):
        description = ""
        return description

    def shoot(self, coords, enemy):
        coords = enemy.board.coords_to_nums(coords)
        while coords == None:
            coords = str(input("Enter coordinates: "))
            coords = enemy.board.coords_to_nums(coords)
        coords_index = enemy.board.coords_to_index(coords)
        board_coords = enemy.board.get_coords(coords_index)
        
        is_hit = False
        for name in self.fleet.ship_names:
            if name in board_coords[3]:
                if name == "Patrol Boat":
                    name = "_".join(name.split())
                is_destroyed = getattr(enemy.fleet, name.lower())
                is_destroyed = getattr(is_destroyed, "is_destroyed")
                # if is_destroyed == True:
                    # break
                is_hit = True
                if name == "Patrol Boat":
                    name = "_".join(name.split())
                ship = getattr(enemy.fleet, name.lower())
                ship_health = getattr(ship, "health")
                setattr(ship, "health", ship_health - 1)
                if getattr(ship, "health") == 0:
                    ship.destroyed()
                    print(ship.name + " is destroyed!")
                    enemy.fleet.ships_alive -= 1
                    board_coords[3] = ""
                else:
                    board_coords[3] = ""    
                    print(ship.name + " health = " + str(getattr(ship, "health")))
                break
        if not is_hit:
            print("Missed :(")
                

class Game:

    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)   

    def check_win(self):
        if self.player1.fleet.ships_alive == 0:
            print("Congratulations " + self.player2.name + " won!")
            return True
        elif self.player2.fleet.ships_alive == 0:
            print("Congratulations " + self.player1.name + " won!")
            return True

    def place_ships(self, player):
        player_ships = []
        for ship in player.fleet.ship_names:
            player_ships.append(ship)
        while len(player_ships) > 0:
            print(f"{player.name} place your ships!\nAvailable ships:")
            i = 1
            for ship in player_ships:
                print(str(i) + " - " + ship)
                i += 1
            input_ship = str(input("Enter the ship name: "))
            if input_ship in player.fleet.ship_names:
                coords = str(input("Enter the coordinates in format x: A-J, y: 0-9: "))
                direction = str(input("Enter the direction to place (up, down, left, right): "))
                if player.board.place_ship(input_ship.lower(), coords.upper(), direction.lower(), player.fleet):
                    player_ships.remove(input_ship.title())
            else:
                "Wrong input!"
            
    def start(self):
        self.place_ships(self.player1)
        self.place_ships(self.player2)

    def turn(self):
        player = self.player1
        enemy = self.player2
        while True:
            print(player.name + " It's your turn, you have 5 times to shoot.")
            for a in range(5):
                coords = str(input("Enter the coords: "))
                player.shoot(coords, enemy)
                if self.check_win():
                    return 0
            if player == self.player1:
                player = self.player2
                enemy = self.player1
            else:
                player = self.player1
                enemy = self.player2

if __name__ == "__main__":
    while True:
        player1 = str(input("Enter player's 1 name: "))
        player2 = str(input("Enter player's 2 name: "))
        game = Game(player1, player2)
        game.start()
        game.turn()
        replay = str(input("Do you want to replay? Y - yes, N - no: "))
        yes = ["Yes", "Y", "yes", "y"]
        if replay not in yes:
            break

