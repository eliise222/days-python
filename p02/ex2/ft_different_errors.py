def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        "1" + 2
    else:
        return


def test_error_types():
    print("=== Garden Error Types Demo ===")

    catch_error_value = False
    catch_error_division = False
    catch_error_file = False
    catch_error_type = False

    print("Testing operation 0...")
    try:
        garden_operations(0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
        catch_error_value = True

    print("Testing operation 1...")
    try:
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
        catch_error_division = True

    print("Testing operation 2...")
    try:
        garden_operations(2)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
        catch_error_file = True

    print("Testing operation 3...")
    try:
        garden_operations(3)
    except TypeError as e:
        print(f"Caught TypeError: {e}")
        catch_error_type = True

    print("Testing operation 4...")
    try:
        garden_operations(4)
        print("Operation completed successfully")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError):
        print("This should not be printed")

    if catch_error_value and catch_error_division and \
       catch_error_file and catch_error_type:
        print("\nAll error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
