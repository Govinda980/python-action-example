import time


class Elevator:
    def __init__(self, floors=10):
        self.current_floor = 1  # Start at First Floor
        self.destination_floors = []  # List to store floor requests
        self.direction = None  # "up", "down", or None
        self.door_open = False

    def request_floor(self, floor):
        """Handles internal elevator requests."""
        if 1 <= floor <= 10 and floor not in self.destination_floors:
            self.destination_floors.append(floor)
            self.destination_floors.sort()  # Ensure sorted order
            print(f"Floor {floor} requested.")
        else:
            print("Invalid floor request or already requested.")

    def move_elevator(self):
        """Moves the elevator to handle requests."""
        while self.destination_floors:
            next_floor = self.destination_floors.pop(0)  # Get next floor in order
            self.direction = "up" if next_floor > self.current_floor else "down"

            while self.current_floor != next_floor:
                time.sleep(1)  # Simulate movement
                self.current_floor += 1 if self.direction == "up" else -1
                print(f"Elevator at floor {self.current_floor}")

            self.open_doors()

        self.direction = None
        print("Elevator idle.")

    def open_doors(self):
        """Opens and closes doors at the current floor."""
        print(f"Doors opening at floor {self.current_floor}")
        time.sleep(2)  # Simulate door open time
        print("Doors closing.")

    def call_elevator(self, floor):
        """Handles external elevator requests (calling elevator)."""
        print(f"Elevator called to floor {floor}.")
        self.request_floor(floor)


# Simulation
elevator = Elevator()

# External requests (people calling the elevator)
elevator.call_elevator(3)
elevator.call_elevator(7)

# Internal requests (passengers choosing floors)
elevator.request_floor(5)

elevator.move_elevator()
