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
    print("\nTesting temperature: 25")
    try:
        check_temperature("25")
        print("Temperature 25°C is perfect for plants!")
    except ValueError as e:
        print(e)
    print("\nTesting temperature: abc")
    try:
        check_temperature("abc")
    except ValueError as e:
        print(e)
    print("\nTesting temperature: 100")
    try:
        check_temperature("100")
    except ValueError as e:
        print(e)
    print("\nTesting temperature: -50")
    try:
        check_temperature("-50")
    except ValueError as e:
        print(e)

    print("\nAll tests completed - program didn't crash!")


'''
def main():
    test_temperature_input()


if __name__ == "__main__":
    main()
'''
