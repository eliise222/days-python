from abc import abstractmethod, ABC
from typing import Any


class DataProcessor(ABC):
    def __init__(self):
        self._storage: list[str] = []
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

    def ingest(self, data: int | float | list[int | float]) -> None:
        """Action : Reçoit des nombres, les convertit en chaînes de
          caractères (str) et les ajoute à la file d'attente interne."""
        if not self.validate(data):
            raise Exception("Improper numeric data")

        list_of_data = []
        if isinstance(data, list):
            list_of_data = data
        else:
            list_of_data.append(data)

        for d in list_of_data:
            self._storage.append((self.count, str(d)))
            self.count += 1


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if type(data) is str:
            return True
        if type(data) is list:
            for elements in data:
                if type(elements) is not str:
                    return False
            return len(data) > 0
        return False

    def ingest(self, data: str | list[str]) -> None:
        """Action : Reçoit les textes et les stocke directement en interne."""
        if self.validate(data) is True:
            print(f"Trying to validate input {data}: {self.validate(data)}")
        else:
            raise Exception(f"Trying to validate input {data}: "
                            f"{self.validate(data)}")

        list_of_data = []
        if data is list[str]:
            list_of_data = data
        else:
            list_of_data.append(data)

        for d in list_of_data:
            self._storage.append((self.count, d))
            self.count += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is dict:
            for key, value in data.items():
                if type(key) is not str or type(value) is not str:
                    return False
            return True
        if type(data) is list:
            for elements in data:
                if type(elements) is not dict:
                    return False
            return True

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        """Action : Reçoit les dictionnaires, les convertit en format texte
        (pour qu'ils soient lisibles comme un log) et les stocke."""
        if self.validate(data) is True:
            print(f"Trying to validate input {data}: {self.validate(data)}")
        else:
            raise Exception(f"Trying to validate input {data}: "
                            f"{self.validate(data)}")

        list_of_data = []
        list_of_data.append(str(data))
        for d in list_of_data:
            self._storage.append((self.count, d))
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
        num_proc.ingest("foo")
    except Exception as e:
        print(f" Got exception: {e}")
    data_num_ok = [1, 2, 3, 4, 5]
    print(f" Processing data: {data_num_ok}")
    if num_proc.validate(data_num_ok) is True:
        num_proc.ingest(data_num_ok)
    print(" Extracting 3 values...")
    for e in range(3):
        rank, value = num_proc.output()
        print(f" Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    txt_proc = TextProcessor()
    is_valid_txt1 = txt_proc.validate(test1)
    print(f" Trying to validate input '{test1}': {is_valid_txt1}")
    txt_data_ok = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {txt_data_ok}")



if __name__ == "__main__":
    main()
