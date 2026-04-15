from abc import abstractmethod, ABC
from typing import Any, Sequence


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self.count: int = 0

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def output(self) -> tuple[int, str]:
        """Action : (Héritée) Renvoie le rang et le texte."""
        if not self._storage:
            raise Exception("No data available to output")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if type(data) in (int, float):
            return True
        if type(data) is list:
            for element in data:
                if not (type(element) in (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: int | float | Sequence[int | float]) -> None:
        """Action : Reçoit des nombres, les convertit en chaînes de
          caractères (str) et les ajoute à la file d'attente interne."""
        if not self.validate(data):
            raise Exception("Improper numeric data")

        list_of_data: list[int | float] = []
        if isinstance(data, (int, float)):
            list_of_data.append(data)
        else:
            list_of_data.extend(data)

        for d in list_of_data:
            self._storage.append((self.count, str(d)))
            self.count += 1


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if type(data) is str:
            return True
        if type(data) is list:
            if len(data) == 0:
                return False
            for elements in data:
                if type(elements) is not str:
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")

        list_of_data: list[str] = data if isinstance(data, list) else [data]

        for d in list_of_data:
            self._storage.append((self.count, str(d)))
            self.count += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is dict:
            return "log_level" in data and "log_message" in data
        if type(data) is list:
            if not data:
                return False
            return all(type(d) is dict and "log_level" in d for d in data)
        return False

    def ingest(self, data: dict[str, Any] | list[dict[str, Any]]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        list_of_data: list[dict[str, Any]] = data if isinstance(data, list)\
            else [data]

        for d in list_of_data:
            log_str = f"{d['log_level']}: {d['log_message']}"
            self._storage.append((self.count, log_str))
            self.count += 1


def main() -> None:
    num_proc = NumericProcessor()
    print("=== Code Nexus - Data Processor ===\n")
    test1 = 42
    is_valide_num1 = num_proc.validate(test1)
    test2 = "Hello"
    is_valide_num2 = num_proc.validate(test2)
    print("Testing Numeric Processor...")
    print(f" Trying to validate input '{test1}': {is_valide_num1}")
    print(f" Trying to validate input '{test2}': {is_valide_num2}")

    print(" Test invalid ingestion of string 'foo' without prior validataion:")
    try:
        num_proc.ingest("foo")  # type: ignore
    except Exception as err:
        print(f" Got exception: {err}")

    data_num_ok = [1, 2, 3, 4, 5]
    print(f" Processing data: {data_num_ok}")
    if num_proc.validate(data_num_ok) is True:
        num_proc.ingest(data_num_ok)
    print(" Extracting 3 values...")

    for _ in range(3):
        rank, value = num_proc.output()
        print(f" Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    txt_proc = TextProcessor()
    is_valid_txt1 = txt_proc.validate(test1)
    print(f" Trying to validate input '{test1}': {is_valid_txt1}")
    txt_data_ok = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {txt_data_ok}")

    if txt_proc.validate(txt_data_ok) is True:
        txt_proc.ingest(txt_data_ok)
    print(" Extracting 1 value...")
    rank, value = txt_proc.output()
    print(f" Text value {rank}: {value}\n")

    print("Testing Log Processor...")
    log_proc = LogProcessor()
    is_valid_log = log_proc.validate(test2)
    print(f" Trying to validate input '{test2}': {is_valid_log}")

    data_log_ok = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
                  ]
    print(f" Processing data: {data_log_ok}")
    if log_proc.validate(data_log_ok):
        log_proc.ingest(data_log_ok)

    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = log_proc.output()
        print(f" Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
