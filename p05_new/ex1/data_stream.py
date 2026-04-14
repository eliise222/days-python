from abc import abstractmethod, ABC
from typing import Any
import typing


class DataProcessor(ABC):
    def __init__(self):
        self._storage: list[typing.Tuple[int, str]] = []
        self.count: int = 0
        self.total_processed: int = 0

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
            self.total_processed += 1


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

        list_of_data = data if type(data) is list else [data]

        for d in list_of_data:
            self._storage.append((self.count, str(d)))
            self.count += 1
            self.total_processed += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is dict:
            return "log_level" in data and "log_message" in data
        if type(data) is list:
            if not data:
                return False
            return all(type(d) is dict and "log_level" in d for d in data)
        return False

    def ingest(self, data: dict | list[dict]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        list_of_data = data if type(data) is list else [data]

        for d in list_of_data:
            log_str = f"{d['log_level']}: {d['log_message']}"
            self._storage.append((self.count, log_str))
            self.count += 1
            self.total_processed += 1


class DataStream:
    def __init__(self):
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(f" DataStream error - Can't process element in stream: "
                      f"{element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data\n")
            return
        for proc in self._processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            print(f"{name}: total {proc.total_processed} items processed, "
                  f"remaining {len(proc._storage)} on processor")


def main():
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")

    stream_manager = DataStream()
    stream_manager.print_processors_stats()

    print("Registering Numeric Processor")
    num_proc = NumericProcessor()
    stream_manager.register_processor(num_proc)

    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message':
          'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
           ]

    print(f"\nSend first batch of data on stream: {batch}\n")
    stream_manager.process_stream(batch)
    stream_manager.print_processors_stats()

    print("\nRegistering other data processors")
    txt_proc = TextProcessor()
    log_proc = LogProcessor()
    stream_manager.register_processor(txt_proc)
    stream_manager.register_processor(log_proc)

    print("Send the same batch again")
    stream_manager.process_stream(batch)
    stream_manager.print_processors_stats()

    print("\nConsume some elements from the data processors: Numeric 3, Text 2"
          ", Log 1")
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        txt_proc.output()
    for _ in range(1):
        log_proc.output()

    stream_manager.print_processors_stats()


if __name__ == "__main__":
    main()
