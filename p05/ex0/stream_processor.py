from abc import ABC, abstractmethod
from typing import Any


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
        else:
            return False

    def process(self, data: Any) -> str:
        count = len(data)
        total = sum(data)
        moy = total / count

        return f"Processed {count} numeric values, sum={total}, avg={moy}"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return type(data) is str

    def process(self, data: Any) -> str:
        caract = len(data)
        word = len(data.split())
        return f"Processed text: {caract} characters, {word} words"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return type(data) is str and ":" in data

    def process(self, data: Any) -> str:
        sep = data.split(":", 1)
        first = sep[0].strip()
        sec = sep[1].strip()
        return f"{first} level detected: {sec}"

    def format_output(self, result: str) -> str:
        return f"[INFO] {result}"


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    data = [1, 2, 3, 4, 5]
    try:

        process = NumericProcessor()
        print(f"Processing data: {data}")

        if process.validate(data):
            result = process.process(data)
        print("Validation: Numeric data verified")
        final = process.format_output(result)
        print(f"Output: {final}")

    except Exception as e:
        print(f"An error occurred : {e}")

    print("\nInitializing Text Processor...")
    text = "Hello Nexus World"

    try:
        proc = TextProcessor()
        print(f'Processing data : "{text}"')
        if proc.validate(text):
            resultat = proc.process(text)
        print("Validation: Text data verified")
        finalt = proc.format_output(resultat)
        print(f"Output: {finalt}")

    except Exception as e:
        print(f"An error occurred: {e}")

    print("\nInitializing Log Processor...")
    log = "ERROR: Connection timeout"
    try:
        prcs = LogProcessor()
        print(f'Processing data: "{log}"')
        if prcs.validate(log):
            print("Validation: log entry verified")
            rst = prcs.process(log)
        fin = prcs.format_output(rst)
        print(f"Output: {fin}")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("\n=== Polymorphic Processing Demo ===\n")

    print("Processing multiple data types through same interface...")

    processors = [NumericProcessor(), LogProcessor(), TextProcessor()]
    mult_data = [[1, 2, 3], "Hello world!", "INFO: System ready"]
    for i, dt in enumerate(mult_data, 1):
        for p in processors:
            try:
                if p.validate(dt):
                    res = p.process(dt)
                    out = p.format_output(res)
                    print(f"Result {i}: {out}")
                    break
            except Exception as e:
                print(f"An error occured: {e}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
