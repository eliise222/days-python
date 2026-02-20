def garden_operations(choice: int) -> None:
    if choice == 'value':
        int("abc")
    elif choice == 'division':
        10 / 0
    elif choice == 'file':
        open("missing.txt", "r")
    elif choice == 'key':
        {}["missing_plant"]


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    errors_list = ['value', 'division', 'file', 'key']
    catch_error_value = False
    catch_error_division = False
    catch_error_file = False
    catch_error_key = False
    print("Testing ValueError...")
    try:
        garden_operations("value")
    except (ValueError) as e:
        print(f"Caught ValueError: {e}\n")
        catch_error_value = True

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("division")
    except (ZeroDivisionError) as e:
        print(f"Caught ZeroDivisionError: {e}\n")
        catch_error_division = True

    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except (FileNotFoundError) as e:
        print(f"Caught FileNotFoundError: {e}\n")
        catch_error_file = True

    print("Testing KeyError...")
    try:
        garden_operations("key")
    except (KeyError) as e:
        print(f"Caught KeyError: {e}\n")
        catch_error_key = True

    print('Testing multiple errors together...')
    for error in errors_list:
        try:
            garden_operations(error)
        except (ValueError, ZeroDivisionError, FileNotFoundError,
                KeyError) as e:
            print(f"Caught an error ({type(e).__name__}), \
but program continues!")
    if catch_error_key is True and catch_error_division is True and\
       catch_error_file is True and catch_error_value is True:
        print("\nAll error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
