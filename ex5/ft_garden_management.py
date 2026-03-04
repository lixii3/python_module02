class Plant:
    def __init__(self, name: str, height: int, lifeTime: int,
                 water_level: int, sunlight_hours: int) -> None:
        self.name = name
        self.height = height
        self.lifeTime = lifeTime
        self.__water_level = water_level
        self.__sunlight_hours = sunlight_hours

    def get_name(self) -> str:
        return (self.name)

    def get_height(self) -> int:
        return (self.height)

    def get_age(self) -> int:
        return (self.age)

    def get_water_level(self) -> int:
        return self.__water_level

    def get_sunlight_hours(self) -> int:
        return self.__sunlight_hours


class Garden():
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants: dict[str, Plant] = {}

    def add_plant(self, plant: Plant) -> None:
        self.plants.setdefault(plant.name, plant)


# ################custom errors##########################
class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, plant: Plant):
        super().__init__(f"Caught a garden error: The {plant.name} plant "
                         "is wilthing")
        self.faulty_plant = plant


class WaterError(GardenError):
    def __init__(self, message: str = "Caught a garden error: Not enough water in the tank!"):
        super().__init__(message)

class GardenManager():
    def __init__(self, ) -> None:
        self.gardens: dict[str, Garden] = {}
        self.water_tank = 20

    def create_garden(self, owner: str) -> None:
        self.gardens.setdefault(owner, Garden(owner))

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

    def check_plant_health(self, plant: Plant) -> None:
        if plant.get_name() is None:
            raise ValueError("Error: Plant name cannot be empty!")
        if plant.get_water_level() > 10:
            raise ValueError(f"Error: Water level {plant.get_water_level()} "
                             "is too high (max 10)")
        elif plant.get_water_level() < 1:
            raise ValueError(f"Error: Water level {plant.get_water_level()} "
                             "is too low (min 1)")
        if plant.get_sunlight_hours() < 2:
            raise ValueError(f"Error: Sunlight hours "
                             f"{plant.get_sunlight_hours()} "
                             "is too low (min 2)")
        elif plant.get_sunlight_hours() > 12:
            raise ValueError("Error: Sunlight hours "
                             f"{plant.get_sunlight_hours()} "
                             "is too high (max 12)")
        print(f"Plant '{plant.get_name()}' is healthy!")

    def check_garden_health(self, garden: Garden) -> None:
        for plant in garden.plants.values():
            try:
                self.check_plant_health(plant)
            except ValueError as e:
                raise e

    def water_plants(plant_list: list[Plant]) -> None:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None or plant.name is None:
                raise WaterError("Error: Cannot water None - invalid plant!")
            print(f"Watering {plant.name}")
        print("Watering completed successfully!")
