def garden_operations(op_type: str) -> None:
    if op_type == "value":
        try:
            int("abc")
        except ValueError:
            raise ValueError("Caught ValueError: invalid literal for int()")

    if op_type == "zero":
        try:
            42 / 0
        except ZeroDivisionError:
            raise ZeroDivisionError("Caught ZeroDivisionError:"
                                    " division by zero")

    elif op_type == "file":
        try:
            open("missing.txt")
        except FileNotFoundError:
            raise FileNotFoundError("Caught FileNotFoundError: "
                                    "No such file 'missing.txt'")

    elif op_type == "key":
        try:
            inventory = {"roses": 5, "tulips": 10}
            inventory["sunflower"]
        except KeyError:
            raise KeyError("Caught KeyError: 'missing_plant'")

    elif op_type == "all":
        try:
            garden_operations("value")
        except (ValueError) as e:
            raise e
        try:
            garden_operations("zero")
        except (ZeroDivisionError) as e:
            raise e
        try:
            garden_operations("file")
        except (FileNotFoundError) as e:
            raise e
        try:
            garden_operations("key")
        except (KeyError) as e:
            raise e


def test_error_types():
    print("=== Garden Error Types Demo ===")
    print("\nTesting ValueError...")
    try:
        garden_operations("value")
    except ValueError as e:
        print(e)
    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError as e:
        print(e)
    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as e:
        print(e)
    print("\nTesting KeyError...")
    try:
        garden_operations("key")
    except KeyError as e:
        print(e)
    print("\nTesting multiple errors together...")
    try:
        garden_operations("all")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


'''
def main():
    test_error_types()


if __name__ == "__main__":
    main()
'''
