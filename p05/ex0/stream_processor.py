from abc import ABC, abstractmethod
from typing import Any, List, Union


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is list:
            for element in data:
                if not (type(element) in (int, float)):
                    return False
            return True
        return False

    def process(self, data: Any) -> str:
        count: int = len(data)
        total: Union[int, float] = sum(data)
        moy: float = total / count if count > 0 else 0.0
        return f"Processed {count} numeric values, sum={total}, avg={moy}"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return type(data) is str

    def process(self, data: Any) -> str:
        caract: int = len(data)
        word: int = len(data.split())
        return f"Processed text: {caract} characters, {word} words"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return type(data) is str and ":" in data

    def process(self, data: Any) -> str:
        sep: List[str] = data.split(":", 1)
        first: str = sep[0].strip()
        sec: str = sep[1].strip()
        return f"{first} level detected: {sec}"

    def format_output(self, result: str) -> str:
        base_format: str = super().format_output(result)
        tag: str = "[ALERT]" if "ERROR" in base_format else "[INFO]"
        return f"{tag} {base_format}"


def main() -> None:
    print("=== CODE NEXUS DATA - PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    data: List[int] = [1, 2, 3, 4, 5]
    try:
        proc_num: NumericProcessor = NumericProcessor()
        print(f"Processing data: {data}")
        if proc_num.validate(data):
            print("Validation: Numeric data verified")
            result: str = proc_num.process(data)
            print(f"Output: {proc_num.format_output(result)}")
    except Exception as e:
        print(f"An error occurred : {e}")

    print("\nInitializing Text Processor...")
    text: str = "Hello Nexus World"
    try:
        proc_text: TextProcessor = TextProcessor()
        print(f'Processing data: "{text}"')
        if proc_text.validate(text):
            print("Validation: Text data verified")
            result_t: str = proc_text.process(text)
            print(f"Output: {proc_text.format_output(result_t)}")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("\nInitializing Log Processor...")
    log: str = "ERROR: Connection timeout"
    try:
        proc_log: LogProcessor = LogProcessor()
        print(f'Processing data: "{log}"')
        if proc_log.validate(log):
            print("Validation: Log entry verified")
            result_l: str = proc_log.process(log)
            print(f"Output: {proc_log.format_output(result_l)}")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("\n=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [NumericProcessor(), LogProcessor(),
                                       TextProcessor()
                                       ]
    mult_data: List[Any] = [[1, 2, 3], "Hello world!",
                                       "INFO: System ready"]

    for i, dt in enumerate(mult_data, 1):
        for p in processors:
            try:
                if p.validate(dt):
                    res: str = p.process(dt)
                    out: str = p.format_output(res)
                    print(f"Result {i}: {out}")
                    break
            except Exception as e:
                print(f"An error occured: {e}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
