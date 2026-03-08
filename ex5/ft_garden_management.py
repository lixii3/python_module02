class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class Plant:
    def __init__(self, name: str,
                 water_level: int, sunlight_hours: int) -> None:
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager():
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.water_tank = 20
        self.plants: list[Plant] = []

    def fill_tank(self) -> None:
        self.water_tank = 20

    def add_plant(self, plant: Plant) -> None:
        if plant is None or plant.name is None:
            raise ValueError("Plant name cannot be empty!")
        self.plants.append(plant)
        print(f"Added {plant.name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        for plant in self.plants:
            try:
                self.check_water_tank()
            except WaterError as e:
                raise e
            plant.water_level += 1
            self.water_tank -= 1
            print(f"Watering {plant.name} - success")

    def check_plant_health(self, plant: Plant) -> None:
        if plant.name is None:
            raise ValueError("Error: Plant name cannot be empty!")
        if plant.water_level > 10:
            raise ValueError(f"Error checking {plant.name}: "
                             f"Water level {plant.water_level} "
                             "is too high (max 10)")
        elif plant.water_level < 1:
            raise ValueError(f"Error: Water level {plant.water_level} "
                             "is too low (min 1)")
        if plant.sunlight_hours < 2:
            raise ValueError(f"Error checking {plant.name}: Sunlight hours "
                             f"{plant.sunlight_hours} "
                             "is too low (min 2)")
        elif plant.sunlight_hours > 12:
            raise ValueError("Error checking {plant.name}: Sunlight hours "
                             f"{plant.sunlight_hours} "
                             "is too high (max 12)")
        print(f"{plant.name}: healthy (water: {plant.water_level},"
              f" sun: {plant.sunlight_hours})")

    def check_garden_health(self) -> None:
        for plant in self.plants:
            try:
                self.check_plant_health(plant)
            except ValueError as e:
                raise e

    def check_water_tank(self) -> None:
        if self.water_tank <= 0:
            raise WaterError("Not enough water in tank")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    garden = GardenManager("Lia")
    print("\nAdding plants to garden...")
    try:
        garden.add_plant(Plant("tomato", 9, 8))
        garden.add_plant(Plant("lettuce", 10, 6))
        garden.add_plant(Plant(None, 11, 11))
    except ValueError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    try:
        garden.water_plants()
    except WaterError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("Closing watering system (cleanup)")

    print("\nChecking plant health...")
    try:
        garden.check_garden_health()
    except ValueError as e:
        print(e)

    print("\nTesting error recovery...")
    garden.water_tank = 0
    try:
        garden.check_water_tank()
    except WaterError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


'''
def main():
    test_garden_management()


if __name__ == "__main__":
    main()
'''
