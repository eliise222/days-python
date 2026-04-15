from abc import abstractmethod, ABC
from typing import Any, Protocol, Sequence


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
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

    def ingest(self, data: int | float | Sequence[int | float]) -> None:
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

        list_of_data: list[str] = data if isinstance(data, list) else [data]

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

    def ingest(self, data: dict[str, Any] | list[dict[str, Any]]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        list_of_data: list[dict[str, Any]] = data if isinstance(data, list) \
            else [data]

        for d in list_of_data:
            log_str = f"{d['log_level']}: {d['log_message']}"
            self._storage.append((self.count, log_str))
            self.count += 1
            self.total_processed += 1


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
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
        print("\n== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            print(f"{name}: total {proc.total_processed} items processed, "
                  f"remaining {len(proc._storage)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            extract_data: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    extract_data.append(proc.output())
                except Exception:
                    break
            if extract_data:
                plugin.process_output(extract_data)


class CSVExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        value = []
        for idt, val in data:
            value.append(str(val))
        result = ",".join(value)
        print("CSV Output:")
        print(result)


class JSONExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pair = []
        for idt, val in data:
            pair.append(f'"item_{idt}": "{val}"')
        result = "{" + ", ".join(pair) + "}"

        print("JSON Output:")
        print(result)


def main() -> None:
    stream = DataStream()
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch_1 = ['Hello world', [3.14, -1, 2.71],
               [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use \
ssh instead'},
                {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
               42, ['Hi', 'five']]

    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")

    print("== DataStream statistics ==")
    print("No processor found, no data\n")

    print("Registering Processors\n")

    print(f"Send first batch of data on stream: {batch_1}\n")

    stream.process_stream(batch_1)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExport()
    stream.output_pipeline(3, csv_plugin)

    stream.print_processors_stats()

    batch_2 = [
        21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 \
days'}],
        [32, 42, 64, 84, 128, 168], 'World hello'
    ]

    print(f"\nSend another batch of data: {batch_2}")

    stream.process_stream(batch_2)
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    JSON_plugin = JSONExport()
    stream.output_pipeline(5, JSON_plugin)

    stream.print_processors_stats()


if __name__ == "__main__":
    main()
