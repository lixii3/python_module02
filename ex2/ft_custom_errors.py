

class Plant():
    def __init__(self, name: str, height: int, days: int, watering_need: int):
        self.name = name
        self.height = height
        self.days = days
        self.hydration = 20
        self.watering_need = watering_need if watering_need <= 20 else 20

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.days += 1
        if self.days % 2 == 1:
            self.grow()
        self.hydration -= 2

    def hydrate(self) -> None:
        self.hydration += 1
        if self.hydration > 20 or self.hydration <= 0:
            raise PlantError(self)


class Garden():
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants: dict[str, Plant] = {}
        self.water_tank = 20

    def add_plant(self, plant: Plant) -> None:
        self.plants.setdefault(plant.name, plant)

    def fill_tank(self) -> None:
        self.water_tank = 20

    def water(self, plant: Plant) -> None:
        if self.water_tank <= 0:
            raise WaterError()
        if plant.watering_need > self.water_tank:
            raise WaterError()
        plant.hydrate()
        self.water_tank -= plant.watering_need

    def water_garden(self) -> None:
        for plant in self.plants.values():
            self.water(plant)


class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, plant: Plant):
        super().__init__(f"Caught a garden error: The {plant.name} plant "
                         "is wilthing")
        self.faulty_plant = plant


class WaterError(GardenError):
    def __init__(self):
        super().__init__("Caught a garden error: "
                         "Not enough water in the tank!")


def main():
    garden: Garden = Garden("Paolo Ruffini")
    gabriele = Plant("Gabriele", 69, 96, 10)
    garden.add_plant(Plant("Hosa Meravijosah", 69, 96, 11))
    garden.add_plant(Plant("piedini", 1, 2, 3))
    garden.add_plant(gabriele)

    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        gabriele.hydrate()
    except PlantError as e:
        print(e)

    print("\nTesting WaterError...")
    for i in range(10):
        for plant in garden.plants.values():
            plant.age()
    try:
        garden.water_garden()
    except (WaterError, PlantError) as e:
        print(e)

    print("\nTesting catching all garden errors...")
    for i in range(20):
        try:
            gabriele.hydrate()
        except PlantError as e:
            print(e)
    try:
        garden.water_garden()
    except (WaterError, PlantError) as e:
        print(e)
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
