def check_temperature(temp: str) -> int:
    temper: int
    try:
        temper = int(temp)
    except ValueError as e:
        print(e)
    else:
        if temper >= 0 and temper <= 40:
            return temper
        else:
            if temper <= 0:
                                 " for plants (min 0°C)")
            else:
                raise ValueError("Temperature is too hot"
                                 " for plants (max 40°C)")

def test_temperature_input():
    print("Testing temperature: 25")
    try:
        check_temperature(25)
        print("Temperature 25°C is perfect for plants!")
    except ValueError as e:
        print(e)

    try:
        check_temperature("abc")
        print("Temperature 25°C is perfect for plants!")
    except ValueError as e:
        print(e)

    try:
        check_temperature("abc")
        print("Temperature 25°C is perfect for plants!")
    except ValueError as e:
        print(e)

    try:
        check_temperature("100", "-50")
        print("Temperature 25°C is perfect for plants!")
    except ValueError as e:
        print(e)

