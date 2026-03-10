def check_temperature(temp: str) -> int:
    temper: int
    try:
        temper = int(temp)
    except ValueError:
        raise ValueError(f"Error: '{temp}' is not a valid number")
    if temper < 0:
        raise ValueError(f"Error: {temper}°C is too cold for plants (min 0°C)")
    if temper > 40:
        raise ValueError(f"Error: {temper}°C is too hot for plants (max 40°C)")
    return temper


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    for i in range(4):
        x = input("\nTesting temperature: ")
        try:
            check_temperature(x)
            print(f"Temperature {x}°C is perfect for plants!")
        except ValueError as e:
            print(e)

    print("\nAll tests completed - program didn't crash!")


def main():
    test_temperature_input()


if __name__ == "__main__":
    main()
