class Plant():
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.days += 1
        if self.days % 2 == 1:
            self.grow()
        self.hydration -= 2


class WateringError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


def water_plants(plant_list: list[Plant]) -> None:
    print("Opening watering system")
    for plant in plant_list:
        if plant is None or plant.name is None:
            raise WateringError("Error: Cannot water None - invalid plant!")
        print(f"Watering {plant.name}")
    print("Watering completed successfully!")


def test_watering_system() -> None:
    good_list: list[Plant] = {
        Plant("PaoloRuffini", 5, 1),
        Plant("Gabriele", 3, 9),
        Plant("patata", 1, 1)}
    bad_list: list[Plant] = {
        Plant("PaoloRuffini", 5, 1),
        Plant(None, 3, 9),
        Plant("patata", 1, 1)}

    print("=== Garden Watering System ===")

    def ft_test(plant_list: list[Plant]) -> None:
        try:
            water_plants(plant_list)
        except WateringError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")

    print("\nTesting normal watering...")
    ft_test(good_list)
    print("\nTesting with error...")
    ft_test(bad_list)

# def main():
#     test_watering_system()


# if __name__ == "__main__":
#     main()
