class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class Plant():
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days
        self.water_level = 1

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.days += 1
        if self.days % 2 == 1:
            self.grow()
        self.water_level -= 2

    def hydrate(self) -> None:
        self.water_level += 1

    def check_status(self) -> None:
        if self.water_level > 20 or self.water_level < 0 or self.days > 50:
            raise PlantError(f"The {self.name} plant is wilting!")


class Garden():
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants: list[Plant] = []
        self.water_tank = 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)

    def fill_tank(self) -> None:
        self.water_tank = 10

    def water(self, plant: Plant) -> None:
        try:
            self.check_water_tank()
        except WaterError as e:
            raise e
        plant.hydrate()
        self.water_tank -= 1

    def water_garden(self) -> None:
        for plant in self.plants:
            self.water(plant)

    def check_water_tank(self) -> None:
        if self.water_tank <= 0:
            raise WaterError("Not enough water in tank")


def main() -> None:
    garden: Garden = Garden("Paolo Ruffini")
    gabriele = Plant("Gabriele", 12, 36)
    garden.add_plant(Plant("Hosa Meravijosah", 69, 49))
    garden.add_plant(Plant("piedini", 1, 2))
    garden.add_plant(gabriele)

    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")

    try:
        gabriele.water_level = 21
        gabriele.check_status()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")

    try:
        garden.water_garden()
    except GardenError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")

    try:
        gabriele.check_status()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        garden.water_garden()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
