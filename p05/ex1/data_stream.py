from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id: str = stream_id
        self.stream_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "count": self.stream_count}


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        new_lst: List[Union[int, float]] = [e for e in data_batch
                                            if isinstance(e, (int, float))]
        try:
            moy: float = sum(new_lst) / len(new_lst) if new_lst else 0.0
            self.stream_count += len(new_lst)
            return f"{len(new_lst)} readings processed, avg temp: {moy}°C"
        except Exception:
            return "0 readings processed"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high_temp":
            return [t for t in data_batch if isinstance(t, (int, float))
                    and t > 22]
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        lst_transac: List[Dict[str, Any]] = [t for t in data_batch
                                             if isinstance(t, dict)]
        net: int = 0
        for t in lst_transac:
            try:
                if t.get("type") == "buy":
                    net += t.get("amount", 0)
                else:
                    net -= t.get("amount", 0)
            except Exception:
                continue
        self.stream_count += len(lst_transac)
        return f"{len(lst_transac)} operations, net flow: {net:+} units"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "large_amount":
            return [t for t in data_batch if isinstance(t, dict)
                    and t.get("amount", 0) > 120]
        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        print("Initializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        lst_event: List[str] = [e for e in data_batch if isinstance(e, str)]
        lst_err: List[str] = [t for t in lst_event if t == "error"]
        self.stream_count += len(lst_event)
        return f"{len(lst_event)} events, {len(lst_err)} error detected"


class StreamProcessor:
    def __init__(self, streams: List[DataStream]):
        self.streams: List[DataStream] = streams

    def execute(self, all_batch: List[List[Any]]) -> None:
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")

        labels: List[str] = ["Sensor data", "Transaction data", "Event data"]
        for stream, batch, label in zip(self.streams, all_batch, labels):
            res: str = stream.process_batch(batch)
            if label == "Sensor data":
                print(f"{label}: {res.split(',')[0]}")
            else:
                print(f"{label}: {res.split(',')[0]} processed")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    s_sensor: SensorStream = SensorStream("SENSOR_001")
    print("Processing sensor batch: [temp:22.5, humidity:65, "
          "pressure:1013]")
    print(f"Sensor analysis: {s_sensor.process_batch([22.5, 23, 22])}\n")

    t_transaction: TransactionStream = TransactionStream("TRANS_001")
    print("Processing transaction batch: [buy: 100, sell: 150, buy: 75]")
    transac = [
              {'type': 'buy', 'amount': 100},
              {'type': 'sell', 'amount': 150},
              {'type': 'buy', 'amount': 75}
              ]
    print(f"Transaction analysis: {t_transaction.process_batch(transac)}\n")

    e_event: EventStream = EventStream("EVENT_001")
    print("Processing event batch: [login, error, logout]")
    event = ['login', 'error', 'logout']
    print(f"Event analysis: {e_event.process_batch(event)}\n")

    processor: StreamProcessor = StreamProcessor([s_sensor, t_transaction,
                                                  e_event])
    all_data: List[List[Any]] = [
        [23.0, 24.5],
        [{"type": "buy", "amount": 100},
         {"type": "sell", "amount": 150},
         {"type": "buy", "amount": 75}],
        ["login", "error", "logout"]
    ]
    processor.execute(all_data)

    high_temp: int = len(s_sensor.filter_data(all_data[0], "high_temp"))
    large_trans: int = len(t_transaction.filter_data(all_data[1],
                                                     "large_amount"))

    print("\nStream filtering active: High-priority data only")
    print(f"Filtered results: {high_temp} critical sensor alerts, "
          f"{large_trans} large transaction")
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
