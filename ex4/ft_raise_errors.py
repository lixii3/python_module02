def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    if plant_name is None:
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Error: Water level {water_level} "
                         "is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Error: Water level {water_level} "
                         "is too low (min 1)")
    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         "is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         "is too high (max 12)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")

    def test_trycatch(name: str, waterlvl: int, sunlvl: int) -> None:
        try:
            check_plant_health(name, waterlvl, sunlvl)
        except ValueError as e:
            print(e)

    print("\nTesting good values...")
    test_trycatch("michele", 5, 8)
    print("\nTesting empty plant name...")
    test_trycatch(None, 5, 8)
    print("\nTesting bad water level...")
    test_trycatch("michele", -1, 11)
    print("\nTesting bad sunlight hours...")
    test_trycatch("michele", 5, 18)
    print("\nAll error raising tests completed!")


'''
def main():
    test_plant_checks()


if __name__ == "__main__":
    main()
'''
