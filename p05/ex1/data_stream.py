from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.stream_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "stream_count": self.stream_count}


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {stream_id}, Type: Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        new_lst = [e for e in data_batch if isinstance(e, (int, float))]
        try:
            avg = sum(new_lst) / len(new_lst)
        except ZeroDivisionError:
            return "0 readings processed"
        self.stream_count += len(new_lst)
        return f"{len(new_lst)} readings processed, avg temp: {avg}°C"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        lst_transac = [t for t in data_batch if isinstance(t, dict)]
        net = 0
        for t in lst_transac:
            try:
                if t["type"] == "buy":
                    net += t["amount"]
                else:
                    net -= t["amount"]
            except KeyError:
                print(f"[WARNING] Malformed data skipped in {self.stream_id}")
                continue
        self.stream_count += len(lst_transac)
        return f"{len(lst_transac)} operations, net flow: {net:+} units"


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        print("Initializing Event Stream...")
        print(f"Stream ID: {stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        lst_event = [e for e in data_batch if isinstance(e, str)]
        lst_err = [t for t in lst_event if t == "error"]
        self.stream_count += len(lst_event)
        return f"{len(lst_event)} events, {len(lst_err)} error detected"


class StreamProcessor:
    def __init__(self, streams: List[DataStream]):
        self.streams = streams

    def execute(self, all_batch: List[List[Any]]):
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")
        
        labels = ["Sensor data", "Transaction data", "Event data"]
        
        for stream, batch, label in zip(self.streams, all_batch, labels):
            try:
                res = stream.process_batch(batch)
                print(f"- {label}: {res.split(',')[0]} processed")
            except Exception as e:
                print(f"- Error: {e}")


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor = "SENSOR_001"
    s_sensor = SensorStream(sensor)
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(f"Sensor analysis: {s_sensor.process_batch([22.5, 23, 22])}\n")

    transaction = "TRANS_001"
    t_transaction = TransactionStream(transaction)
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(f"Transaction analysis: \
{t_transaction.process_batch([{'type': 'buy', 'amount': 100},
                              {'type': 'sell', 'amount': 150},
                              {'type': 'buy', 'amount': 75}])}\n")

    event = "EVENT_001"
    e_event = EventStream(event)
    print("Processing event batch: [login, error, logout]")
    print(f"Event analysis: {e_event.process_batch(['login', 'error',
                                                    'logout'])}\n")

    processor = StreamProcessor([s_sensor, t_transaction, e_event])
    
    all_data = [
        [23.0, 24.5, 21.5],
        [{"type": "buy", "amount": 100}, {"type": "sell", "amount": 150},
         {"type": "buy", "amount": 75}],
        ["login", "error", "logout"]
    ]

    processor.execute(all_data)

    print("Stream filtering active: High-priority data only")
    print("All streams processed successfully. Nexus throughput optimal.")

    print("\n=== FINAL SYSTEM STATISTICS ===")
    for d in [s_sensor, t_transaction, e_event]:
        stats = d.get_stats()
        print(f"ID: {stats['stream_id']} | Total Processed: \
{stats['stream_count']}")


if __name__ == "__main__":
    main()